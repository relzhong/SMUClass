from socket import *


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
Cookie: JSESSIONID='''
data4='''

'''

def get(JSESSIONID):
    flag=0
    word=data3+JSESSIONID+data4
    sp1='\r\n\r\n'
    dsp1=sp1.encode()
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('192.168.176.246',8080))
    client.send(word.encode('utf8'))
    data1 = client.recv(1024)
    data1 =data1+ client.recv(1024)
    for i in range(1024):
        if dsp1[0]==data1[i]:
            if dsp1[1]==data1[i+1]:
                if dsp1[2]==data1[i+2]:
                    if dsp1[3]==data1[i+3]:
                        flag=i+4
                        break


    for i in range(1024):
        if dsp1[0]==data1[flag+i]:
            if dsp1[1]==data1[flag+i+1]:
                flag=flag+i+2
                break

    data1=data1[flag:]

    fp = open("test.jpg",'wb')
    fp.write(data1)
    fp.close()
    pass


