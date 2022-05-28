from django.shortcuts import render
import serial
from time import sleep
from .forms import SettingsForm

SETTINGS_TXT_FILE = open('./settings.txt', 'r', encoding='utf-8')
COM_PORT = SETTINGS_TXT_FILE.read()

def index(request):
    return render(request, 'index.html', {'title': 'OpenHouse'})

def your_custom_tag_django():
    return "location.href ='" + '/dasboard' +"";

def dashboard(request):
    try:
        d=1
        ser = serial.Serial(COM_PORT, baudrate = 9600, timeout=1)
        sleep(3)
        arduinoData=ser.readline()
        d=arduinoData.decode('utf-8')
        print(d)
    except:
        d='NoneNoneNone'
    return render(request, 'pages/dashboard.html', {'title': 'Dashboard || OpenHouse', 'your_custom_tag_django': your_custom_tag_django(), 'temp': d[0:2], 'humidity': d[5:7]})

def auth(request):
    return render(request, 'pages/auth.html')

def create(request):
    return render(request, 'pages/create.html')

def settings(request):
    submitbutton= request.POST.get("submit")
    comprt = ''

    form = SettingsForm(request.POST or None)
    if form.is_valid():
        comprt = form.cleaned_data["com_port"]
        cmp = open('./settings.txt', 'w')
        stgcom = cmp.write(comprt)
        cmp.close()
    return render(request, 'pages/settings.html', {'form': form})