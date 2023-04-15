from src.cloudFileSystem import CloudFileSystem
from src.unixFileSystem import UnixFileSystem


class Fabric:
    @staticmethod
    def get_needed_class_instance(file_system_type):
        if file_system_type == 'UNIX':
            return UnixFileSystem()
        elif file_system_type == 'Cloud':
            return CloudFileSystem()
        else:
            raise ValueError('invalid OS type')
