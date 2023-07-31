from flask import Flask, render_template, request
from geopy.geocoders import Nominatim
import datetime
import requests
from flask import redirect,url_for
import pandas as pd
from twilio.rest import Client
import matplotlib.pyplot as plt
import seaborn as sns
from googletrans import Translator




app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():


    end_point = "https://api.openweathermap.org/data/2.5/forecast"
    api_key = "8c81c4a2f6b7546cac7913f74b54311c"
    weather_parmeter = {
        "lat": 9.9261153, "lon": 78.1140983, "appid": api_key,
    }
    res = requests.get(end_point, params=weather_parmeter)
    weather_data = res.json()
#------------------------------------API COLLECTION DATA ENDS--------------------------------------------------------


    twele_hour_data = weather_data["list"][:39]
    temperature = twele_hour_data[0]["main"]["temp"]
    temperature_feel = twele_hour_data[0]["main"]["feels_like"]
    celsius_temperature = round(temperature - 273.15)
    celsius_temperature_feel = round(temperature_feel - 273.15)
    weather_name = twele_hour_data[0]["weather"][0]["main"]
    city = weather_data["city"]["name"]
    hum = twele_hour_data[0]["main"]["humidity"]
    pre = twele_hour_data[0]["main"]["pressure"]
    des = twele_hour_data[0]["weather"][0]["description"]
    id_no = twele_hour_data[0]["weather"][0]["id"]
    wind = twele_hour_data[0]["wind"]["speed"]


#----------------------------------------CURRENT WEATGER DATA CLOSED--------------------------------------------------------------


    next1_temp=twele_hour_data[1]["main"]["temp"]
    next1_celsius=round(next1_temp-273.15)
    id_no1 = twele_hour_data[1]["weather"][0]["id"]
    weather_time1=twele_hour_data[1]["dt_txt"].split()[1][:2]


    next2_temp=twele_hour_data[2]["main"]["temp"]
    next2_celsius=round(next2_temp-273.15)
    id_no2 = twele_hour_data[2]["weather"][0]["id"]
    weather_time2=twele_hour_data[2]["dt_txt"].split()[1][:2]


    next3_temp=twele_hour_data[3]["main"]["temp"]
    next3_celsius=round(next3_temp-273.15)
    id_no3 = twele_hour_data[3]["weather"][0]["id"]
    weather_time3=twele_hour_data[3]["dt_txt"].split()[1][:2]



    next4_temp=twele_hour_data[4]["main"]["temp"]
    next4_celsius=round(next4_temp-273.15)
    id_no4 = twele_hour_data[4]["weather"][0]["id"]
    weather_time4=twele_hour_data[4]["dt_txt"].split()[1][:2]


#-----------------------------------------NEXT WEATHER DATA ENDS-------------------------------------------------------

    date_time = datetime.datetime.now()
    date = date_time.strftime("%d")
    month = date_time.strftime("%b")
    time = date_time.strftime("%H")
    pm_or_am = date_time.strftime("%p")
    day=date_time.strftime("%a")
   # con_time=date_time.now()
    #con_est=con_time.strftime("%I")
    a=f"{date} {month}"
    b=f"{time}"
    c=f"{pm_or_am}"
    d=city
    e=day

#---------------------------------------DATE TIME DATA ENDS---------------------------------------------------------------------

    if request.method=="POST":
        home2=request.form["search"]
        return redirect((url_for("home2",city=home2)))

    else:
        return render_template("weather.html",celsius=celsius_temperature,weather=weather_name,celsius_feel=celsius_temperature_feel,
                           date=a,time=int(b),std=c,city_name=d,day=e,humidity=hum,pressure=pre,desc=des,air=wind,id=id_no,
                           next1_t=next1_celsius,next2_t=next2_celsius,next3_t=next3_celsius,next4_t=next4_celsius,id1=id_no1,id2=id_no2,
                           id3=id_no3,id4=id_no4,up_time1=int(weather_time1),up_time2=int(weather_time2),up_time3=int(weather_time3),up_time4=int(weather_time4))





