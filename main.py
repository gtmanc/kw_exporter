import urllib, json, sys, os.path, getpass, time
import urllib.request


def getToken(host, port, user) :
   ltoken = os.path.normpath(os.path.expanduser("~/.klocwork/ltoken"))
   ltokenFile = open(ltoken, 'r')
   for r in ltokenFile :
      rd = r.strip().split(';')
      if rd[0] == host and rd[1] == str(port) and rd[2] == user :
        ltokenFile.close()
        return rd[3]
   ltokenFile.close()

def from_json(json_object) :
   if 'id' in json_object :
      return Issue(json_object)
   return json_object

server = "brookmanwang.altek.c.t"
host = 'BrookmanWang'
port = 8080
""" TODO: This should be entered by the user"""
user = 'jensonchin' #user = getpass.getuser()
project = "WAVE3_RCApp_RCFrameworkLibrary"
url = "http://%s:%d/review/api" % (server, port)

#Create dictionary 
values = {"project": project, "user": user, "action": "search"}

loginToken = getToken(host, port, user)
if loginToken is not None :
   values["ltoken"] = loginToken
print('token = {t}'.format(t = loginToken))

values["query"] = "severity:1-3"
data = urllib.parse.urlencode(values)
print('data = {d}'.format(d = data))
data = data.encode('ascii')
print(url)
#req = urllib.request.Request(url, data)
response = urllib.request.urlopen(url, data)
print(response)
for record in response :
   #print(json.loads(record, object_hook=from_json))
   print(json.loads(record))