1. project framework. simple introduce to our project
- E-commerce about Lego MiniFigures
- Basic functions: register, browse, buy and sell mini figures

2. create ERD; set up table relationships;

3. Create our own API; 
- scrape from Lego website;
- use beautifulsoup to scrape these data;
- save it into Json files;

4. use SQL Alchemy to build tables in database;
- import our Json files; 
- create models and class, attributes, table rows;
- build relationships and join tables;
- create queries to make HTML functional; 
  
5. HTML templates
- use jinja (make base html, blockhead, blockbody) No need to repeat the same parts in html;
- JQuery Ajax to sort data and replace html content dynamically;
- JQuery auto completion fields (Alchemy querry) - search item by substring
- make routes redirect and render templates;


Technology:
language: Python--backend API to interact with frontend, use MVC model;
HTML5, CSS, Javascript --frontend for visualizintg website
framework: flask
Database: MySQL--data store and import and validate;
 (Apply Flask build-in methods like flask-webforms, login, validators, Migrate to our project)
-scrape tool: beautifulsoup and Json file read, write;
-jquerry (AJAX, API)
-SQL Alchemy
-Apply cache to minimize latency and reduce query times;
-Docker to run all the service components and AWS Hosting to deploy the project;


Future optimize project:
use redis cache;
use CDN to store database image;
permanent session lifetime flask;
SSL to secure connections;