#---------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------first data ends-----------------------------------------------------------

@app.route('/<city>')
def home2(city):
    loc = Nominatim(user_agent="GetLoc")
    ci = city
    getLoc = loc.geocode(ci)
    data = getLoc.address
    lat = getLoc.latitude
    lon = getLoc.longitude



    end_point = "https://api.openweathermap.org/data/2.5/forecast"
    api_key = "8c81c4a2f6b7546cac7913f74b54311c"
    weather_parmeter = {
        "lat": lat, "lon": lon, "appid": api_key,
    }
    res = requests.get(end_point, params=weather_parmeter)
    weather_data = res.json()

    twele_hour_data = weather_data["list"][:5]
    temperature = twele_hour_data[0]["main"]["temp"]
    temperature_feel = twele_hour_data[0]["main"]["feels_like"]
    celsius_temperature = round(temperature - 273.15)
    celsius_temperature_feel = round(temperature_feel - 273.15)
    weather_name = twele_hour_data[0]["weather"][0]["main"]
    city = weather_data["city"]["name"]
    hum = twele_hour_data[0]["main"]["humidity"]
    pre = twele_hour_data[0]["main"]["pressure"]
    des = twele_hour_data[0]["weather"][0]["description"]
    id_no = twele_hour_data[0]["weather"][0]["id"]
    wind = twele_hour_data[0]["wind"]["speed"]

    # ---------------------------------------- SECOND CURRENT WEATGER DATA CLOSED--------------------------------------------------------------

    next1_temp = twele_hour_data[1]["main"]["temp"]
    next1_celsius = round(next1_temp - 273.15)
    id_no1 = twele_hour_data[1]["weather"][0]["id"]
    weather_time1 = twele_hour_data[1]["dt_txt"].split()[1][:2]

    next2_temp = twele_hour_data[2]["main"]["temp"]
    next2_celsius = round(next2_temp - 273.15)
    id_no2 = twele_hour_data[2]["weather"][0]["id"]
    weather_time2 = twele_hour_data[2]["dt_txt"].split()[1][:2]

    next3_temp = twele_hour_data[3]["main"]["temp"]
    next3_celsius = round(next3_temp - 273.15)
    id_no3 = twele_hour_data[3]["weather"][0]["id"]
    weather_time3 = twele_hour_data[3]["dt_txt"].split()[1][:2]

    next4_temp = twele_hour_data[4]["main"]["temp"]
    next4_celsius = round(next4_temp - 273.15)
    id_no4 = twele_hour_data[4]["weather"][0]["id"]
    weather_time4 = twele_hour_data[4]["dt_txt"].split()[1][:2]

    # -----------------------------------------SECOND NEXT WEATHER DATA ENDS-------------------------------------------------------

    date_time = datetime.datetime.now()
    date = date_time.strftime("%d")
    month = date_time.strftime("%b")
    time = date_time.strftime("%H")
    pm_or_am = date_time.strftime("%p")
    day = date_time.strftime("%a")
    # con_time=date_time.now()
    # con_est=con_time.strftime("%I")
    a = f"{date} {month}"
    b = f"{time}"
    c = f"{pm_or_am}"
    d = city
    e = day

# ---------------------------------------SECOND DATE TIME DATA ENDS---------------------------------------------------------------------
    return render_template("search.html", celsius=celsius_temperature, weather=weather_name,
                           celsius_feel=celsius_temperature_feel,
                           date=a, time=int(b), std=c, city_name=d, day=e, humidity=hum, pressure=pre, desc=des,
                           air=wind, id=id_no,
                           next1_t=next1_celsius, next2_t=next2_celsius, next3_t=next3_celsius, next4_t=next4_celsius,
                           id1=id_no1, id2=id_no2,
                           id3=id_no3, id4=id_no4, up_time1=int(weather_time1), up_time2=int(weather_time2),
                           up_time3=int(weather_time3), up_time4=int(weather_time4))



