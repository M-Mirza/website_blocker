# website_blocker
## Simple python script that denies website access by redirecting website addresses to the localhost within the hosts file
### The script is designed to run in the background at start up. Use [Cron](http://www.jessicayung.com/automate-running-a-script-using-crontab/) to automate the script.
### To block the desired websites, modify the following code
```
website_list = ["www.facebook.com","facebook.com"]
```
### The script activates between the hours of 8 a.m and 5 p.m , change numbers to modify.
```
if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
```

#### Program Architecture 
Script accesses hosts file , checks what time it is every five seconds to see if it is within the working hours or not. If it is within working hours , the script writes to the hosts file the redirect address and the domain name which denies access to the websites. If it is not within working hours the script will check if the hosts file contains the domain name and redirect address, if it does it will delete the lines to allow website access. 



