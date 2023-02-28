import sys
import os
import subprocess
import shutil
import json

# this tool syncs the orginal audio and filter audio returned time offset.
git_link = "https://github.com/dsholes/python-warpdrive.git"

def getSyncsTool():
    if not os.path.exists("python-warpdrive"):
        print("Cloning python-warpdrive")
        clone = subprocess.Popen(["git", "clone", git_link], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        clone.wait()
        if clone.returncode != 0:
            print("Error occured while cloning python-warpdrive")
            print("Please check your internet connection and try again")
            print("Check if you have git installed")
            print("If you have git installed, try to clone the repo manually")
            print(git_link)
            sys.exit()
        else:
            print("python-warpdrive cloned successfully")

def create_folder(file_path, new_folder):
    if not os.path.isfile(file_path):
        raise ValueError("Need a file path, not a directory path.") # Keep it simple
    directory_path = os.path.dirname(file_path)
    new_folder_path = os.path.join(directory_path, new_folder)
    os.makedirs(new_folder_path, exist_ok=True)
    return new_folder_path

def mv_files(destination_path, *file_paths):
    if not os.path.isdir(destination_path):
        raise ValueError("No folder found at the destination path.")

    for file_path in file_paths:
        if not os.path.isfile(file_path):
            raise ValueError("mv_files() only works with files this exists.")
        
        # Moves the file to the destination path
        file_name = os.path.basename(file_path)
        new_file_path = os.path.join(destination_path, file_name)
        shutil.move(file_path, new_file_path)

def runSycTool(folder_path):
    command = [
        "python",
        "python-warpdrive/warpdrive.py",
        folder_path
    ]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f'Error: {stderr.decode()}')
        print("Please check just the tool Standalone")
        print("This tool was ckecked on version 9919f0c from Oct 13, 2019")
        print("Check if you have all packages installed")
        return False
    else:
        print(f'Success: {stdout.decode()}')
        return True , None


def extract_values_from_json(file_path, key_list):
    if not os.path.isfile(file_path):
        raise ValueError("Need a file path, not a directory path.")
    with open(file_path, "r") as json_file:
        json_data = json_file.read()
        json_obj = json.loads(json_data)
        values = []
        for key, obj in json_obj.items():
            item_values = {}
            print(key)
            for key in key_list:
                if key in obj:
                    item_values[key] = obj[key]
            values.append(item_values)
        return values

key_list = ["path", "tshift_from_base_sec", "dur_sec"]
#file_path = "D:/AudioKI/python-warpdrive/audiotest/_warpdrive_results/_warpdrive_audiotest.json"
#values = extract_values_from_json(file_path, key_list)
#print(values[0]["tshift_from_base_sec"])

def find_index_of_zero_tshift(values):
    for i, item in enumerate(values):
        if item.get("tshift_from_base_sec", None) == 0.0:
            return i
    return None

def find_index_of_shift(values):
    for i, item in enumerate(values):
        if item.get("tshift_from_base_sec", None) != 0.0:
            return i
    return None

