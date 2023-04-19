from file_manager.cloud_file_system import CloudFileSystem
from file_manager.os_file_system import OSFileSystem


class Fabric:
    @staticmethod
    def get_needed_class_instance(file_system_type):
        if file_system_type == 'OS':
            return OSFileSystem()
        elif file_system_type == 'Cloud':
            return CloudFileSystem()
        else:
            raise ValueError('invalid file system type')
