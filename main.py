import requests
import smtplib
api_url='http://api.weatherapi.com/v1/forecast.json'
parameters={
    'q':'New Delhi',
    'days':2,
    'aqi':'no',
    'alerts':'no',
    'key':'7fd781eff0484726a52190624221307'
}
recipent=['akhilpanwar989@gmail.com','panwarakhil033@gmail.com','panwarr@appstate.edu','dollypanwar07@gmail.com','panshul54@gmail.com','gauravchoudhary18791@gmail.com']
response=requests.get(url=api_url,params=parameters)
response.raise_for_status()
data=response.json()
message=""
weather_slice=data["forecast"]["forecastday"][0]["hour"][:12]
day=data["forecast"]["forecastday"][0]["date"]
max_temp=data["forecast"]["forecastday"][0]["day"]["maxtemp_c"]
for hour in weather_slice:
    if hour["will_it_rain"]==1:
        message=f"rain will probably occur in next 12 hours on date{day},please bring an umberalla.Today maximum temperature will be{max_temp}c"
        break
    else:
        message="toady probability of raining is negligible,so no need of umberalla"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(password="voiggbqmndvtuvtr", user="panwarakhil033@gmail.com")
connection.sendmail(from_addr="panwarakhil033@gmail.com", to_addrs=recipent,
                            msg=f"Subject:weather forecast\n\n{message} ")
connection.close()

