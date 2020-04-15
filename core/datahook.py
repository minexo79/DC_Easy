import yaml

# --------------------
# yd : yaml data
# 資料勾手
# --------------------

class yamlhook:
    def __init__(self,filename):
        self.filename = filename

    # load : 純讀取

    def load(self):    
        with open(self.filename,'r',encoding="utf8") as yd:
            return yaml.safe_load(yd)

    def owner(self,did:int,process=""):
        with open(self.filename,'r',encoding="utf8") as yd:
            data = yaml.safe_load(yd)

        # append: 增加
        # remove: 移除

        if process == "append":
            data['bot']['owner'].append(did)

        elif process == "remove":
            data['bot']['owner'].remove(did)

        with open(self.filename,'w',encoding="utf8") as yd:
            yaml.safe_dump(data,yd)