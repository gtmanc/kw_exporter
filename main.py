import urllib, json, sys, os.path, getpass, time
import urllib.request

import Retrieve
import transcode


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
projects = {"WAVE3_RCApp_RCFrameworkLibrary"}
url = "http://%s:%d/review/api" % (server, port)

loginToken = getToken(host, port, user)
#if loginToken is not None :
#   values["ltoken"] = loginToken
#print('token = {t}'.format(t = loginToken))

for pj in projects:
   print("Project = {p}".format(p = pj))
   # Get an overview for all open issues
   issues = []
   issues = Retrieve.search_open_issue(url, user, pj, loginToken)

   #Get more detail for each issue
   for i in issues:
      id = i.get('id')
      print("ID = {id}".format(id = id))
      xsync = "false"
      #detail = Retrieve.issue_detail(url, user, project, loginToken, issues[0].get('id'), xsync)
      detail = Retrieve.issue_detail(url, user, pj, loginToken, id, xsync)
      transcode.transcode(detail)
#history = detail.get('history')

#print('History = {c}'.format(c = history))
#print('type = {t}'.format(t= type(history)))
#print('type = {t}'.format(t= type(history[0])))
#print(history[0].get('date'))
#print(history[1])

#for record in response :
   #print(json.loads(record, object_hook=from_json))
#   print(json.loads(record))
#   break