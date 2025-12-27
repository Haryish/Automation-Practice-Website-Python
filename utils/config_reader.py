import os
import configparser

class ConfigReader:
    config_path = './config/config.ini'  # Default path to config file  
    
    def __init__(self, env='default'):
        # Expand user tilde (~) if present
        self.config_path = os.path.expanduser(self.config_path)
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)
        self.env = env

    def get(self, key):
        # First check if the environment-specific section exists
        if self.env in self.config and key in self.config[self.env]:
            return self.config[self.env][key]
        # Fallback to default section
        elif 'default' in self.config and key in self.config['default']:
            return self.config['default'][key]
        else:
            raise KeyError(f"Key '{key}' not found in config for environment '{self.env}' or 'default'.")
        
    
    
    