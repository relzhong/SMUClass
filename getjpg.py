import httplib,urllib



'''GET /ntss/verifycode.servlet HTTP/1.1
Host: 192.168.176.246:8080
Connection: keep-alive
Cookie: JSESSIONID='''


def get(JSESSIONID):
    word ='JSESSIONID='+JSESSIONID
    headers = {"Content-type": "application/x-www-form-urlencoded","Cookie": word}  
    conn = httplib.HTTPConnection("192.168.176.246:8080")
    conn.request("GET", "/ntss/verifycode.servlet",None,headers)
    response = conn.getresponse()
#    print response.msg, response.reason
    data = response.read()
    fp = open("test.jpg",'wb')
    fp.write(data)
    fp.close()
    conn.close()
    pass


