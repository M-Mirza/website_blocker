#Muhammad Mirza
import time
from datetime import datetime as dt
hosts_path = "/private/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        # checks if the current time is within working hours or not
        print("Working Hours...")
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + "    " + website + "\n")
        # if within working hours, program writes domain name and redirect ip to hosts file
    else:
        with open(hosts_path,'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Regular Hours...")
        # if not within working hours, the program will delete the lines that redirect the domain names within hosts file
    time.sleep(5)
