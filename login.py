from socket import *


JSESSIONID =0 
data2 ='''POST /ntss/login!welcome.action HTTP/1.1
Host: 192.168.176.246:8080
Connection: keep-alive
Content-Length: 87
Content-Type: application/x-www-form-urlencoded
Cookie: JSESSIONID='''

data='''

'''

def login(account,pwd,verifycode,JSESSIONID):
    js = 'account='+account+'&pwd='+pwd+'&verifycode=%s'%verifycode+'&mmtip=&ok=%E7%A1%AE%E3%80%80%E8%AE%A4'
    word = data2+JSESSIONID+data+js+data
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('192.168.176.246',8080))
    client.send(word.encode('utf8'))
    data1 = client.recv(1024)
    data1 =data1+ client.recv(1024)
    pass

