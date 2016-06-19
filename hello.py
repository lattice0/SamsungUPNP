import http.client

conn = http.client.HTTPConnection("192.168.1.107", 7676)

headers = {"Content-type": "text/xml; charset='utf-8'",

"SOAPACTION": "SoapAction:urn:schemas-upnp-org:service:RenderingControl:1#SetVolume "}

#body = '<?xml version="1.0" encoding="utf-8"?> <s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"> <s:Body> <ns0:GetVolume xmlns:ns0="urn:schemas-upnp-org:service:RenderingControl:1"> <InstanceID>0</InstanceID> <Channel>Master</Channel> </ns0:GetVolume> </s:Body> </s:Envelope>'

body = """<?xml version="1.0" encoding="utf-8"?>

<s:Envelope s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/" xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">

<s:Body>

<ns0:SetVolume  xmlns:ns0="urn:schemas-upnp-org:service:RenderingControl:1">

<InstanceID>0</InstanceID>

<Channel>Master</Channel>

<InstanceID>0</InstanceID>

<DesiredVolume>21</DesiredVolume>

</ns0:SetVolume >

</s:Body>

</s:Envelope>

"""



conn.request("POST","/smp_13_",body,headers)

response = conn.getresponse()

print(response.status, response.reason)
