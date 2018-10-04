# website_blocker
## Simple python script that accesses the hosts file and redirects website addresses to the localhost
### The script is designed to run in the background at start up. Use [Cron](http://www.jessicayung.com/automate-running-a-script-using-crontab/) to automate the script.
### To block the desired websites, modify the following code
```
website_list = ["www.facebook.com","facebook.com"]
```
### The script activates between the hours of 8 a.m and 5 p.m , change numbers to modify.
```
if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
```



