
import os
import sys
import webbrowser

from DailyLogin.admin import Admin
from DailyLogin.task import TaskService
from DailyLogin.message import Message
from DailyLogin.application_exe import ApplicationEXE
from DailyLogin.account import Account
from DailyLogin.connection import Connection



print("""
________  __________    __   _________________________
___  __ \ ___    |_ |  / /   ___  ____/__  __ \_|__  /
__  /_/ / __  /| |_ | / /    __  /_   __  /_/ /__/_ <
_  ____/___  ___ |_ |/ /     _  __/   _  _, _/____/ /
/_/    _(_)_/  |_|____/______/_/      /_/ |_| /____/
                      _/_____/

Contact Discord : PAV_FR#3269
\n
""")

# Instance for update language
Message()

# Create the task if it doesn't exist (if excecute in admin) and if file exe.
if Admin.is_admin() and os.path.split(sys.executable)[-1] != "python.exe":
    TaskService()

# Check Version .exe
if os.path.split(sys.executable)[-1] != "python.exe":
    app = ApplicationEXE()
    if app.compare_version():
        Message.last_version()
        os.system("PAUSE")
        webbrowser.open("https://github.com/PAVfr/DailyLogin")
        sys.exit(0)

# Start Accounts
for account in Account.get_account():
    cnx = Connection(*account)
