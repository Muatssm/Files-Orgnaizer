import os
import shutil

def move_files_to_folder(folder_path: str, files_extension: str, files_list: list, files_path: str, folders_dict: dict) -> None:
    for item in files_list:
        item_path = os.path.join(files_path, item)
        if os.path.isfile(item_path):
            item_name, item_extension = os.path.splitext(item_path)
            if item_extension == files_extension:
                destination_path = os.path.join(folder_path, item)
                shutil.move(item_path, destination_path)
                print(f"Move file from {item_path} to {destination_path}")
                folders_dict[files_extension] = f"{folder_path}"



def create_folder(path: str, name: str) -> str:
    base_path: str = path
    folder_name: str = name
    full_path: str = os.path.join(base_path, folder_name)
    os.makedirs(full_path, exist_ok=True)
    return full_path

def organize_folder(folder_path:str):

    folders_dict: dict = {}
    files_and_folders: list = os.listdir(folder_path)
    for item in files_and_folders:
        item_path: str = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            item_name, item_extension = os.path.splitext(item_path)
            if item_extension in folders_dict:
                move_files_to_folder(folders_dict[item_extension], item_extension, files_and_folders, folder_path, folders_dict)

            else:
                new_folder_path = create_folder(folder_path, item_extension)
                print(f"Create folder : name {item_extension}, at {folder_path}")
                move_files_to_folder(new_folder_path, item_extension, files_and_folders, folder_path, folders_dict)

        if os.path.isdir(item_path):
            organize_folder(item_path)


if __name__ == "__main__":
    path_folder = input("Enter Your Folder Path To Organize it : ")
    print("logs:\nprocessing...")
    organize_folder(path_folder)