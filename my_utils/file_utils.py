from genericpath import isfile
import os


def get_all_files(root_folder: str, file_list: list):
    """
    Gets all files recursively from the root folder and i'ts subfolders.
    root_folder: the root folder (str)
    file_list: an empty list being used for collect files (list)
    """
    # get files and subfolders from current dir
    folder_content = os.listdir(root_folder)

    # collect files and subfolders separately
    subfolders = []
    for i in folder_content:
        full_path = os.path.join(root_folder, i)
        
        if os.path.isfile(full_path):
            file_list.append(full_path)
        else:
            subfolders.append(full_path)
    
    # recursion
    if subfolders:
        for folder in subfolders:
            get_all_files(folder, file_list)