import getpass
import sys
import os


USER_NAME = getpass.getuser()

class Start:

    def __init__(self,file_path=""):

        self._file_path = file_path
         
    def add_to_startup(self):

        if self._file_path == "":

            self._file_path = os.path.realpath(__file__)

        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME

        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
            #print(bat_file)
            bat_file.write(r'start "" %s' % self._file_path)
            #print(self._file_path)
            print("\n[*]Done embedding generate file into startup of the system.\n")

def rm_strt():

    ftd = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\open.bat' % USER_NAME
        
    if os.path.isfile(ftd):
        os.remove(ftd)
        print("File %s was erased." % ftd)
            
    else:

        print("Error occured...")
