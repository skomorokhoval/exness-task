import hashlib
import os
import sys


class FileSystemAbstract:

    def if_exists(self, folder_path):
        raise NotImplementedError("Method 'if_exists()' must be implemented.")

    def read_dir_content(self, folder_path):
        raise NotImplementedError("Method 'read_dir_content()' must be implemented.")

    def create_dir(self, directory_path):
        raise NotImplementedError("Method 'create_dir()' must be implemented.")

    def copy_file(self, source_file, destination_file):
        raise NotImplementedError("Method 'copy_file()' must be implemented.")

    def remove_dir(self, directory_path):
        raise NotImplementedError("Method 'remove_dir()' must be implemented.")

    def is_dir(self, file_path):
        raise NotImplementedError("Method 'is_dir()' must be implemented.")

    def read_file(self, file_path):
        raise NotImplementedError("Method 'read_file()' must be implemented.")

    def remove_file(self, file_path, ):
        raise NotImplementedError("Method 'remove_file()' must be implemented.")

    def rename_file(self, old_filename, new_filename):
        raise NotImplementedError("Method 'rename_file()' must be implemented.")

    def is_directory_empty(self, directory_path):
        return len(self.read_dir_content(directory_path)) == 0

    def copy_files_in_folder(self, src_folder_path, dst_folder_path):
        self.create_dir(dst_folder_path)
        files = self.read_dir_content(src_folder_path)

        for file in files:
            source_path = os.path.join(src_folder_path, file)
            target_path = os.path.join(dst_folder_path, file)

            if self.is_dir(source_path):
                self.copy_files_in_folder(source_path, target_path)
            else:
                self.copy_file(source_path, target_path)

    def delete_files(self, directory_path):
        files = self.read_dir_content(directory_path)
        for file in files:
            file_path = os.path.join(directory_path, file)
            if self.is_dir(file_path):
                self.delete_files(file_path)
                self.remove_dir(file_path)
            else:
                self.remove_file(file_path)
            print(f"Successfully deleted all contents of directory: {file_path}")

    def calculate_hashes_for_folder(self, directory_path):
        files = self.read_dir_content(directory_path)
        file_hashes = {}
        for file in files:
            file_path = f"{directory_path}/{file}"
            if self.is_dir(file_path):
                subfolder_hashes = self.calculate_hashes_for_folder(file_path)
                file_hashes.update(subfolder_hashes)
            else:
                data = self.read_file(file_path)
                result = hashlib.md5(data).hexdigest()
                file_hashes[result] = file

        return file_hashes

    def sync_dirs(self, source_directory_path, destination_directory_path):
        source_folder_hash = self.calculate_hashes_for_folder(source_directory_path)
        destination_folder_hash = self.calculate_hashes_for_folder(destination_directory_path)
        if len(source_folder_hash) != len(destination_folder_hash):
            return
        for key, value in source_folder_hash.items():
            test_value = destination_folder_hash.get(key)
            if test_value != value or (test_value is None and key not in destination_folder_hash):
                print(f"Content of ${value} is identical to  ${test_value}, but these files need to be renamed")
                old_path = self.find_file_in_directory(test_value, destination_directory_path)
                new_path = os.path.join(os.path.dirname(old_path), value)
                self.rename_file(old_path, new_path)

    def find_file_in_directory(self, file_name, directory_path):
        files = self.read_dir_content(directory_path)
        for file in files:
            file_path = f"{directory_path}/{file}"
            if self.is_dir(file_path):
                sub_filepath = self.find_file_in_directory(file_name, file_path)
                if sub_filepath:
                    return sub_filepath
            else:
                if file == file_name:
                    return file_path
            return None

    def analize_dirs(self, source_directory_path, destination_directory_path):
        if self.is_directory_empty(destination_directory_path):
            self.copy_files_in_folder(source_directory_path, destination_directory_path)
            print("Files are copied successfully")
            sys.exit()

        if self.is_directory_empty(source_directory_path):
            self.delete_files(destination_directory_path)
            print("Files are deleted successfully")
            sys.exit()

        self.sync_dirs(source_directory_path, destination_directory_path)


