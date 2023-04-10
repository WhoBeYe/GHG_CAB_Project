# Collaborative Project for CSC 315 - "Sustainable Jersey"

## Project Contributors:
### Professor: Dr. DeGood
### Developers: Emmanuel Pasteur, Madison Bavosa, EJ Gasataya
### Last Updated: 4/9/23 (for submission on Phase 5a)

## Installation Guide

### Creating Database & Migrating Raw CSV Files into the database
* Prerequisites, ensure that the following packages are installed:
```
# install python pip and psycopg2 packages
sudo pacman -Syu
sudo pacman -S python-pip python-psycopg2

# install flask
pip install flask
# "pip3" for some
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
Install this repository & navigate to the "scripts" directory. Then run the following files:
```
python create_ev_ownership_data.py
python create_ghg_data.py
python create_vmt_data.py
python create_zipcode_data.py
```

These files will read the CSV content stored in the data_files sub-directory and create initial table copies of them in the CAB_database database. You can then check that CAB_database contains these tables by typing the following commands:
```
psql CAB_database
\d
SELECT *
FROM <relation_name>;
```
### Execution of DDL (Data Definition Language) and DML (Data Manipulation Language) Scripts
The DDL scripts are of .sql extension. After creating tables containing the CSV elements, the following scripts will create more tables pertaining to this data (Specified in Phase IV)

```
# Be sure to enter the database if not done already
psql CAB_database
\i contains_DDL_script.sql;
\i mun_DDL_script.sql;
\i vehicle_DDL_script.sql;
```

The following DML script contains some example queries we propose to utilize in the web application in Phase 5b. Execution of this file is similar to the scripts above:

```
# Be sure to enter the database if not done already
psql CAB_database
\i example_DML_script.sql;
```
* Note, if the terminal window is small, you won't be able to see all the queries at once. To move down the terminal window, press the "q" button.

### Dropping Tables Script
To make our testing easier when making these tables, if any mistakes were found in our tables, we can simply run a script where all tables made in the DDL will be dropped. We can then run the same scripts above to reload the tables.

```
# Be sure to enter the database if not done already
psql CAB_database
\i drop_tables.sql
```

## Link to open repository in VSCode Extension
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10765357&assignment_repo_type=AssignmentRepo)
