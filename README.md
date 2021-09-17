
# Jira ETL

<h4 align="left"> 
	 Status: Under Development
</h4>

<p align="left">
 <a href="#about">About</a> •
 <a href="#how-it-works">How it works</a> •
 <a href="#dependencies">Dependencies</a> •
 <a href="#installation-and-using">Installation and Using</a> • 
 <a href="#author">Author</a> •
 <a href="#user-content-license">License</a>

</p>

## About

Jira ETL is a python jira etl script to allow you to extract your issues, manipulate and store them in your data warehouse

---

## How it works

This project is a python script that collects issues from Jira through its Rest API.

Edit the config files to your instance of Jira and create you db connection to start the ETL.

### Pre-requisites

Before you begin, you will need to have the following tools installed on your machine:
[Git] (https://git-scm.com), [Python 3.6+] (https://https://www.python.org/).
As a suggestion, use a modern editor like [Pycharm] (https://www.jetbrains.com/pt-br/pycharm/) or [VSCode ] (https://code.visualstudio.com/)

#### Dependencies

```bash

# SQLAlchemy
$ pip install SQLAlchemy

# Requests
$ pip install requests

```

### Installation and Using

```bash

# Clone this repository
$ git clone git@github.com:jh-ecomp/jira-etl.git

# Access the project folder cmd/terminal
$ cd jira-etl

# Run the application
$ python main.py

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
