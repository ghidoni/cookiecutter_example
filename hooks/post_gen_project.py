import os
import shutil

def move_files_and_folders_to_parent_directory():
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)

    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)
        new_path = os.path.join(parent_dir, item)
        shutil.move(item_path, new_path)

if __name__ == '__main__':
    if '{{ cookiecutter.create_directory }}'.lower() == 'n':
        move_files_and_folders_to_parent_directory()
        shutil.rmtree(os.getcwd())