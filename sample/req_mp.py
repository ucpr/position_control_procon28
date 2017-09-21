from System.Net import *
from System.IO import *


#for missionplanner.
url = "localhost:5000"

req = WebRequest.Create(url)
res = req.GetResponse()
res_stream = res.GetResponseStream()
sr = StreamReader(res_stream)
response = sr.ReadToEnd()

data = eval(response)
print(data[0])

sr.Close()
res.Close()
