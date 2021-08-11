import os
from zipfile import ZipFile, ZIP_DEFLATED
from shutil import rmtree
from consolemenu import *
from consolemenu.items import *

filesAbsPath = []
fileNames = []
extracted = []

def getZipFiles():
    print("FILES:\n")

    os.chdir('./') # dosya dosya geziyor.
    for item in os.listdir('./'):
        if item.endswith('.zip'):
            
            global fileAbsPath
            filesAbsPath.append(os.path.abspath(item))
            
            global fileName
            fileNames.append(item)

def mainMenu(fileNameList):
    menu = ConsoleMenu("FILES")
    for item in fileNameList:
        menuItem = FunctionItem(item, unzip, [fileNameList.index(item)])
        menu.append_item(menuItem)
    menu.show()

def unzip(index):
    print("Unzipping...")

    zip_ref = ZipFile(fileNames[index])

    global extracted
    extracted = zip_ref.namelist() # zipten çıkarılan dosya isimleri
    zip_ref.extractall('./')
    zip_ref.close()

    createZipFile(index)

def createZipFile(index):
    print("Creating symbols.zip...")
    zippedFiles = ZipFile(fileNames[index], 'w', ZIP_DEFLATED)

    for item in extracted:
        zippedFiles.write(item)

    zippedFiles.close()

    Clean()

def Clean():
    global filesAbsPath, fileNames, extracted

    print("Cleaning...")

    # os.remove(filesAbsPath[index])
    for item in extracted:
        if os.path.isdir(item) or os.path.isfile(item):
            rmtree(item)

    filesAbsPath = []
    fileNames = []
    extracted = []

    print("Finished successfully!")

def main():
    getZipFiles()
    mainMenu(fileNames)

if __name__ == "__main__":
    main()

# pyinstaller.exe --onefile --uac-admin --icon=icon.ico zipper.py      