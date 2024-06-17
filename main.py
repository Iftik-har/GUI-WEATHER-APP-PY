from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=7790adf22b06e8c61f0cbf93dacc2ac0"

        json_data=requests.get(api).json()
        condition=json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")

# ------------------------------------------search box:-------------------------------------------------

Search_image=PhotoImage(file="images/search.png")
myimage=Label(image=Search_image)
myimage.place(x=200,y=20)

# -------------------------------------------textfield:-------------------------------------------------

textfield=tk.Entry(root,justify="center",width=10,font=("poppins",20,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=330,y=40)
textfield.focus()

# -------------------------------------------search icon:------------------------------------------------

Search_icon=PhotoImage(file="images/search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=570,y=34)

# ----------------------------------------------logo:----------------------------------------------------

Logo_image=PhotoImage(file="images/logo.png")
logo=Label(image=Logo_image)
logo.place(x=290,y=100)

# -------------------------------------------Button box--------------------------------------------------

Frame_image=PhotoImage(file="images/box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

# ----------------------------------------------Time-----------------------------------------------------

name=Label(root,font=("arial",15,"bold"))
name.place(x=85,y=200)
clock=Label(root,font=("Helvetica",20))
clock.place(x=130,y=260)

# ---------------------------------------------label------------------------------------------------------

label1=Label(root,text="WIND",font=("helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400 )

label2=Label(root,text="HUMIDITY",font=("helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=250,y=400 )

label3=Label(root,text="DESCRIPTION",font=("helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=430,y=400 )

label4=Label(root,text="PRESSURE",font=("helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=650,y=400 )

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=560,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=560,y=270)
w=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",15,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)


root.mainloop()