@app.route('/home3')
def home3():

        end_point = "https://api.openweathermap.org/data/2.5/forecast"
        api_key = "8c81c4a2f6b7546cac7913f74b54311c"
        weather_parmeter = {
            "lat": 9.9261153, "lon": 78.1140983, "appid": api_key,
        }
        res = requests.get(end_point, params=weather_parmeter)
        weather_data = res.json()

        city = weather_data["city"]["name"]

        filter = weather_data["list"]




        farenheit = filter[1]["main"]["temp"]
        temperature2 = round(farenheit - 273.15)
        date_time = filter[1]["dt_txt"].split()
        date2 = date_time[0]
        time2 = date_time[1]
        idno2 = filter[1]["weather"][0]["id"]
        weather2 = filter[1]["weather"][0]["description"]

        farenheit = filter[2]["main"]["temp"]
        temperature3 = round(farenheit - 273.15)
        date_time = filter[2]["dt_txt"].split()
        date3 = date_time[0]
        time3 = date_time[1]
        idno3 = filter[2]["weather"][0]["id"]
        weather3 = filter[2]["weather"][0]["description"]

        farenheit = filter[3]["main"]["temp"]
        temperature4 = round(farenheit - 273.15)
        date_time = filter[3]["dt_txt"].split()
        date4 = date_time[0]
        time4 = date_time[1]
        idno4 = filter[3]["weather"][0]["id"]
        weather4 = filter[3]["weather"][0]["description"]

        farenheit = filter[4]["main"]["temp"]
        temperature5 = round(farenheit - 273.15)
        date_time = filter[4]["dt_txt"].split()
        date5 = date_time[0]
        time5 = date_time[1]
        idno5 = filter[4]["weather"][0]["id"]
        weather5 = filter[4]["weather"][0]["description"]

        farenheit = filter[5]["main"]["temp"]
        temperature6 = round(farenheit - 273.15)
        date_time = filter[5]["dt_txt"].split()
        date6 = date_time[0]
        time6 = date_time[1]
        idno6 = filter[5]["weather"][0]["id"]
        weather6 = filter[5]["weather"][0]["description"]

        farenheit = filter[6]["main"]["temp"]
        temperature7 = round(farenheit - 273.15)
        date_time = filter[6]["dt_txt"].split()
        date7 = date_time[0]
        time7 = date_time[1]
        idno7 = filter[6]["weather"][0]["id"]
        weather7 = filter[6]["weather"][0]["description"]

        farenheit = filter[7]["main"]["temp"]
        temperature8 = round(farenheit - 273.15)
        date_time = filter[7]["dt_txt"].split()
        date8 = date_time[0]
        time8 = date_time[1]
        idno8 = filter[7]["weather"][0]["id"]
        weather8 = filter[7]["weather"][0]["description"]

        farenheit = filter[8]["main"]["temp"]
        temperature9 = round(farenheit - 273.15)
        date_time = filter[8]["dt_txt"].split()
        date9 = date_time[0]
        time9 = date_time[1]
        idno9 = filter[8]["weather"][0]["id"]
        weather9 = filter[8]["weather"][0]["description"]

        farenheit = filter[9]["main"]["temp"]
        temperature10 = round(farenheit - 273.15)
        date_time = filter[9]["dt_txt"].split()
        date10 = date_time[0]
        time10 = date_time[1]
        idno10 = filter[9]["weather"][0]["id"]
        weather10 = filter[9]["weather"][0]["description"]

        farenheit = filter[10]["main"]["temp"]
        temperature11 = round(farenheit - 273.15)
        date_time = filter[10]["dt_txt"].split()
        date11 = date_time[0]
        time11 = date_time[1]
        idno11 = filter[10]["weather"][0]["id"]
        weather11 = filter[10]["weather"][0]["description"]

        farenheit = filter[11]["main"]["temp"]
        temperature12 = round(farenheit - 273.15)
        date_time = filter[11]["dt_txt"].split()
        date12 = date_time[0]
        time12 = date_time[1]
        idno12 = filter[11]["weather"][0]["id"]
        weather12 = filter[11]["weather"][0]["description"]

        farenheit = filter[12]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[12]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[12]["weather"][0]["id"]
        weather13 = filter[12]["weather"][0]["description"]

        farenheit = filter[12]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[12]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[12]["weather"][0]["id"]
        weather13 = filter[12]["weather"][0]["description"]

        farenheit = filter[13]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[13]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[13]["weather"][0]["id"]
        weather13 = filter[13]["weather"][0]["description"]

        farenheit = filter[14]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[14]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[14]["weather"][0]["id"]
        weather13 = filter[14]["weather"][0]["description"]

        farenheit = filter[15]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[15]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[15]["weather"][0]["id"]
        weather13 = filter[15]["weather"][0]["description"]

        farenheit = filter[16]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[16]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[16]["weather"][0]["id"]
        weather13 = filter[16]["weather"][0]["description"]

        farenheit = filter[17]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[17]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[17]["weather"][0]["id"]
        weather13 = filter[17]["weather"][0]["description"]

        farenheit = filter[18]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[18]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[18]["weather"][0]["id"]
        weather13 = filter[18]["weather"][0]["description"]

        farenheit = filter[19]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[19]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[19]["weather"][0]["id"]
        weather13 = filter[19]["weather"][0]["description"]

        farenheit = filter[20]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[20]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[20]["weather"][0]["id"]
        weather13 = filter[20]["weather"][0]["description"]

        farenheit = filter[21]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[21]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[21]["weather"][0]["id"]
        weather13 = filter[21]["weather"][0]["description"]

        farenheit = filter[22]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[22]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[22]["weather"][0]["id"]
        weather13 = filter[22]["weather"][0]["description"]

        farenheit = filter[23]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[23]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[23]["weather"][0]["id"]
        weather13 = filter[23]["weather"][0]["description"]

        farenheit = filter[24]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[24]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[24]["weather"][0]["id"]
        weather13 = filter[24]["weather"][0]["description"]

        farenheit = filter[25]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[25]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[25]["weather"][0]["id"]
        weather13 = filter[25]["weather"][0]["description"]

        farenheit = filter[26]["main"]["temp"]
        temperature13 = round(farenheit - 273.15)
        date_time = filter[26]["dt_txt"].split()
        date13 = date_time[0]
        time13 = date_time[1]
        idno13 = filter[26]["weather"][0]["id"]
        weather13 = filter[26]["weather"][0]["description"]


        return render_template("content2.html", location=city
                               , temp2=temperature2, date2=date2, ti2=time2, id2=idno2, wea2=weather2
                               , temp3=temperature3, date3=date3, ti3=time3, id3=idno3, wea3=weather3
                               , temp4=temperature4, date4=date4, ti4=time4, id4=idno4, wea4=weather4
                               , temp5=temperature5, date5=date5, ti5=time5, id5=idno5, wea5=weather5
                               , temp6=temperature6, date6=date6, ti6=time6, id6=idno6, wea6=weather6
                               , temp7=temperature7, date7=date7, ti7=time7, id7=idno7, wea7=weather7
                               , temp8=temperature8, date8=date8, ti8=time8, id8=idno8, wea8=weather8
                               , temp9=temperature9, date9=date9, ti9=time9, id9=idno9, wea9=weather9
                               , temp10=temperature10, date10=date10, ti10=time10, id10=idno10, wea10=weather10
                               , temp11=temperature11, date11=date11, ti11=time11, id11=idno11, wea11=weather11
                               , temp12=temperature12, date12=date12, ti12=time12, id12=idno12, wea12=weather12
                               , temp13=temperature13, date13=date13, ti13=time13, id13=idno13, wea13=weather13

                               )

