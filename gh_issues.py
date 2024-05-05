from tasks.gh_integration import *
ish = fetch_all_issues("aradmschool")
for idd in ish:
    print("*"*100)
    for i in idd:
        print(f"{i}:{idd[i]}")
        print("-"*100)
        if i == 'events_url':
            print("?"*100)
            print(fetch_all_events(idd[i]))

""" 
# post if

assignees and assignee are not fields?

# fields we should post

[title](html_url)





"""
