
import shutil

import pytest

from file_manager.os_file_system import OSFileSystem

source = '/user/source'
destination = '/user/destination'


@pytest.fixture()
def os_file_system(monkeypatch, mocker):
    os_file_system = OSFileSystem()
    monkeypatch.setattr(os_file_system, 'read_dir_content', mocker.Mock(return_value=['file1.txt', 'file2.txt']))
    monkeypatch.setattr(os_file_system, 'create_dir', mocker.Mock(return_value=[]))
    monkeypatch.setattr(os_file_system, 'if_exists', mocker.Mock(return_value=[]))
    monkeypatch.setattr(os_file_system, 'copy_file', mocker.Mock(return_value=[]))
    monkeypatch.setattr(os_file_system, 'remove_dir', mocker.Mock(return_value=[]))
    monkeypatch.setattr(os_file_system, 'is_dir', mocker.Mock(return_value=[]))
    monkeypatch.setattr(os_file_system, 'read_file', mocker.Mock(return_value=[]))
    monkeypatch.setattr(os_file_system, 'remove_file', mocker.Mock(return_value=[]))
    monkeypatch.setattr(os_file_system, 'rename_file', mocker.Mock(return_value=[]))
    return os_file_system


def test_is_directory_not_empty(monkeypatch, os_file_system):
    # arrange

    # act
    not_empty = os_file_system.is_directory_empty(source)

    # assert
    os_file_system.read_dir_content.assert_called_once_with(source)
    assert not_empty is False


def test_is_directory_is_empty(monkeypatch, mocker, os_file_system):
    # arrange
    monkeypatch.setattr(os_file_system, 'read_dir_content', mocker.Mock(return_value=[]))

    # act
    empty_result = os_file_system.is_directory_empty(source)

    # assert
    os_file_system.read_dir_content.assert_called_once_with(source)
    assert empty_result is True


def test_copy_files_in_folder_so_no_folders_inside(monkeypatch, mocker, os_file_system):
    # arrange
    monkeypatch.setattr(os_file_system, 'is_dir', mocker.Mock(return_value=False))
    monkeypatch.setattr(shutil, 'copyfile', mocker.Mock(return_value=None))

    # act
    os_file_system.copy_files_in_folder(source, destination)

    # assert
    os_file_system.create_dir.assert_called_once_with(destination)
    os_file_system.read_dir_content.assert_called_once_with(source)
    assert os_file_system.create_dir.call_count == 1
    assert os_file_system.copy_file.call_count == 2


def test_copy_files_in_folder_so_folders_inside(monkeypatch, mocker, os_file_system):
    # arrange
    monkeypatch.setattr(os_file_system, 'read_dir_content', mocker.Mock(side_effect=[['folder', 'file2.txt'], ['file3.txt']]))
    mocker.patch.object(os_file_system, 'is_dir', side_effect=[True, False, False])

    # act
    os_file_system.copy_files_in_folder(source, destination)

    # assert
    os_file_system.create_dir.assert_has_calls([
        mocker.call(destination),
        mocker.call(destination + '/folder'),
    ])
    os_file_system.read_dir_content.assert_has_calls([
        mocker.call(source),
        mocker.call(source + '/folder'),
    ])
    assert os_file_system.create_dir.call_count == 2
    assert os_file_system.read_dir_content.call_count == 2
    assert os_file_system.copy_file.call_count == 2


