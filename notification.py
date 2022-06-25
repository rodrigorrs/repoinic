import datetime
import time
import requests
from plyer import notification

covidData = None

try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/india")
except:
    # se os dados não forem buscados devido à falta de internet
    print("Checar conexao com a internet")



if (covidData != None):
    data = covidData.json()['Success']

    while (True):
        notification.notify(
            title = "COVID19 Stats on {}".format(datetime.date.today()),
            message = "Total cases : {totalcases}\nToday cases : {todaycases}\nToday deaths :{todaydeaths}\nTotal active :{active}".format(
                        totalcases = data['cases'],
                        todaycases = data['todayCases'],
                        todaydeaths = data['todayDeaths'],
                        active = data["active"]),


            #creating icon for the notification
            #we need to download a icon of ico file format
            # the notification stays for 50sec
            timeout  = 50
        )

        time.sleep(60*60*4)