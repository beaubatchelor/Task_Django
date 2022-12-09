from django.shortcuts import render
from django.http import HttpResponse

test_data = {"_id":{"$oid":"5f0a6b880c689113c019b670"},
"user":"test_user",
"values_data":{"values_data" : [{"category":"Maslow","values":["Physiological Needs","Safety","Belongingness and Love","Esteem","Self Actualization"]},{"category":"Urgency","values":["Urgent","Neutral","Not Urgent"]},{"category":"Interest","values":["Technology","Wealth","Friendship","Health"]}]},
"org_data":{'org_data' : ["Life","Work","Project"]},
"task_data":{"columns":["Maslow","Urgency","Interest","Due Date","Task","Status (Optional)","Assigned To (Optional)"],
"values":[["Esteem","Netral","Health","2099-7-8","Creat a workout schedule","not started","Beau"],["Physiological Needs","Urgent","Health","2020-8-1","Groceries","not started","Beau"],["Belongingness and Love","Neutral","Friendship","2020-12-4","420Bot","not started","Beau"],["Saftey","Neutral","Health","2020-8-1","Pay Rent","not started","Beau"]]}}


def index(request):
    return render(request, 'index.html', {'name' : 'Beau'})

def organizations(request):
    # user_data = mongo.db.User.find_one({'user': 'test_user'}) ##production data
    user_data = test_data ##for test data
    org_data = user_data['org_data']
    

    return render(request, 'organization.html', org_data)

def values(request):
    # user_data = mongo.db.User.find_one({'user': 'test_user'}) ##production data
    user_data = test_data ##for test data  
    values_data = user_data['values_data']

    return render(request, 'values.html', values_data)

def tasks(request):
    # user_data = mongo.db.User.find_one({'user': 'test_user'}) ##production data
    user_data = test_data ##for test data
    task_data = user_data['task_data']

    return render(request, 'tasks.html', task_data)

# def update():
#     result = request.get_json() ##JS request of table information 
#     user_data = mongo.db.User.find_one({'user': 'test_user'}) ##production data
#     user_data['values_data'] = result

#     mongo.db.User.replace_one({'user': 'test_user'}, user_data)

#     return redirect('/values')

