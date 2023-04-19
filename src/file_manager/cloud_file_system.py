from file_manager.file_system_abstract import FileSystemAbstract


class CloudFileSystem(FileSystemAbstract):
    def if_exists(self, folder_path):
        pass  # TODO: implement for cloud based OS

    def read_dir_content(self, directory_path):
        pass  # TODO: implement for cloud based OS

    def create_dir(self, directory_path):
        pass  # TODO: implement for cloud based OS

    def copy_file(self, source_file, destination_file):
        pass  # TODO: implement for cloud based OS

    def remove_dir(self, directory_path):
        pass  # TODO: implement for cloud based OS

    def read_file(self, file_path):
        pass  # TODO: implement for cloud based OS

    def rename(self, old_path, new_path):
        pass  # TODO: implement for cloud based OS

    def remove_file(self, file_path):
        pass  # TODO: implement for cloud based OS
