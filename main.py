import getjpg,createjsi,login,getclass


js = createjsi.create()
getjpg.get(js)
print('input:')
vf = input()
login.login('','',vf,js)   #在这里输入用户名密码
fp=open('date.ics','wb')
fp.write('BEGIN:VCALENDAR')
fp.write('VERSION:2.0')
for i in range(1,22):
    getclass.get(js,i)
    fp1=open('zc%s.ics'%i,'rb')
    fp1.readline()            
    fp1.readline()
    while True:
        s = fp1.readline()
        if s == 'END:VCALENDAR\r\n':
            break
        fp.write(s)
fp.write('END:VCALENDAR')
    
