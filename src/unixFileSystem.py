import os
import shutil

from src.oSAbstract import OSAbstract


class UnixFileSystem(OSAbstract):

    def if_exists(self, folder_path):
        return os.path.exists(folder_path)

    def read_dir_content(self, directory_path):
        try:
            return os.listdir(directory_path)
        except OSError as err:
            raise err

    def create_dir(self, directory_path):
        try:
            if not self.if_exists(directory_path):
                os.makedirs(directory_path)
        except OSError as err:
            raise err

    def copy_file(self, source_file, destination_file):
        try:
            shutil.copyfile(source_file, destination_file)
        except PermissionError as err:
            raise err
        except IOError as err:
            raise err

    def remove_dir(self, directory_path):
        try:
            os.rmdir(directory_path)
        except OSError as err:
            raise err

    def is_dir(self, file_path):
        return os.path.isdir(file_path)

    def read_file(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: file not found at {file_path}")
            return None
        except PermissionError:
            print(f"Error: insufficient permissions to read file at {file_path}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def remove_file(self, file_path):
        try:
            os.remove(file_path)
        except OSError as err:
            raise err

    def rename_file(self, old_filename, new_filename):
        try:
            os.rename(old_filename, new_filename)
        except OSError as err:
            raise err
