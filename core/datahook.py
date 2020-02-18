import yaml

class yamlhook:
    def __init__(self,filename):
        self.filename = filename
    
    def open(self,method="load"):
        with open(self.filename,'r',encoding="utf8") as f:
            # load : 讀取
            if method == "load":
                return yaml.safe_load(f)

