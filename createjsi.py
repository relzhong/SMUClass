import httplib
'''GET /ntss/ HTTP/1.1
Host: 192.168.176.246:8080
Connection: keep-alive

'''
def create():
    conn = httplib.HTTPConnection("192.168.176.246:8080")
    conn.request("GET", "/ntss/")
    response = conn.getresponse()
    data1 = str(response.msg)
    sw = data1.split('JSESSIONID=')
    JSESSIONID = (sw[1][0:32])
    return (JSESSIONID)

