import PyInstaller.__main__
import os
import shutil


PyInstaller.__main__.run([
    'game\\application.py',
    '--noconfirm',
    '--onedir',
    '--windowed',
    '--no-embed-manifest',
    '--add-data=game\\res;res\\'
])

shutil.rmtree("build")
os.remove("application.spec")
 
shutil.move("dist\\application",".")
shutil.rmtree("dist")

os.rename("application","Space Invaders")
