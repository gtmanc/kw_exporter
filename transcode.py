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

    #Only the last comment in history is intereted
    history = detail.get('history') #history is list of dict
    last = len(history) - 1
    last_history = history[last]
    comment = last_history.get('comment')
    #print('Comment type = {t}'.format(t = type(comment)))
    #print('Comment = {t}'.format(t = comment))
    coded.update({"Comment":comment})
    #print(coded)
    return coded