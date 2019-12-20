import urllib, json, sys, os.path, getpass, time
import urllib.request

import Retrieve
import transcode
import write_ws
import configuration


def getToken(host, port, user) :
   ltoken = os.path.normpath(os.path.expanduser("~/.klocwork/ltoken"))
   ltokenFile = open(ltoken, 'r')
   for r in ltokenFile :
      rd = r.strip().split(';')
      if rd[0] == host and rd[1] == str(port) and rd[2] == user :
        ltokenFile.close()
        return rd[3]
   ltokenFile.close()

# ---- main routine start ----
# load server configuraions
server = configuration.server #"brookmanwang.altek.c.t"
host = configuration.host #'BrookmanWang'
port = configuration.port #8080
user = configuration.user #'jensonchin' #user = getpass.getuser()

url = "http://%s:%d/review/api" % (server, port)

#projects = configuration.projects


loginToken = getToken(host, port, user)
#if loginToken is not None :
#   values["ltoken"] = loginToken
#print('token = {t}'.format(t = loginToken))

# Fill first row with the predefined names
#print('Keys = {k}'.format(k = transcode.coded.keys()))

keys = []
for k in transcode.coded.keys():
   keys.append(k)
#wb = write_ws.init(keys)
wb = write_ws.create_wb()

#Get project list according to the configuration
project_list = Retrieve.get_project_list(url, user, loginToken)
projects = transcode.project_list(project_list, configuration.pid_include, configuration.pid_exclude)
#projects = []
#projects.append("WAVE3_RCApp_ContinuaService")
# main control loop
for pj in projects:
   print("Project = {p}".format(p = pj))
   # Get an overview for all open issues
   issues = []
   issues = Retrieve.search_open_issue(url, user, pj, loginToken)

   ws = write_ws.create_ws(wb, pj, keys)

   #Get more detail for each issue
   row = 2  #start with 2 as 1st row has been filled
   for i in issues:
      id = i.get('id')
      #print("ID = {id}".format(id = id))
      xsync = "false"
      #detail = Retrieve.issue_detail(url, user, project, loginToken, issues[0].get('id'), xsync)
      detail = Retrieve.issue_detail(url, user, pj, loginToken, id, xsync)
      coded_detail = transcode.transcode(detail)
      #print('type = {t}'.format(t = type(coded_detail.keys())))

      #convert the coded detail in dict type to a list in str
      d_list = list(coded_detail.values())
      write_ws.write2ws(d_list, ws, row)
      row = row + 1


wb.save(configuration.name_report) #save it

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