@app.route('/<city>/home4')
def home4(city):
    loc = Nominatim(user_agent="GetLoc")
    ci = city
    getLoc = loc.geocode(ci)
    data = getLoc.address
    lat = getLoc.latitude
    lon = getLoc.longitude

    end_point = "https://api.openweathermap.org/data/2.5/forecast"
    api_key = "8c81c4a2f6b7546cac7913f74b54311c"
    weather_parmeter = {
        "lat": lat, "lon": lon, "appid": api_key,
    }
    res = requests.get(end_point, params=weather_parmeter)
    weather_data = res.json()

    city = weather_data["city"]["name"]

    filter = weather_data["list"]

    farenheit = filter[1]["main"]["temp"]
    temperature2 = round(farenheit - 273.15)
    date_time = filter[1]["dt_txt"].split()
    date2 = date_time[0]
    time2 = date_time[1]
    idno2 = filter[1]["weather"][0]["id"]
    weather2 = filter[1]["weather"][0]["description"]

    farenheit = filter[2]["main"]["temp"]
    temperature3 = round(farenheit - 273.15)
    date_time = filter[2]["dt_txt"].split()
    date3 = date_time[0]
    time3 = date_time[1]
    idno3 = filter[2]["weather"][0]["id"]
    weather3 = filter[2]["weather"][0]["description"]

    farenheit = filter[3]["main"]["temp"]
    temperature4 = round(farenheit - 273.15)
    date_time = filter[3]["dt_txt"].split()
    date4 = date_time[0]
    time4 = date_time[1]
    idno4 = filter[3]["weather"][0]["id"]
    weather4 = filter[3]["weather"][0]["description"]

    farenheit = filter[4]["main"]["temp"]
    temperature5 = round(farenheit - 273.15)
    date_time = filter[4]["dt_txt"].split()
    date5 = date_time[0]
    time5 = date_time[1]
    idno5 = filter[4]["weather"][0]["id"]
    weather5 = filter[4]["weather"][0]["description"]

    farenheit = filter[5]["main"]["temp"]
    temperature6 = round(farenheit - 273.15)
    date_time = filter[5]["dt_txt"].split()
    date6 = date_time[0]
    time6 = date_time[1]
    idno6 = filter[5]["weather"][0]["id"]
    weather6 = filter[5]["weather"][0]["description"]

    farenheit = filter[6]["main"]["temp"]
    temperature7 = round(farenheit - 273.15)
    date_time = filter[6]["dt_txt"].split()
    date7 = date_time[0]
    time7 = date_time[1]
    idno7 = filter[6]["weather"][0]["id"]
    weather7 = filter[6]["weather"][0]["description"]

    farenheit = filter[7]["main"]["temp"]
    temperature8 = round(farenheit - 273.15)
    date_time = filter[7]["dt_txt"].split()
    date8 = date_time[0]
    time8 = date_time[1]
    idno8 = filter[7]["weather"][0]["id"]
    weather8 = filter[7]["weather"][0]["description"]

    farenheit = filter[8]["main"]["temp"]
    temperature9 = round(farenheit - 273.15)
    date_time = filter[8]["dt_txt"].split()
    date9 = date_time[0]
    time9 = date_time[1]
    idno9 = filter[8]["weather"][0]["id"]
    weather9 = filter[8]["weather"][0]["description"]

    farenheit = filter[9]["main"]["temp"]
    temperature10 = round(farenheit - 273.15)
    date_time = filter[9]["dt_txt"].split()
    date10 = date_time[0]
    time10 = date_time[1]
    idno10 = filter[9]["weather"][0]["id"]
    weather10 = filter[9]["weather"][0]["description"]

    farenheit = filter[10]["main"]["temp"]
    temperature11 = round(farenheit - 273.15)
    date_time = filter[10]["dt_txt"].split()
    date11 = date_time[0]
    time11 = date_time[1]
    idno11 = filter[10]["weather"][0]["id"]
    weather11 = filter[10]["weather"][0]["description"]

    farenheit = filter[11]["main"]["temp"]
    temperature12 = round(farenheit - 273.15)
    date_time = filter[11]["dt_txt"].split()
    date12 = date_time[0]
    time12 = date_time[1]
    idno12 = filter[11]["weather"][0]["id"]
    weather12 = filter[11]["weather"][0]["description"]

    farenheit = filter[12]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[12]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[12]["weather"][0]["id"]
    weather13 = filter[12]["weather"][0]["description"]

    farenheit = filter[12]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[12]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[12]["weather"][0]["id"]
    weather13 = filter[12]["weather"][0]["description"]

    farenheit = filter[13]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[13]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[13]["weather"][0]["id"]
    weather13 = filter[13]["weather"][0]["description"]

    farenheit = filter[14]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[14]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[14]["weather"][0]["id"]
    weather13 = filter[14]["weather"][0]["description"]

    farenheit = filter[15]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[15]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[15]["weather"][0]["id"]
    weather13 = filter[15]["weather"][0]["description"]

    farenheit = filter[16]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[16]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[16]["weather"][0]["id"]
    weather13 = filter[16]["weather"][0]["description"]

    farenheit = filter[17]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[17]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[17]["weather"][0]["id"]
    weather13 = filter[17]["weather"][0]["description"]

    farenheit = filter[18]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[18]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[18]["weather"][0]["id"]
    weather13 = filter[18]["weather"][0]["description"]

    farenheit = filter[19]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[19]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[19]["weather"][0]["id"]
    weather13 = filter[19]["weather"][0]["description"]

    farenheit = filter[20]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[20]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[20]["weather"][0]["id"]
    weather13 = filter[20]["weather"][0]["description"]

    farenheit = filter[21]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[21]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[21]["weather"][0]["id"]
    weather13 = filter[21]["weather"][0]["description"]

    farenheit = filter[22]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[22]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[22]["weather"][0]["id"]
    weather13 = filter[22]["weather"][0]["description"]

    farenheit = filter[23]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[23]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[23]["weather"][0]["id"]
    weather13 = filter[23]["weather"][0]["description"]

    farenheit = filter[24]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[24]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[24]["weather"][0]["id"]
    weather13 = filter[24]["weather"][0]["description"]

    farenheit = filter[25]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[25]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[25]["weather"][0]["id"]
    weather13 = filter[25]["weather"][0]["description"]

    farenheit = filter[26]["main"]["temp"]
    temperature13 = round(farenheit - 273.15)
    date_time = filter[26]["dt_txt"].split()
    date13 = date_time[0]
    time13 = date_time[1]
    idno13 = filter[26]["weather"][0]["id"]
    weather13 = filter[26]["weather"][0]["description"]

    return render_template("content2.html", location=city
                           , temp2=temperature2, date2=date2, ti2=time2, id2=idno2, wea2=weather2
                           , temp3=temperature3, date3=date3, ti3=time3, id3=idno3, wea3=weather3
                           , temp4=temperature4, date4=date4, ti4=time4, id4=idno4, wea4=weather4
                           , temp5=temperature5, date5=date5, ti5=time5, id5=idno5, wea5=weather5
                           , temp6=temperature6, date6=date6, ti6=time6, id6=idno6, wea6=weather6
                           , temp7=temperature7, date7=date7, ti7=time7, id7=idno7, wea7=weather7
                           , temp8=temperature8, date8=date8, ti8=time8, id8=idno8, wea8=weather8
                           , temp9=temperature9, date9=date9, ti9=time9, id9=idno9, wea9=weather9
                           , temp10=temperature10, date10=date10, ti10=time10, id10=idno10, wea10=weather10
                           , temp11=temperature11, date11=date11, ti11=time11, id11=idno11, wea11=weather11
                           , temp12=temperature12, date12=date12, ti12=time12, id12=idno12, wea12=weather12
                           , temp13=temperature13, date13=date13, ti13=time13, id13=idno13, wea13=weather13

                           )
