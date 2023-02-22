# **flask_hillel**
_This is a trial flask app._
_It consists of 9 pages:_
* Main ( with links to other pages)
* Requirements 
* Generate_users ( shows names and emails of generated users)
* Mean value ( shows mean height and weight values from csv file)
* Space info (shows a number of astronauts from http://api.open-notify.org/astros.json)
* Unique names of artists (from database)
* All tracks in database
* Tracks length (in sec)
* Tracks statistics (the average lenght and sum of length (in sec))

_To run the app:_
* Clone the repo
* Install requirements
* To initialize the database file run the command:
``` flask --app flaskr init-db```
* there will be a flaskr.sqlite file in the instance folder in project with two tables.
* To fill the database tables with data run the command:
``` flask --app flaskr fill-db```
* Use command:
```flask --app flaskr  run```
* or:
``` flask --app flaskr run --debug``` (in case you want to use a debug mode)
