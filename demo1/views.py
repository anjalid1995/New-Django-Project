from django.db import Error
import pandas as pd
from datetime import datetime
import sqlite3
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render
import requests


#database connection
def connection():
    database  = "C:/Users/ANJALI/Downloads/myproject/myproject.sqlite3"
    try:
        conn = sqlite3.connect(database)
    except Error as e1:
        print(e1)
    return conn

def home(request):
    return render(request, "home.html")

def login_tb(request):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn = connection()
    email = request.POST.dict().get("email")
    password = request.POST.dict().get("psw")
    id_pass = pd.read_sql_query("SELECT count(email) as Count from register where email = '" + str(email) + "' and password = '" + str(
            password) + "'", conn)
    x = id_pass['Count'][0]

    if (x > 0):
        request.email = email
        request.session['email'] = email

        session_set = "your session is set"
        print(session_set)
        email_stat = request.session['email']
        response = requests.get('https://api.imgflip.com/get_memes')
        geodata = response.json()
        data = geodata['data']['memes']
        response = HttpResponse(render(request, 'login.html', {'email': email_stat, 'data': data[:5]}))
        response.set_cookie('email_stat', 'Hello this is your Cookies', max_age=None)
        return response

        db_email = pd.read_sql_query("select email from user_stats where email = '" + str(email) + "' ", conn)
        print("select email from user_stats where email = '" + str(email) + "'")
        x1 = db_email['email']
        if (email not in list(x1)):
         cursor.execute("INSERT INTO user_stats (email, login_time ) values ('" + str(email) + "', '" + str(timestamp) + "')")
         conn.commit()
         return login(request)
        else:
            request.email = email
            request.session['email'] = email
            session_set="your session is set"
            print(session_set)
            return login(request)
    else:
           wrong = "Wrong Username or Password"
           return render(request, 'home.html', {'wrong': wrong})

def register(request):
 return render(request, 'register.html')

def user_create(request):
    email = request.POST.dict().get("email")
    print(email)
    password1 = request.POST.dict().get("psw")
    password2 = request.POST.dict().get("psw-repeat")
    conn = connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO register (Email, Password , 'Repeat Password') values ('" + str(email) + "', '" + str(
            password1) + "', '" + str(password2) + "')")
        conn.commit()
    except:
        return render(request, 'register.html', {'exist': 'User Already Exist'})
    return home(request)

def login(request):
 email = request.email
 return render(request,'login.html',{'email': email})

def user_stats(request):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    email = request.POST.dict().get("email")
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_stats (email, login_time ) values ('" + str(email) + "', '" + str(timestamp) + "')")
    conn.commit()
    return home(request)

def logout(request):
    email_stat = request.session['email']
    del request.session['email']
    return render(request,'logout.html',{'email': email_stat})

def about(request):
    if request.session.has_key('email'):
        return render(request,'about.html')
    else:
        return render(request,'home.html')