@app.route('/home5', methods=["GET", "POST"])
def home5():

        if request.method == "POST":
            c = request.form.get("city")
            na= request.form.get("name")
            pn= request.form.get("mobile")
            ln = request.form.get("language")


            with open(file="userdatas.csv",mode='a') as files:
                files.write(f"{na},{pn},{ln},{c}\n")

        return render_template("sms.html")

def sms():
    account_sid = "ACbd111ac9094ac011d8b6c4ef5ed0c5b0"
    auth_token = "c68ac25ec922b4d4f19208c60c8329fa"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=a,
        from_="+19789193671",
        to="+919361585219"
    )
def sms2():


    account_sid = "AC64187fd8c6f2f3f4428632ff8e706176"
    auth_token = "20ea5fccb04e1463a90c3f79ba8487dc"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=a,
        from_="+19705949467",
        to="+919361585219"
    )

    print(message.sid)
datato=0
userdats=pd.read_csv("userdatas.csv")
for i in range(len(userdats)):

    name=userdats["name"][datato]
    number=userdats["mobile"][datato]
    language=userdats["language"][datato]
    city = userdats["ci"][datato]


    print(city)
    print(name)
    print(number)
    print(language)


    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(str(city))
    data = getLoc.address
    lat = getLoc.latitude
    lon = getLoc.longitude
    print(data)
    print(f'lat:{lat}')
    print(f'lon:{lon}')



    end_point = "https://api.openweathermap.org/data/2.5/forecast"
    api_key = "8c81c4a2f6b7546cac7913f74b54311c"
    weather_parmeter = {
            "lat": lat, "lon": lon, "appid": api_key,
        }
    res = requests.get(end_point, params=weather_parmeter)
    weather_data = res.json()

    twele_hour_data = weather_data["list"][:5]
    temperature = twele_hour_data[1]["main"]["temp"]
    celsius_temperature = round(temperature - 273.15)
    print(celsius_temperature)
    weather_name = twele_hour_data[1]["weather"][0]["main"]
    des = twele_hour_data[1]["weather"][0]["description"]
    id = twele_hour_data[1]["weather"][0]["id"]
    print(des)


    if celsius_temperature<0:
        translator = Translator()
        t1=f"Hello !  {name} it's a cold place {city} in next three hours will be {des} weather conditions like {celsius_temperature}°C don't forget jackets Have a good day!"
        results = translator.translate(t1, dest=language)
        a=results.text
        print(a)
    elif id<=800:
        translator = Translator()
        t2= f"Hello {name}  {city} next three hours will be  {des} conditions like {celsius_temperature}°C  don't forget umberla☂ Have a good day!"
        results = translator.translate(t2, dest=language)
        a=results.text
        print(a)
    else:
        translator = Translator()
        t3 = f"Hello {name}  {city} next three hours will be {des} weather conditions like {celsius_temperature}°C Have a good day!"
        results = translator.translate(t3, dest=language)
        a=results.text
        print(a)
    #sms()

    datato+=1

