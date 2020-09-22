from csv import reader, writer 
from os import remove
from pathlib import Path
from subprocess import getstatusoutput
from zipfile import ZipFile
import sys

# TODO: Modularity

# config
# TODO(Dennis): runtime config? or file based config?
config = {
    "asdos_code": "DNS",
    "asdosee_data": "DNS.csv",                              # csv path relative to file
    "tasks": ["nama", "lovemeter"]
}

cwd = Path.cwd() / sys.argv[0]
asdosees = []

class Asdosee:
    def __init__(self, data):
        self.npm = data[0]
        self.nama = data[1]
        self.email = data[2]
        self.asisten = data[3]
        self.tasks = []
        
# TASK CLASS

def fetch_asdosee(asdosee_data):
    with open(config["asdosee_data"], 'r') as file_:
        data = reader(file_)
        for row in data:
            asdosee = Asdosee(row)
            asdosees.append(asdosee)
        
def fetch_subs():
    extensions = ('**/*.zip', '**/*.rar')
    if not (submission_path := cwd / "submission").exists():
        raise Exception("submission folder doesn't exist")
    else:
        
        subs = []
        for extension in extensions:
            subs.extend(list(submission_path.glob(extension)))
        filtered = filter(lambda sub: config["asdos_code"] in sub, subs)
        return list(filtered)
    
if __name__ == "__main__":
    print("UNDER CONSTRUCTION")