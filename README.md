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

3. Copy the uploaded assignment file **logs_analysis_app.py** and paste it into the **news** folder (created in step 2)

4. Connect to the **news** database and execute the scripts below to create 2 new views: **articles_ranking** and **total_view_by_date**.
  

   ```sql
   create view articles_ranking as 
   (select path, count(*) as view_count 
   from log where path like '/article/%' 
   group by path 
   order by view_count desc);
   ```


   ```sql
   create view total_view_by_date 
   as (select date(time), count(*) as total_view_count 
   from log group by date(time));
   ```
   The view **article_ranking** is required by Q1 and Q2, while **total_view_by_date** is prerequisite for Q3.

## Running the Tests

In **/vagrant/news**, execute the following command line:

   ```
   python logs_analysis_app.py
   ```
  
Once executed, the log analysis results should be displayed as plain text. 

Please check __output.txt__ for the expected output.

## Program Design

The *main* function consists of three composing function calls. 

In each function composition, the *get* functions consist of code using psycopg2 (a PostgreSQL adapter) to connect to the database and return the query results.

The *display* function takes in the *get* function's output (a list of tuples) as argument, and iterates through the list and displays each item as a formatted string.

### Outline of the functions

| *display* functions | *get* functions |
| ------------- | ------------- |
| display_popular_articles  |  get_popular_articles  |
| display_popular_authors  |  get_popular_authors  |
| display_severe_errors_dates | get_date_of_error_gt_1 |

## Authors

* **Suting Chen** 


