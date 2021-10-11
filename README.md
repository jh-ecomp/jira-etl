  
<h1 align="center">  
   <a href="#"> Jira ETL </a>  
</h1>  
  
<h3 align="center">  
    A simple lib to start scraping your jira cards  
</h3>  
  
<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/jh-ecomp/jira-etl?color=%2304D361">
  <img alt="Repository size" src="https://img.shields.io/github/repo-size/jh-ecomp/jira-etl">
  <a href="https://github.com/jh-ecomp/jira-etl/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/jh-ecomp/jira-etl">
  </a>
  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
  <a href="https://docs.atlassian.com/software/jira/docs/api/REST/8.19.1/">
    <img alt="Jira" src="https://img.shields.io/badge/Jira-API%20REST%208.12.1-0052cc">
  </a>
</p>
  
<h4 align="left">   
    Status: Under Development  
</h4>  
  
<p align="left">  
 <a href="#about">About</a> •  
 <a href="#how-it-works">How it works</a> •  
 <a href="#dependencies">Dependencies</a> •  
 <a href="#installation">Installation</a> •   
 <a href="#using">Using</a> •   
 <a href="#author">Author</a> •  
 <a href="#user-content-license">License</a>  
  
</p>  
  
## About  
  
Jira ETL is a python jira etl script to allow you to extract your issues, manipulate and store them in your data warehouse  
  
---  
  
## How it works  
  
This project is a python script that collects issues from Jira through its Rest API. Using Postgresql to store the jira data,  
I choose SQLAlchemy and Psycopg to manipulate my data warehouse.  
  
Edit the config files to your instance of Jira to start the ETL.  
This script is modular, so feel free to forget the whole database thing and build your own.  
  
### Pre-requisites  
  
Before you begin, you will need to have the following tools installed on your machine:  
[Git] (https://git-scm.com), [Python 3.6+] (https://https://www.python.org/), [PostgreSQL] (https://www.postgresql.org/).  
As a suggestion, use a modern editor like [Pycharm] (https://www.jetbrains.com/pt-br/pycharm/) or [VSCode ] (https://code.visualstudio.com/)  
  
#### Dependencies  
  
```bash  
  
# SQLAlchemy  
# Psycopg2  
# Requests  
  
```  
  
### Installation  
  
```bash  
  
# Clone this repository  
$ git clone git@github.com:jh-ecomp/jira-etl.git  
  
# Access the project folder cmd/terminal  
$ cd jira-etl  
  
# Install dependencies  
$ pip install -r requirements.txt  
  
```  
  
### Using  
##### This project is the basis for your application.  
**For hobby purposes it is necessary to change:**  
- jira.config file, inserting the parameters of your Jira instance and the Query you want to do;  
- database.config file, inserting the parameters for communication with your database;  
- jira_requests.py file, inserting your credentials for HTTPBasicAuth  
- db_connection.py file, inserting your credentials for acess the database.  
**For professional purpose more things need to be changed, like:**  
- jira.config file, inserting the parameters of your Jira instance and the Query you want to do;  
- database.config file, inserting the parameters for communication with your database;  
- change authentication mode on jira_requests.py  
- decrypt database credentials in db_connection.py  
  
```python  
  
# Import the lib  
from jiraetl import get_issues, process_issues, store_issues  
  
# Call get_issues to download a list of json with the issues as described in jira.config  
issues = get_issues()  
  
# Process the issues to carry out the necessary transformations and cleaning  
processed_issues = process_issues(issues)  
  
# Finally, store the data  
store_issues(processed_issues)  
#  
```  
  
## Author  
  
<a href="https://github.com/jh-ecomp?tab=repositories">  
 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/21336271?s=400&u=4b4ff916cafb59709adaa958f3c0f46bed35ae62&v=4" width="100px;" alt="João Henrique"/>  
 <br />  
 <sub><b>João Henrique</b></sub></a> <a href="https://github.com/jh-ecomp?tab=repositories" title="João Henrique"></a>  
 <br />  
---  
  
## License  
  
This project is under the license [MIT](./LICENSE.txt).  
  
Made by João Henrique 👋🏽 [Get in Touch!](Https://www.linkedin.com/in/joaohenriqueengcomp )