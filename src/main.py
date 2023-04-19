import sys

from file_manager.fabric import Fabric


def main():
    _, source_directory_path, destination_directory_path, *args = sys.argv
    if args:
        file_system = args[0]
    else:
        file_system = 'OS'

    os_to_analyze = Fabric.get_needed_class_instance(file_system)

    if not os_to_analyze.if_exists(source_directory_path):
        raise Exception(source_directory_path + " does not exist")

    if not os_to_analyze.if_exists(destination_directory_path):
        raise Exception(destination_directory_path + " does not exist")

    os_to_analyze.analize_dirs(source_directory_path, destination_directory_path)
    print("Script is finished")


if __name__ == '__main__':
    main()
