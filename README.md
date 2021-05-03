# GoogleCloud_FLASKAPI_surveyUserRating
The objective is to create api using Flask and to connect with google cloud MYSQL instance while deploying the app on gcloud.

##### Table Of Contents:

* 1.Introduction
* 2.Description about local flask api
    - 2.1 Setup Environment for local Flask api
    - 2.2 Outcome for local flask api 
* 3.Description about cloud flask api
    - 3.1.Setup Environment for cloud Flask api
    - 3.2 Outcome for cloud flask api
* 4.Technologies Used
* 5.Future Proposal
* 6.References


* 1.Introduction

    * The technical Challenge's first part: 

        * This repository provides information about two api's: 
            - Firstly, "local_main.py" 
            - Secondly, combnination of "main.py", "db.py", "app.yaml" & "requirements.txt" 
        * Both the api allow to post the results of a customer satisfaction survey. The request should contain the following:
             -	Channel (string) {website, app}
             -	Rating (int) {1,2,3,4,5}
             
    * The technical Challenge's second part: 
        * The combnination of ("main.py", "db.py", "app.yaml" & "requirements.txt") in the same root directory is used to intiate the instance where an api interacts with google app cloud engine and SQL instance to view data and add data to cloud database. This helps us to protect data which can be lost in local api while refreshing server.
        
    * The technical Challenge's third part: (not been completed)
        * This part of challenge has not been completed as the cloud based api generated serve errors while allocating request.
        * So, I discuss the process of performing visulaisation which can be implemented after the internal server errors have been handled.
         
    * The technical Challenge's fourth part:
        * This provides an API payload so that data can be submitted to the API(both local & cloud) so that the results can be obsereved on the dashboard later on. Postman is used to invoke the API endpoints.
        
    * This repository aslo provides a pdf document sharing the architectural diagram.


* 2.Description about local flask api

    - 2.1 Setup Environment for local Flask api
    
         * The python script file named local_main.py lists the methods and necessary py script to run the Flask app
         * The script provides methods: 
             * survey(), for GET request 
             * addValue_survey() for POST request
         * The script also handles the error that can occur while entring values for  the keys "Channel" or "Rating"
         * The script should be executed after installing all the dependencies in terms of libraries have been installed.
         
    - 2.2 Outcome for local flask api 
     
         * The outcome of this local app is an endpoint in the format http web link. This can be used with Postman to invoke endpoint and initiate GET or POST request to fetch or add data respectively in json format.
         
* 3.Description about cloud flask api

    - 3.1.Setup Environment for cloud Flask api
    
        * This is a combiantion of files named "main.py", "db.py", "app.yaml" & "requirements.txt" that lists the methods necessary to run the Flask app and connect to google cloud MYSQL instance.
        * After initiating the google cloud instance create table survey_report within user defined database.
        * All the files should be within same directory while deploying app on gcloud.
        * Open the py terminal and within any directory execute command "./google-cloud-sdk/install.sh" to install google cloud sdk.
        * Followed by this ./google-cloud-sdk/bin/gcloud init to initialise the google cloud sdk
        * Now change directory to the root folder containing all the previous files and execute "gcloud app deploy"
        * In my case, errors were experience in terms of internal server error while running the app.
        * The script main.py provides methods: 
             * get_rating(), for GET request 
             * add_rating() for POST request
        * The script db.py provides methods: 
             * open_conn() for google cloud MYSQL instance connection
             * get_rating(), for SELECT statements for query
             * add_rating() for INSERT INTO () VALUES() statements
        * The script doesnot handles the error that can occur while entring values for  the keys "Channel" or "Rating" as the table constraints can be laid out within google cloud SQL database table from cloud console. Moreover, the internal server errors have also not been handled.
        * The script should be executed after installing all the dependencies in terms of libraries from the requirement.txt.
        * The takes reference from app.yaml file for initiating the variables for cloud requisites.
         
    - 3.2 Outcome for cloud flask api
    
        * The outcome of this local app is an endpoint in the format http web link. This can be used with Postman to invoke endpoint and initiate GET or POST request to fetch or add data respectively in json format. There is a server error due to which we cannot use GET or POST.
        
* 4.Technologies Used
    * Python 3.8
    * Jupyter Notebook
    * Google Cloud SQL
    * Google Cloud SDK
    * Python bash terminal
    
* 5.Future Proposal
    * Since due to internal server error after the app deployment, we cannot use GET AND POST to interact with the server. The proposal is to handle the error.
    * Suggestion is to follow the process of web data connectors for using the server outcome and visualising it within Tableau Dashboard.
      
* 6.References
    * Oyekanmi.W,2020,'Setting Up An API Using Flask, Google’s Cloud SQL And App Engine'. Retrieved from "https://www.smashingmagazine.com/2020/08/api-flask-google-cloudsql-app-engine/" 
    
    * Google Cloud,n.d.,'Quickstart: Getting started with Cloud SDK'. Retrieved from "https://cloud.google.com/sdk/docs/quickstart"
