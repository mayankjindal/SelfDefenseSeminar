from django.shortcuts import render
from seminar.models import Register
import pandas as pd

def register(request):
    registered = False
    context = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        loc = request.POST.get('loc')
        if loc == '1':
            loc = 'Safdarjung Enclave, South Delhi'
        elif loc == '2':
            loc = 'Vikaspuri, West Delhi'
        elif loc == '3':
            loc = 'Gurgaon'
        elif loc == '4':
            loc = 'Noida'
        elif loc == '5':
            loc = 'Chandigarh'
        reg = Register(id=None, name=name, age=age, contact=contact, email=email, preferred_location=loc)
        reg.save()

        data_list = [name, age, contact, email, loc]
        data = pd.read_csv("./seminar/static/seminar/data.csv")
        data.loc[len(data)] = data_list
        data.to_csv("./seminar/static/seminar/data.csv")

    return render(request, 'seminar/register.html', context)

