# explorer/folder_contents.py

import os

def list_folder_contents(folder_path):
    if not os.path.exists(folder_path):
        return f"Folder not found: {folder_path}"

    files = os.listdir(folder_path)
    return files
