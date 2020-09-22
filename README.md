# SCeLE Grader
Simple tool to review and grade codes efficiently using Python.

## TODO:
- [ ] Implement mosspy

Usage: `python scele_grader.py [assignment name]`  
Example: `python scele_grader.py Lab0`

Requirements:
1. Asdosee data in CSV contains
    - SCeLE Name
    - NPM
    - Class
    - Asdos  

    Example row:
    ```
    Lorem Ipsum - 69696969,69696969,Kelac C,DNS - Dennis Walangadi
    ```
2. Submission folder, contains submissions inside archive data type (`rar`/`zip`).

Folder structure:
```
.
|   dns.csv
|   scele_grader.py
|   
\---Lab0
    \---submission
            [SCeLE Name]_[user_id]_assignsubmission_[filetype]_[NPM]_[Asdosee Name]_[Asdos Code]_[Class]_[task].zip
            Adimas Putra - 6969696969 Adimas_098765_assignsubmission_file_6969696969_AdimasPutra_XYZ_A_lab0.zip
            Louise Wicaksono - 123456789 Lowi_420069_assignsubmission_file_123456789_LouiseWicaksono_ABC_A_lab0.zip
            ...
            
```