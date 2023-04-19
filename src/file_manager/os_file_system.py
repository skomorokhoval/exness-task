import os
import shutil

from file_manager.file_system_abstract import FileSystemAbstract


class OSFileSystem(FileSystemAbstract):

    def if_exists(self, folder_path):
        return os.path.exists(folder_path)

    def read_dir_content(self, directory_path):
        return os.listdir(directory_path)

    def create_dir(self, directory_path):
        if not self.if_exists(directory_path):
            os.makedirs(directory_path)

    def copy_file(self, source_file, destination_file):
        shutil.copyfile(source_file, destination_file)

    def remove_dir(self, directory_path):
        os.rmdir(directory_path)

    def is_dir(self, file_path: str) -> bool:
        return os.path.isdir(file_path)

    def read_file(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                return f.read()
        except (FileNotFoundError, PermissionError, Exception):
            return None

    def remove_file(self, file_path):
        os.remove(file_path)

    def rename_file(self, old_filename, new_filename):
        os.rename(old_filename, new_filename)
