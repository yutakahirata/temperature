from bottle import route, view
from datetime import datetime
import time,requests,json
import gauges
@route('/')
@route('/home')
@view('index')
def home():
    return dict(
        year=datetime.now().year,gauge=gauges.canvas
    )

global temp, humid,temp1,humid1,press1
temp, humid,temp1,humid1,press1=0,0,0,0,0
@route('/temp',method = "GET")
def temp():
    global temp, humid,temp1,humid1,press1
    try:
        r = requests.post('http://192.168.1.13/temp')
        rx = requests.post('http://192.168.1.13/humidity')
        t=int(r.text)
        h=int(rx.text)
        if t==2147483647 or h==2147483647: return dict(text="",text1="",t=temp,h=humid,t1=temp1,h1=humid1,p1=press1)
        temp, humid=t,h
        rxx= requests.get('http://192.168.1.111:8080/BME280')
        j=json.loads(rxx.text)
        print(j)
        temp1,humid1,press1=j['temp'],j['humid'],j['pressure']
    except:
        dict(text="",text1="",t=temp,h=humid,t1=temp1,h1=humid1,p1=press1)
    tmp=str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))+"<br>温度:%7.2f℃"%temp+"<br>湿度:%7.2f％"%humid
    print(tmp)
    tmp1=str(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))+"<br>温度:%7.2f℃"%temp1+"<br>湿度:%7.2f％"%humid1+"<br>気圧:%7.2fhp"%press1
    print(tmp1)
    return dict(text=tmp,text1=tmp1,t=temp,h=humid,t1=temp1,h1=humid1,p1=press1)
