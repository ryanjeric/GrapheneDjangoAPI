# DJANGO WITH GRAPHENE API

## Introduction

> Django, the web framework for perfectionists with deadlines. It allows you to quickly prototype and build full web applications with less code.

>Last but not least, there’s Graphene and Graphene-Django, exposing a simple and powerful API for creating GraphQL servers.

>GraphQL is a query language for your API, and a server-side runtime for executing queries by using a type system you define for your data. GraphQL isn't tied to any specific database or storage engine and is instead backed by your existing code and data.








## Workspace Setup 
#### In the terminal, create a new virtual environment and activate it
```
$ virtualenv env
$ . env/bin/activate
 ```

#### With the virtual environment activated, run the following commands:
``` 
$ pip install -r requirements.txt
```
#### Run migrate 
```
 $ python manage.py makemigrations
 $ python manage.py migrate
```
#### After that you can now run the Server using this command
```
$ python manage.py runserver *youcanspecifyporthere
```

### Some [manage.py] commands (```$ python manage.py```)
| Command | Usage |
| ------ | ------ |
| makemigrations | Prepare the changes on models.py (models.py is your Table Structure) |
| migrate | Migrate all the changes made on models.py |
| createsuperuser | Create a SuperUser on UserTable |
| startapp *yourappname | Create new app/module  |
| - add here - | - add here-|


## INSOMNIA (Works like postman) 
>Download Insomnia here : https://insomnia.rest/

>export the GRAPHENE-API_YYYY-MM-DD.json on Insomnia to view the all Sample GRAPHQL API 


## GENERATING OF API STATIC Documentation 
```
npm install -g graphql-docs
graphql-docs-gen http://localhost:8000/api/ documentation.html
```





## SRC LINKS


>Django + Graphene
https://www.howtographql.com/graphql-python/0-introduction/

>Django Tutorials
https://www.youtube.com/watch?v=UmljXZIypDc , https://www.youtube.com/watch?v=qgGIqRFvFFk&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK
