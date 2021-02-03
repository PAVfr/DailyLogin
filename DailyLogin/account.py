
import os
import re

from DailyLogin.message import Message


class Account:
    path_file = "account.txt"

    @classmethod
    def read_file(cls) -> str:
        """Open and Return the string file"""
        if not os.path.exists(cls.path_file):
            with open(cls.path_file, mode="w", encoding="utf-8") as f:
                f.write(Message.file_account())
            # Open file for user
            os.system(cls.path_file)
        with open(cls.path_file, mode="r", encoding="utf-8") as f:
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
