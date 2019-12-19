coded = {
        "id" :  'id',
        "code": 'code',
        "name": 'name',
        "location": 'location',
        "build": 'build',
        "severity": 'severity',
        "owner":  'owner',
        "state":  'state',
        "status":  'status',
        "Comment": 'Comment'
        }
"""
Transcode the detail of an issue to the format we like.
This routine mainly extract the comment from the last entry in the histroy
Input:
detail: 
Dictionary of an issue

Output:
Transcoded dictionary
"""
def transcode(detail):
    #simply copy what we have
    coded.update({"id" : detail.get('id')})
    coded.update({"code": detail.get('code')})
    coded.update({"name": detail.get('name')})
    coded.update({"location": detail.get('location')})    
    coded.update({"build":    detail.get('build')})    
    coded.update({"severity": detail.get('severity')})    
    coded.update({"owner":    detail.get('owner')})    
    coded.update({"state":    detail.get('state')})    
    coded.update({"status":   detail.get('status')})    

    #Only the newest comment in history is intereted
    #Be careful, a history may contin empty comment. We have to find a good comment backward.
    #A history will be added to history list by klocwork server only if the status is changed
    history = detail.get('history') #history is list of dict
    #print('history: {h}'.format(h = history))
    for h in history:
        comment = h.get('comment')
        if len(comment) > 0:
            break
        print('empty comment!')
    #print('Comment length= {t}'.format(t = len(comment)))
    #print('Comment type = {t}'.format(t = type(comment)))
    #print('Comment = {t}'.format(t = comment))
    coded.update({"Comment":comment})
    #print(coded)
    return coded

"""
Select project according to the specified IDs (string)
Input:
list:   all available projects in server 
id_incl:string. A project contains this string will be added to the list 
id_excl: A project contains this string will NOT be added to the list
Note: operation "AND" is used. e.g. A project contains both will be ignored
Output:
project list in string
"""
def project_list(list, id_incl, id_excl):
    pj_name_list = []
    
    for i in range(len(list)):
        name = list[i].get('name')
        if name.find(id_incl) >= 0 and name.find(id_excl) < 0:
            pj_name_list.append(name)

    return pj_name_list
