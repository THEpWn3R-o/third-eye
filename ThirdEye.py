import subprocess
import time
import os 
import random

colors = ['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W = '\033[0m'

try:
    import shodan
    import requests
except ImportError:
    print("Dependancies not found, this script will not work without them.")
    ch1 = input("should I install for you? (y/n)-> ").lower()
    if ch1 == "y":
        subprocess.call("pip3 install -r requirements.txt", shell=True)
    else:
        print("Okay, Install It before running this script again!")
        exit()

try:
    country = ""
    state = ""
    output = ""
    subprocess.call('clear',shell=True)
    def WritePrevDetails():
        with open ("details.txt", "w") as f:
            f.write(f"{Prev_Api},{Prev_Name}")
    
    if os.path.isfile("details.txt"):
        with open("details.txt", "r") as f:
            d = f.read().split(",")
            Prev_Api = d[0]
            Prev_Name = d[1]
    else:
        Prev_Api = ""
        Prev_name = ""
   
    def LegalNotice():
        print("\033[1;31;40m                       ***WARNING***")
        print( "This tool is strictly used for pentesting and fun. It in no situatuon should be used in for illegal intent.")
        print("I can not be responsable for your actions using this tool.")
        print("there is a bug here where it stains everything red until you rerun the script. Im not sure why. If you do feel to reach out.")
        ch2 = input("Do you agree with these terms? (y/n)-> ").lower()
        if ch2 == "y":
            subprocess.call("clear", shell=True)
            print("Good, continue with the tool setup and have a good day!")
            time.sleep(0.5)
        else:
            print("That's a shame. Come back when you agree.")
            exit()

    if not os.path.isfile("details.txt"):
        LegalNotice()
        Prev_Api = input("What's your shodan Api key? -> ")
        Prev_Name = input("Sorry, Last question for setup. What should I call you? -> ")
        WritePrevDetails()
    else:
        print("Checking for updates and such :p....")
        subprocess.call('git pull https://github.com/THEpWn3R-o/third-eye.git',shell=True)
        time.sleep(2)
        subprocess.call('clear',shell=True)


    SHODAN_API_KEY = Prev_Api
    NAME = Prev_Name
    
    api = shodan.Shodan(SHODAN_API_KEY)


    print(f"""
|------------------------------------------|
|                    |                     |
|  setup complete    |    Welcome back,    |
|                    |       {NAME}       |
|------------------------------------------|""")
    time.sleep(1)
    print("Only support for webcams right now. Laptop & phone camreas comming soon.")
    print("Currently supporting, SQ-WEBCAM")
    query = input(random.choice(colors) + f"what are we looking at today {NAME.lower()}: " + W).lower()
    subprocess.call('clear',shell=True)
    country = input(random.choice(colors) + "What country? -> " + W)
    subprocess.call('clear',shell=True)
    state = input(random.choice(colors) + "What state? -> " + W)
    subprocess.call('clear',shell=True)
    print("I dont recomend over 6.")
    MaxNumb = input(random.choice(colors) + "What is the max ips you want? -> " + W)
    if query == "sq-webcam":
        output = api.search(f"Server: SQ-WEBCAM country:{country} state:{state}")
        for service in output['matches']:
            ips = []
            service['ip_str'].append(ips)
            ips.split([5])
    
except KeyboardInterrupt:
    subprocess.call('clear',shell=True)
    print("ctrl+c detected... Exiting...")
    time.sleep(2)

except shodan.exception.APIError:
            subprocess.call('clear',shell=True)
            print(random.choice(colors) + "Api error, You have to upgrade your api to use filters :(" + W)

