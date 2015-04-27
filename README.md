#DEPLOY ON HEROKU


```
git clone https://github.com/orymeyer/Logging-Server-Heroku.git
heroku create
cd <app_name>
git add --all
git commit -m "Init"
git push heroku master
```

To log data,POST data to the url <app-name>.herokuapp.com/log
The raw data gets logged walong with the timeStamp.
