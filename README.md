
This repo contains a Python/Django REST API which retrieves banks details based on user's queries.


## Deployment
This app is deployed using Render.
The link is here : https://banksapi.onrender.com

## Overview
This Api contains routes to retrieve bank details like ifsc, branch and other things based on users queries.
This Api contains three endpoints :
 - /api/get-banks/ : Lists all the banks available.
 - /api/get-branch-by-ifsc/<ifsc> : Retrieves the details of given ifsc branch
 - /api/get-branch-by-search : This endpoint accepts query parameters from users.
 - Two options are available:
   1. search - query parameter - useful when user have a vague search term not exact
   Eg : /api/get-branch-by-search?search=andhra
   2. field_name - In this option, the user can filter the branch by giving the exact field name .
   Eg : /api/get-branch-by-search?branch=KANJUR

Data is available in the form of an SQL Dump at [this repo](https://github.com/Amanskywalker/indian_banks).

## Libraries/Framworks

 - Django (ORM and Web Framework)
 - Django-rest-framework
 - Django-filters

## Approach

 - Based on the given data, it is clear that Django framework with it's batteries included approach is more 
    appropriate. It's ORM is very useful with its out of the box migrations.
 - After selecting the framework, now the models are to be created. The models are created with the apis endpoints
    in mind. For the filtering and retrieving branch details, the database view is also included as a model, so 
    that instead of retrieving the data from the database and joining it in the server, the data can be retrieved 
    directly from the view.
 - Once the models are done, it's time to create views for the API's endpoints. Since, django-rest-framework has
    some easily accessible functionality for creating RESTAPIs, it is used. The rest-framework provides serializers
    for serializing the data and class based views for retrieving the data.
 - Now, three views are required for the endpoints. Listing all the banks and retrieving using ifsc are pretty
    straight forward. The problem is searching by users requirements such as if a user knows the exact value for
    a field name or only has a vague idea.
 - For this, django-filters are available. Whenever some filter fields are provided to the view, the view can query
    the database based on these fields. The search fields however are more free to use, the user can give a search
    word and the view queries the database based on the if search word is present in the given fields or not. It works somewhat like google search.
 - Once everything is configured, now the app is ready to be deployed. Its deployed on Render because it has a free 
    tier and supports both django and postgres.

