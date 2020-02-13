import yaml

class yamlhook:
    def __init__(self,filename):
        self.filename = filename
    
    def open(self):
        with open(self.filename,'r',encoding="utf8") as f:
            return yaml.safe_load(f)