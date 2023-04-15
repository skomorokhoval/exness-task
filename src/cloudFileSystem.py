from src.oSAbstract import OSAbstract


class CloudFileSystem(OSAbstract):
    async def if_exists(self, folder_path):
        pass  # TODO: implement for cloud based OS

    async def read_dir_content(self, directory_path):
        pass  # TODO: implement for cloud based OS

    async def create_dir(self, directory_path):
        pass  # TODO: implement for cloud based OS

    async def copy_file(self, source_file, destination_file):
        pass  # TODO: implement for cloud based OS

    async def remove_dir(self, directory_path):
        pass  # TODO: implement for cloud based OS

    async def read_file(self, file_path):
        pass  # TODO: implement for cloud based OS

    async def rename(self, old_path, new_path):
        pass  # TODO: implement for cloud based OS

    def remove_file(self, file_path):
        pass  # TODO: implement for cloud based OS
