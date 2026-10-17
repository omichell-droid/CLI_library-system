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

        if not os.path.exists(path):
            self.save(name, [])
            return []

        with open(path, "r") as file:
            records = json.load(file)
        return records

    def save(self, name, records):
        path = self.get_file_path(name)

        with open(path, "w") as file:
            json.dump(records, file, indent=4)