end_point="https://api.openweathermap.org/data/2.5/forecast"
api_key="8c81c4a2f6b7546cac7913f74b54311c"
weather_parmeter={
"lat":9.9261153,"lon":78.1140983,"appid":api_key,
}
res=requests.get(end_point,params=weather_parmeter)
weather_data=res.json()
full_data=weather_data["list"][:40]

print(full_data)
#-------------------------------------------------------WRITING WEATHER DATAS___________________________________________
with open(file="weather_data.csv", mode='w') as file:
    contents = file.write(f'temperature,date,weather,humidity,wind_speed\n')
data=0
for i in range(40):
    temperature=full_data[data]["main"]["temp"]
    celsius_temperature=round(temperature-273.15)
    weather_time = full_data[data]["dt_txt"]
    weather_name = full_data[data]["weather"][0]["description"]
    hum = full_data[data]["main"]["humidity"]
    wind =full_data[data]["wind"]["speed"]

    data+=1
    with open(file="weather_data.csv",mode='a') as file:
          contents=file.write(str(f'{celsius_temperature},{weather_time},{weather_name},{hum},{wind}\n'))

#-------------------------------------------------------DATA ANALYSIS & VISUALIZATATION---------------------------------
















































if __name__=="__main__":
    app.run(debug=True)
