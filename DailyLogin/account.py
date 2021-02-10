
import os
import sys
import re

from DailyLogin.message import Message


class Account:
    name_file = "account.txt"

    @classmethod
    def get_path_file(cls):
        if os.path.split(sys.executable)[-1] == "python.exe":
            return os.path.join(os.path.split(os.path.abspath("."))[0], cls.name_file)
        else:
            return os.path.join(os.path.split(sys.executable)[0], cls.name_file)


    @classmethod
    def read_file(cls) -> str:
        """Open and Return the string file"""
        path_file = cls.get_path_file()
        if not os.path.exists(path_file):
            with open(path_file, mode="w", encoding="utf-8") as f:
                f.write(Message.file_account())
            # Open file for user
            os.system(path_file)
        with open(path_file, mode="r", encoding="utf-8") as f:
            return f.read()


    @classmethod
    def get_account(cls) -> list:
        accounts = []
        for value in cls.read_file().splitlines():
            # Ignore the comments
            if value.startswith("#"):
                continue
            accounts.append(re.split(r"\s+", value, maxsplit=1))
        return accounts
