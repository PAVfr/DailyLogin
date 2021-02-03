
import sys
import requests
from win32com.client import Dispatch
from distutils.version import LooseVersion




class ApplicationEXE:
    def __init__(self):
        self.link_repo = "https://api.github.com/repos/PAVfr/DailyLogin/releases/latest"
        self.version_executable = self.get_version_exe()
        self.last_version = self.get_last_version(self.link_repo)

    @staticmethod
    def get_version_exe():
        from DailyLogin import _init__
        return _init__.__version__

    # def get_version_exe(filename):
        # parser = Dispatch("Scripting.FileSystemObject")
        # version = parser.GetFileVersion(filename)
        # return version

    @staticmethod
    def get_last_version(link: str) -> str:
        """
        Get the last version with url.
        :return: last version
        """
        resp = requests.get(link)
        if resp.status_code == 200:
            version = resp.json().get("tag_name")
            return version if version else "0.0.0.0"
        else:
            return "0.0.0.0"

    def compare_version(self):
        return LooseVersion(self.last_version) > LooseVersion(self.version_executable)
