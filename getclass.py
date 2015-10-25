import json 
import httplib,urllib,json
from pytz import timezone
from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta

'''GET /ntss/xskbxx!xskbList.action?xnxqdm=1368&zc=12 HTTP/1.1
Host: 192.168.176.246:8080
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36
Referer: http://192.168.176.246:8080/ntss/xskbxx!xskbMain.action
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8
Cookie: JSESSIONID='''

def get(JSESSIONID,zc):
    fp=open('zc%s.ics'%zc,'wb')
    cal = Calendar()
    cal.add('version','2.0')
    word ='JSESSIONID='+JSESSIONID
    params = urllib.urlencode({'xnxqdm': 1369, 'zc': zc})
    headers = {"Content-type": "application/x-www-form-urlencoded","Cookie": word}  
    conn = httplib.HTTPConnection("192.168.176.246:8080")
    conn.request("POST", "/ntss/xskbxx!xskbList.action", params, headers)
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    weekdate1 = data.split('星期一<br>')
    weekdate = weekdate1[1][0:10]
    monthdate = 31
    if weekdate[5:7]=='04' or weekdate[5:7]=='06' or weekdate[5:7]=='09' or  weekdate[5:7]=='11' :
        monthdate = 30
    elif weekdate[5:7]=='02':
        monthdate = 28
    print(weekdate)
    word = data.split('[{')
    if 	len(word) == 1:
		data = ''
    else:
		word1= word[1].split('}]')
		data = '[{'+word1[0]+'}]'
		js=json.loads(data)
		for i in js:
			kcmc = i["kcmc"]
			jxcdmc = i["jxcdmc"]
			teaxm = i["teaxm"]
			jcdm = i["jcdm"]
			xq = i["xq"]
			al = Alarm()     
			al.add('TRIGGER', timedelta(0, 600))
			al.add('ACTION','DISPLAY')
			event= Event()
			event.add('summary', kcmc)
			hstart = 8
			hend = 9
			mstart = 00
			mend = 30
			day = (int(weekdate[8:10])+int(xq)-1)
			month = int(weekdate[5:7])
			if jcdm =='0304':
				hstart = 9
				hend = 11
				mstart = 40
				mend = 20
			elif jcdm == '030405':
				hstart = 9
				hend = 12
				mstart = 40
				mend = 00
			elif jcdm == '0607':
				hstart = 14
				hend = 16
				mstart = 30
				mend = 10
			elif jcdm == '060708':
				hstart = 14
				hend = 16
				mstart = 30
				mend = 40
			elif jcdm == '0809':
				hstart = 16
				hend = 17
				mstart = 10
				mend = 40
			elif jcdm == '1011':
				hstart = 18
				hend = 20
				mstart = 30
				mend = 30
			elif jcdm == '01020304':
				hstart = 8
				hend = 11
				mstart = 00
				mend = 10
			elif jcdm == '06070809':
				hstart = 14
				hend = 17
				mstart = 30
				mend = 40
			elif jcdm == '0102030405':
				hstart = 8
				hend = 12
				mstart = 00
				mend = 00
			if day>monthdate:
				day = day-monthdate
				print day
				month = month+1
			event.add('dtstart', datetime(int(weekdate[0:4]),month,day,hstart,mstart,0,tzinfo=timezone('Asia/Shanghai')))
			event.add('dtend', datetime(int(weekdate[0:4]),month,day,hend,mend,0,tzinfo=timezone('Asia/Shanghai')))
			event.add('description', jxcdmc + '--'+teaxm)
			event.add_component(al)
			cal.add_component(event)
    a=cal.to_ical()    
    fp.write(a)    
    fp.close()
    conn.close()
    pass

