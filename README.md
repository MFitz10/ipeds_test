Deloitte Workforce Analytics Sourcing Tool
===========================================

Data Sources
-------------

### IPEDS

The Sourcing Tool relies on data from the Integrated Postsecondary Education
Data System (IPEDS). This data is available at:

https://nces.ed.gov/ipeds/

The most recent data available at the time of the last update was 2013.
If you need to make changes or update data for subsequent years, please use
the instructions below.

The raw data may be downloaded as .csv files, and data dictionaries may be 
downloaded as .xls files. Replace the files in 
[sourcing_tool/IPEDS_Data/](sourcing_tool/IPEDS_Data/) with the new data.

To upload all of the .csv files in the [IPEDS_Data](sourcing_tool/IPEDS_Data/) 
directory to the database, run the 
[csv_import.py](sourcing_tool/csv_import.py) file.

### U.S. News & World Report

Scrape updated U.S. News & World Report rankings using the
[scrape-rankings.py](sourcing_tool/rankings/scrape_rankings.py) script. The 
results save to the [rankings.txt](sourcing_tool/rankings/rankings.txt) file 
and may be imported into the database table usnwr_rankings. Note that this will 
attempt to pull the matching IPEDS university ID, but it will make mistakes, so 
always validate those results.

### USAJobs

USAJobs data was used in conjunction with IPEDS Classification of Instructional
Programs (CIP) data to map jobs to majors. The SQL script
[create_job_cip_mappings.sql](sourcing_tool/sql/create_job_cip_mappings.sql) 
converts the raw manual crosswalk table into the tables needed for the 
Sourcing Tool.

The USAJobs data is in the sourcing_tool directory and is available at:

https://www.usajobs.gov/Content/pdfs/Jobs_By_College_Major.pdf

Django Models Setup
--------------------

This project is built with the Python web framework Django. If the structure
of the tables in the database changes, those changes must be reflected in the
models.py files.

To automatically generate a basic models.py file of all tables in the
database, use the `python manage.py inspectdb` command. To automatically read
in human-readable column names for the IPEDS tables, run the 
[datadicts.py](sourcing_tool/datadicts.py) file.

App Structure
--------------

### [sourcing_tool](sourcing_tool/)

The sourcing_tool directory is the central project directory, which includes
project-level settings in the [settings.py](sourcing_tool/settings.py) file, as 
well as the raw data and scripts. See the section above for more details about 
the data sources.

### [universities](universities/)

The universities app contains the API for the IPEDS and other university data.
This API is built with the Django Rest Framework and is helpful for
understanding the data structures used in the Sourcing Tool. It is deployed at:

http://10.118.4.223:84/sourcing_tool/universities/

### [dashboard](dashboard/)

The dashboard app is the front-end web app for the Sourcing Tool. All of the
html and static files (JavaScript, CSS, etc.) are found in this app. The
Sourcing Tool was built as a single-page web application. It is deployed at:

http://10.118.4.223:84/sourcing_tool/dashboard/

NOTE: The custom JavaScript files for the project are sourcingtool.js and
bubblechart.js. All other JavaScript files are from 3rd parties.

### admin

There is also an admin site, which currently has functionality to edit the 
school recruiting affiliations. The admin site is deployed at:

http://10.118.4.223/sourcing_tool/admin/

Project Workflow
-----------------

The Sourcing Tool code is managed using Git and Gitlab. There are two main Git
branches for the project:

- **master**: the primary development branch
- **testing**: the testing branch for the deployed version (this serves as the
  production branch until deployed on a true production server)

Developers should work in the master branch. To deploy updates on the server, 
merge the master branch into the testing branch, then push the testing branch 
upstream to the server. The project will then be automatically rebuilt by the 
Jenkins build named sourcing_tool_test_build. See the WFA_Server_Documentation 
repo for more information on Jenkins and deploying on the WFA demo server.
