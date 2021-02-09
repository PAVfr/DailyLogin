
import os
import sys
import datetime
import subprocess
from bs4 import BeautifulSoup
import win32com.client

from DailyLogin.admin import Admin
from DailyLogin.message import Message



class TaskService:
    def __init__(self):
        # Get lists Tasks
        scheduler = win32com.client.Dispatch("Schedule.Service")
        scheduler.Connect()
        objTaskFolder = scheduler.GetFolder("\\")
        self.tasks = objTaskFolder.GetTasks(1)

        self.name = "DailyLogin (DarkOrbit)"
        self.path_run = sys.executable

        # Checks if the task exists.
        try:
            exist = [True for n in self.tasks if n.Name == self.name][0]
        except IndexError:
            self.create_task()
        else:
            # Compare path.
            path = None
            for value in [task.XML for task in self.tasks if task.Name == self.name]:
                soup = BeautifulSoup(value, features="html.parser")
                path = soup.find("task").find("actions").find("exec").text.split()[0]
                break
            if self.path_run != path:
                self.create_task()


    def create_task(self):
        r = subprocess.run(f'SCHTASKS /Create /F /SC ONLOGON /TN "{self.name}" /TR "{self.path_run}"', capture_output=True).stdout
        Message.task_update()
        return r
