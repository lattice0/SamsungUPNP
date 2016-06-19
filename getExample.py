import http.client

c = http.client.HTTPConnection('192.168.1.107',7676)
c.request("GET","/smp_12_")
print(c.getresponse().read())
