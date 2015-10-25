from socket import *
JSESSIONID =0 
data = '''GET /ntss/ HTTP/1.1
Host: 192.168.176.246:8080
Connection: keep-alive

'''
data2 ='''POST /ntss/login!welcome.action HTTP/1.1
Host: 192.168.176.246:8080
Connection: keep-alive
Content-Length: 87
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: http://192.168.176.246:8080
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Referer: http://192.168.176.246:8080/ntss/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: JSESSIONID=CDCA1AA3A4DA5C371E07B2C336016690

account=3138010031&pwd=3138010031&verifycode=1865&mmtip=&ok=%E7%A1%AE%E3%80%80%E8%AE%A4

'''
data3 = '''GET /ntss/verifycode.servlet HTTP/1.1
Host: 192.168.176.246:8080
Connection: keep-alive
Cookie: JSESSIONID=60441D87D39982121B6382E4F17AF164

'''

print(data)
client = socket(AF_INET, SOCK_STREAM)
client.connect(('192.168.176.246',8080))
client.send(data.encode('utf8'))
data1 = client.recv(1024)
#data1 =data1+ client.recv(1024)
sw = data1.split('JSESSIONID=')
JSESSIONID = (sw[1][0:32])
print(JSESSIONID)
#print('%s' %data1)
#print('%s' %data1.decode('utf8'))

#for i in data1:
#    print(i)
    
fp = open("test.txt",'w')
fp.writelines(data1)
fp.close()
 
