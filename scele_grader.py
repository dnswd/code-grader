from csv import reader, writer 
from os import remove
from pathlib import Path
from subprocess import getstatusoutput
from zipfile import ZipFile
import sys

# TODO: Modularity

# config
config = {
    "asdos_code": "DNS",
    "asdosee_data": "DNS.csv",       # csv path relative to file
    "lab": "0",
    "tasks": ["nama", "lovemeter"]
}

cwd = Path.cwd() / sys.argv[0]

class Asdosee:
    def __init__(self, data):
        self.npm = data[0]
        self.nama = data[1]
        self.email = data[2]
        self.asisten = data[3]
        self.tasks = []
        
# TASK CLASS

def fetch_asdosee(asdosee_data):
    asdosees = []
    with open(config[asdosee_data], 'r') as file_:
        data = reader(file_)
        for row in data:
            asdosee = Asdosee(row)
            asdosees.append(asdosee)
    return asdosees
        
def fetch_subs(lab):
    extensions = ('**/*.zip', '**/*.rar')
    if not (submission_path := cwd / lab / "submission").exists():
        raise Exception("submission folder doesn't exist")
    else:
        subs = []
        for extension in extensions:
            subs.extend([files for files in submission_path.glob(extension)])
        filtered = filter(lambda sub: config["asdos_code"] in sub, subs)
        return list(filtered)
    
if __name__ == "__main__":
    print("UNDER CONSTRUCTION")
    asdosee = fetch_asdosee(config["asdosee_data"])
    subs = fetch_subs(config["lab"])
    
    # TODO
    for sub in subs:
        with ZipFile(sub, "r") as unzip:
            for task in unzip.namelist():
                # wait using count (ghetto lmao)
                getstatusoutput('code -r ' + task).count(0)
