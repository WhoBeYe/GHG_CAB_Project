# Collaborative Project for CSC 315 - "Sustainable Jersey"

## Project Contributors:
### Professor: Dr. DeGood
### Developers: Emmanuel Pasteur, Madison Bavosa, EJ Gasataya
### Last Updated: 4/7/23 (for submission on Phase 5a)

## Installation Guide

### Creating Database & Migrating Raw CSV Files into the database
* Prerequisites, ensure that the following packages are installed:
```
# install python pip and psycopg2 packages
sudo pacman -Syu
sudo pacman -S python-pip python-psycopg2

# install flask
pip install flask
```
This project utlizes raw CSV files converted from Excel spreadsheets that will be utilized by the Python Script.
After installing the required packages, you will need to create a new database with a specific name (CAB_database), since the scripts assume a certain database name. Enter the following commands to create a new database:
```
createdb CAB_database
```
Check that the database can be be entered into PSQL (Note: there will be no relations inside yet!)
```
psql CAB_database
\q
```
Install this repository & navigate to the scripts directory. Then run the following files:
```
python create_ev_ownership_data.py
create_ghg_data.py
create_vmt_data.py
create_zipcode_data.py
```

These files will read the CSV content stored in the data_files sub-directory and create inital table copies of them in the CAB_database database. You can then check that CAB_database contains these tables by typing the following commands:
```
psql CAB_database
\d
SELECT *
FROM <relation_name>;
```

## Link to open repository in VSCode Extension
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10765357&assignment_repo_type=AssignmentRepo)
