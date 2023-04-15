import os
import sys

from src.fabric import Fabric


def main():
    source = '/source'
    destination = '/destination'
    file_system = sys.argv[1:][0]

    source_directory_path = os.path.join(os.path.dirname(__file__) + source)
    destination_directory_path = os.path.join(os.path.dirname(__file__) + destination)
    os_file_system = Fabric.get_needed_class_instance(file_system)

    if not os_file_system.directory_exists(source_directory_path):
        raise Exception(f"{source} does not exist")

    if not os_file_system.directory_exists(destination_directory_path):
        raise Exception(f"{destination['destination']} does not exist")

    if os_file_system.is_directory_empty(destination_directory_path):
        os_file_system.copy_files_in_folder(source_directory_path, destination_directory_path)
        print("Files are copied successfully")
        sys.exit()

    if os_file_system.is_directory_empty(source_directory_path):
        os_file_system.delete_files(destination_directory_path)
        print("Files are deleted successfully")
        sys.exit()

    os_file_system.compare_dirs(source_directory_path, destination_directory_path)
    print("Script is finished")


if __name__ == '__main__':
    main()
