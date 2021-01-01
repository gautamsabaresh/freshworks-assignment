# This is a sample Python script.

# Press Shift+F1    0 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import os
from threading import Timer
import threading

d = {}
datastore_dir_path = os.path.dirname(os.path.realpath(__file__))+"\\datastore.json"


def empty_json_file():
    temp = {}
    with open(datastore_dir_path, 'r+') as json_file:
        json.dump(temp, json_file, indent=4, sort_keys=True)


def create(key, value, timeout=0):
    if os.path.exists(datastore_dir_path):
        with open(datastore_dir_path, 'r+') as json_file:
            file_content = json_file.read()
    else:
        with open(datastore_dir_path, 'w+') as json_file:
            file_content = json_file.read()
    if len(file_content) == 0:
        empty_json_file()
    with open(datastore_dir_path, 'r+') as file:
        file_data = json.load(file)
    if key in file_data:
        print("error: This key already exists")
        return False  # error message1
    else:
        if key.isalpha() and type(value) == dict:
            if len(file_data) < (1024 * 1024 * 1024) and len(value) <= (
                    16 * 1024 * 1024):  # constraints for file size less than 1GB and json object value less than 16KB
                if timeout != 0:
                    if timeout < 0:
                        print("The time should not be given in negative integer.")
                        return False
                    t = Timer(timeout, delete, [key])
                    t.start()
                if len(key) <= 32:  # constraints for input key_name capped at 32chars
                    d[key] = value
                    with open(datastore_dir_path, 'r+') as json_file:
                        data = json.load(json_file)
                        data.update(d)
                        json_file.seek(0)
                        json.dump(data, json_file, indent=4, sort_keys=True)
            else:
                print("error: Memory limit exceeded!! ")
                return False
        else:
            if type(value) != dict:
                print("error: The value should be a json object with key-value pair")
                return False
            else:
                print(
                    "error: Invalid key name. Key name must only have alphabets and no special characters or numbers")
                return False


def read(userkey):
    with open(datastore_dir_path, 'r+') as json_file:
        file_data = json.load(json_file)
        if userkey in file_data:
            return file_data[userkey]
        else:
            return "Error: given key is not in the data store"


def delete(userkey):
    with open(datastore_dir_path, 'r+') as json_file:
        file_data = json.load(json_file)
        if userkey in file_data:
            del file_data[userkey]
            with open(datastore_dir_path, 'w') as json_file:
                json.dump(file_data, json_file, indent=4, sort_keys=True)
            return True
        else:
            print("Error: given key is not in the data store")
            return False

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
