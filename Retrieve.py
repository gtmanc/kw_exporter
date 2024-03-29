import urllib.request,json

import configuration

"""
Search all open issue in a project.
Input
url: url
user: user name
project: project name
token: token needed for server uthenticaion
Output:
List of dict. Each dict in the list stres the basic information of an issue.
"""
def search_open_issue(url, user, project, token):
    values = {"project": project, "user": user, "action": "search", "ltoken": token}
    values["query"] = configuration.query
    
    data = urllib.parse.urlencode(values)
    #print('data = {d}'.format(d = data))
    data = data.encode('ascii')
    #print(url)
    #req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(url, data)

    list_issue = []
    i = 0
    for record in response :
        #print(type(record))
        #print(record)
        #print(json.loads(record, object_hook=from_json))
        
        list_issue.append(json.loads(record))
        #print(type(issue[i]))
        #print(issue[i])
        i = i + 1
    
    print('Number of issues = {no}'.format(no = len(list_issue)))
    return list_issue


"""
Get detail for an specified issue.
Input
url: url
user: user name
project: project name
token: token needed for server uthenticaion
Output:
Dict which contain all of the detail of an issue
"""
def issue_detail(url, user, project, token, id, xsync=None):
    values = {"user": user, "action": "issue_details", "project": project, "id": id}
    values["ltoken"] = token
    if xsync is not None:
        values['include_xsync'] = xsync

    data = urllib.parse.urlencode(values)
    #print('data = {d}'.format(d = data))
    data = data.encode('ascii')
    #print(url)
    #req = urllib.request.Request(url, data)
    response = urllib.request.urlopen(url, data) 
    result = json.loads(response.read()) #response.read() returns bytes
    #print(result)
    #print('type = {t}'.format(t = type(result)))

    #result = []
    #for record in response:
        #print "R:" ,record
    #    result.append(json.loads(record))
  
    return result

"""
Get project list.
Input
url: url
user: user name
token: token needed for server uthenticaion
Output:
Dict list which contains detail of all projects
"""
def get_project_list(url, user, token):
    values = {"user": user, "action": "projects", "ltoken": token}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    response = urllib.request.urlopen(url, data) 
    
    r_bytes = response.read() #response.read() returns bytes

    #The bytes carries out the multi Json objects. It's easier to split those Jsons in string.
    r_string = r_bytes.decode("utf-8")
    r_list = r_string.splitlines()

    result = []
    for j in range(len(r_list)):
        result.append(json.loads(r_list[j]))
    
    #print('Search result: {r}'.format(r = r_list[0].find('WAVE3')))
    #print('type = {t}'.format(t = type(result[0])))
    #print(result)
    return  result