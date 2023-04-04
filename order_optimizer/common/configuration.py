import json


class Configuration:
    def __init__(self, config_path=None):
        self.config_path = config_path
        self.config = {}

    def get_config(self):
        if self.config_path:
            self.config = json.load(self.config_path)
        return self.config
