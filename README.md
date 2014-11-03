# Galileo #

Project for mapping the network using [NMAP](http://nmap.org/).

## Warnings ##

Use pexpect version 3.2 or 3.1. **Otherwise exception occurs - [pexpect](http://stackoverflow.com/questions/24524162/pexpect-runs-failed-when-use-multiprocessing).**


## Usage ##

Connect to the network you want to scan (directly, VPN, ...).
**Use NMAP to scan the network and export the data to XML.**

NMAP scan example that will scan all the computer in 10.168.2.* range, outputting the results to file 'iii_network.xml'


```
#!bash

nmap -v -T5 10.168.2.* -oX iii_network.xml
```


Finally, upload the XML to Galileo. Galileo will use the data to generate the required DB data, allowing the users to check the network data anytime. The problem could be the data staleness.

![post usage.png](https://bitbucket.org/repo/dn7B4B/images/3917744280-post%20usage.png)




## Check this out ##

* [SQLalchemy pattern](http://flask.pocoo.org/docs/0.10/patterns/sqlalchemy/)

> "pip freeze > requirements.txt"
> "pip install -r requirements.txt"

> [JSON extraction](http://stackoverflow.com/questions/22012655/restangular-getlist-with-object-containing-embedded-array)

* https://github.com/mgonto/restangular
* SVN default port **3690**

## Project structure ##

Project/
|-- bin/
|   |-- project
|
|-- project/
|   |-- test/
|   |   |-- __init__.py
|   |   |-- test_main.py
|   |   
|   |-- __init__.py
|   |-- main.py
|
|-- setup.py
|-- README

> [Used for angular project](https://github.com/yeoman/generator-angular)
> [Used for flask project structure](https://github.com/mitsuhiko/flask/wiki/Large-app-how-to)
> [Flask project structure](https://github.com/mitsuhiko/flask/wiki/Large-app-how-to)

