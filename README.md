# Logs Analysis App

Logs Analysis App is a reporting tool that prints out reports (in plain text) based on the data in the news database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Follow the instructions from this [link](https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0 "VM Setup Instructions") to set up the virtual machine.


### Installing

1. Import news data to the local database. 
Instruction notes can be found [here](https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91 "Prepare the data")

2. Create a directory folder **news** under __/vagrant__

3. Copy the uploaded assignment file **log_analysis_app.py** and paste it into the **news** folder (created in step 2)

4. Connect to the **news** database and execute the script below to create a new view, **articles_ranking**. This view is required by the first two log analysis sql query statement
  

   ```sql
   create view articles_ranking as 
   (select path, count(*) as view_count 
   from log where path like '/article/%' 
   group by path 
   order by view_count desc);
   ```

## Running the tests

In **/vagrant/news**, execute the following command line:

   ```
   python log_analysis_app.py
   ```
  
Once executed, the log analysis results should be displayed as plain text below:
   ```
   [Logs Analysis]

   The most popular three articles of all time:
   1. "Candidate is jerk, alleges rival" - 338,647 views
   2. "Bears love berries, alleges bear" - 253,801 views
   3. "Bad things gone, say good people" - 170,098 views


   The most popular article authors of all time:
   1. Ursula La Multa - 507,594 views
   2. Rudolf von Treppenwitz - 423,457 views
   3. Anonymous Contributor - 170,098 views
   4. Markoff Chaney - 84,557 views

   Dates having more than 1% of requests lead to errors:
   1. July 17, 2016 - 2.26% errors
   ```

## Authors

* **Suting Chen** 


