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
    transcode = {
        "id" :      detail.get('id'),
        "code":     detail.get('code'),
        "name":     detail.get('name'),
        "location": detail.get('location'),
        "build":    detail.get('build'),
        "severity": detail.get('severity'),
        "owner":    detail.get('owner'),
        "state":    detail.get('state'),
        "status":   detail.get('status')
    }

    #Only the last comment in history is intereted
    history = detail.get('history') #history is list of dict
    last = len(history) - 1
    last_history = history[last]
    comment = last_history.get('comment')

    transcode["comment"] = comment
    
    #print(transcode)
    return transcode