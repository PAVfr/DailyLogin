
import os
import requests
from bs4 import BeautifulSoup

from DailyLogin.message import Message



class Connection:
    web_agent = "BigpointClient"
    default_version = "1.4.6"
    version = None

    def __init__(self, user, password):
        self.user = user
        self.password = password

        if not self.version:
            Connection.version = self.get_version_client()

        self.session = requests.session()
        self.session.headers['User-Agent'] = f"{self.web_agent}/{self.version}"

        # Connect Login
        cnx = self.send_login()
        url_hangar: str = cnx.url

        dosid = cnx.headers.get("Set-Cookie").split(";", maxsplit=1)[0].replace("dosid=", "")
        server = url_hangar.split("/")[2].split(".")[0]

        print(Message.user_logged(), self.user)
        print(Message.dosid(), dosid)

        # List Links
        url_logout = f"https://{server}.darkorbit.com/indexInternal.es?action=externalLogout"
        url_daily_connect = f"https://{server}.darkorbit.com/flashAPI/dailyLogin.php?doBook=1"

        # Get Calendar
        dailylogin = self.session.get(url_daily_connect).text
        if dailylogin == '{"isError":1,"error":{"message":"Already booked today"}}':
            Message.calendar_already_done(user=self.user)
        elif dailylogin == '{"success":true}':
            Message.calendar_done(user=self.user)
        elif dailylogin == '{"isError":1,"error":{"message":"No rewards left"}}':
            Message.calendar_no_rewards_left(user=self.user)
        else:
            Message.user_pass_error()


    def get_link_post(self):
        html = self.session.get("https://darkorbit.com").text
        soup = BeautifulSoup(html, features="html.parser")
        dico = soup.find("form", {"name": "bgcdw_login_form"})
        return str(dico.get("action"))


    def send_login(self):
        data = {
            "username": self.user,
            "password": self.password
            }
        return self.session.post(self.get_link_post(), data=data)


    @classmethod
    def get_version_client(cls):
        url = "http://darkorbit-22-client.bpsecure.com/bpflashclient/windows.x64/repository/Updates.xml"
        session = requests.session()
        session.headers['User-Agent'] = cls.web_agent
        html = session.get(url).text
        try:
            soup = BeautifulSoup(html, features="html.parser")
            version = soup.find("version").text
        except AttributeError:
            print(Message.client())
            print("Client Version : ", cls.default_version)
            return cls.default_version
        else:
            Connection.version = version
            return version
