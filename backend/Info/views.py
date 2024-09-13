from django.shortcuts import render
from pymongo import MongoClient
import os

# Connecting to Mongo
Mongo_url = os.getenv('mongo')
client = MongoClient(Mongo_url)
db = client["NFC"]
convo = db["USER DATA"]


def addictions(request):
    return render(request, 'Addictions.html')

def Aboutus(request):
    return render(request, 'Aboutus.html')

def progress(request):
    if 'userid' in request.session:
            user_id = request.session['userid']
    Rehab = convo.find_one({'userid':user_id}, {'Rehab_Plan': True, '_id': False})
    # Extract the rehabilitation plan
    rehab_plan = Rehab.get('Rehab_Plan', 'No rehabilitation plan available.')
        
    # Prepare the context for rendering the template
    context = {
            'rehab_plan': rehab_plan
        }
    return render(request, 'progress.html', context)