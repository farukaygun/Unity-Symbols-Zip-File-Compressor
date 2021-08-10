from genericpath import exists, isfile
import os
from zipfile import ZipFile, ZIP_DEFLATED
from shutil import rmtree
from os.path import basename

dir_name = './'
extension = ".zip"
fileName = ""
extracted = []

def Unzip():
    print("Unzipping...")

    os.chdir(dir_name) # dosya dosya geziyor.
    for item in os.listdir(dir_name):
        if item.endswith(extension):

            global fileName
            fileName = os.path.abspath(item)
            zip_ref = ZipFile(fileName)

            global extracted
            extracted = zip_ref.namelist() # zipten çıkarılan dosya isimleri

            zip_ref.extractall(dir_name)
            zip_ref.close()

def CreateZipFile():
    print("Creating symbols.zip...")
    zippedFiles = ZipFile('symbols.zip', 'w', ZIP_DEFLATED)

    for item in extracted:
        zippedFiles.write(item)

    zippedFiles.close()

def Clean():
    print("Cleaning...")

    os.remove(fileName)
    for item in extracted:
        if os.path.isdir(item) or os.path.isfile(item):
            rmtree(item)

    print("Finished successfully!")


def Main():
    Unzip()
    CreateZipFile()
    Clean()

if __name__ == "__main__":
    Main()
    input("Press Enter to continue...")

# pyinstaller.exe --onefile --uac-admin --icon=icon.ico zipper.py      