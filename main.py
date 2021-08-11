import os
from zipfile import ZipFile, ZIP_DEFLATED
from shutil import rmtree
from consolemenu import *
from consolemenu.items import *

files_abs_path = []
filenames = []
extracted = []


class Zipper:

    @staticmethod
    def get_zip_files():
        print("FILES:\n")

        os.chdir('./')
        for item in os.listdir('./'):
            if item.endswith('.zip'):
                global files_abs_path
                files_abs_path.append(os.path.abspath(item))

                global filenames
                filenames.append(item)

    def main_menu(self, file_name_list):
        menu = ConsoleMenu("FILES")
        for item in file_name_list:
            menu_item = FunctionItem(item, self.unzip, [file_name_list.index(item)])
            menu.append_item(menu_item)
        menu.show()

    @staticmethod
    def unzip(self, index):
        print("Unzipping...")

        zip_ref = ZipFile(filenames[index])

        global extracted
        extracted = zip_ref.namelist()
        zip_ref.extractall('./')
        zip_ref.close()

        self.create_zip_file(index)

    @staticmethod
    def create_zip_file(self, index):
        print("Creating symbols.zip...")
        zipped_files = ZipFile(filenames[index], 'w', ZIP_DEFLATED)

        for item in extracted:
            zipped_files.write(item)

        zipped_files.close()

        self.clean()

    @staticmethod
    def clean():
        global files_abs_path, filenames, extracted

        print("Cleaning...")

        # os.remove(filesAbsPath[index])
        for item in extracted:
            if os.path.isdir(item) or os.path.isfile(item):
                rmtree(item)

        files_abs_path = []
        filenames = []
        extracted = []

        print("Finished successfully!")


def main():
    zipper = Zipper()
    zipper.get_zip_files()
    zipper.main_menu(filenames)


if __name__ == "__main__":
    main()
