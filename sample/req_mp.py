from System.Net import *
from System.IO import *
from System.Text import *


#for missionplanner.
url = "localhost:5000"
encoding = Encoding.GetEncoding("utf-8")

req = WebRequest.Create(url)
res = req.GetResponse()
res_stream = res.GetResponseStream()
sr = StreamReader(res_stream)
response = sr.ReadToEnd()

data = eval(response)
print(data[0])

sr.Close()
res.Close()