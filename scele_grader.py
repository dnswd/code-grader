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
    "asdosee_data": "dns.csv",                              # csv path relative to file
}

cwd = Path.cwd() / sys.argv[0]
asdosee = {}

# fetch asdosee data
# TODO(Dennis): Store asdosee data efficiently (dictionary? it's JSON-like)
with open(config["asdosee_data"], 'r') as file_:
    data = reader(file_)
    for row in data:
        row.append(dict())      # why
        asdosee[row[1]] = row
        
# fetch submissions
if not (submission_path := cwd / "submission").exists():
    raise Exception("submission folder doesn't exist")
else:
    submissions = list(submission_path.glob("**/*.zip"))
    print(submissions)
    
for submission in submissions:
    # filter based on asdosee
    if config["asdos_code"] in (file_name := submission.name.split('_')[-3]):
        with ZipFile(submission, "r") as s:
            print("### Now grading", file_name[-4], file_name[-5], "###")
            for task in s.namelist():
                # most ghetto way to wait
                # opens file in vscode, 
                if can_open := getstatusoutput('code -r ' + task).count(0):
                    print("=>", task)
                    
                    # check plagiarism here
                    
                    # grading components
                    # TODO: Make this modular (config perhaps?)
                    functionality = float(input("fungsionalitas (45 max): "))
                    error = 0 if input("apakah error (y/n) (10 points): ") == "y" else 10
                    validate = float(input("apakah ada validasi input? (5 max): "))
                    pep8 = float(input("apakah kode rapi/sesuai PEP8? (10 max): "))
                    doc = float(input("comments/documentation coverage (10 max): "))
                    efficiency = float(input("kode efisien (10 max): "))
                    
                    grade = functionality + error + validate + pep8 + doc + efficiency
                    asdosee[file_name[4]][-1][task] = grade # this is terrible
                    print(6)
                else:
                    print("Error: can't open", file_name[-4], task)
    else:
        # removing submission from someone else's asdosee
        remove(submission)

# TODO(Dennis): Output data
report_name = cwd.name + "_grade.csv"
with open(report_name, 'w+') as report:
    report_writer = writer(report)
    report_writer.writerow("test")
