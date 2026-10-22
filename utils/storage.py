import json
import os


class StorageManager:

    def __init__(self, data_folder="data"):
        self.data_folder = data_folder

        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

    def get_file_path(self, name):
        return self.data_folder + "/" + name + ".json"

    def load(self, name):
        path = self.get_file_path(name)

        # If the file does not exist yet, create an empty one
        if not os.path.exists(path):
            self.save(name, [])
            return []

        # If the file is damaged, start with an empty list instead of crashing
        try:
            with open(path, "r") as file:
                records = json.load(file)
        except json.JSONDecodeError:
            print("Warning: " + path + " is damaged. Starting with an empty list.")
            return []
        return records

    def save(self, name, records):
        path = self.get_file_path(name)

        with open(path, "w") as file:
            json.dump(records, file, indent=4)