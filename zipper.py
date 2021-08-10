import os
from zipfile import ZipFile, ZIP_DEFLATED
from shutil import rmtree

fileAbsPath = ""
fileName = ""
extracted = []

def Unzip():
    print("Unzipping...")

    os.chdir('./') # dosya dosya geziyor.
    for item in os.listdir('./'):
        if item.endswith('.zip'):

            global fileAbsPath
            fileAbsPath = os.path.abspath(item)
            
            global fileName
            fileName = item

            zip_ref = ZipFile(fileName)

            global extracted
            extracted = zip_ref.namelist() # zipten çıkarılan dosya isimleri

            zip_ref.extractall('./')
            zip_ref.close()

def CreateZipFile():
    print("Creating symbols.zip...")
    zippedFiles = ZipFile(fileName + '.zip', 'w', ZIP_DEFLATED)

    for item in extracted:
        zippedFiles.write(item)

    zippedFiles.close()

def Clean():
    print("Cleaning...")

    os.remove(fileAbsPath)
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