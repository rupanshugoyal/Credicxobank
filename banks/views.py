#for loading the dataset,
import pandas as pd

from django.shortcuts import render
from django.http import HttpResponse
from .models import banks, bank_branches
from .forms import IFSCForm, BANKSForm

def index(request):    
    if request.method == "GET":        
        return render(request, "index.html" , {"result": False})
    
    elif request.method == "POST":
        if request.POST.dict()["FORMNAME"] == "IFSC":
            form1 = IFSCForm(request.POST)
    
            if form1.is_valid():
                num = form1.cleaned_data['IFSC']
                details = bank_branches.objects.filter(ifsc=num)
                if(len(details) != 0):
                    return render(request, "index.html" , {"query_results":details, "result": True})
            return render(request, "index.html", {"result": False})
        
        elif request.POST.dict()["FORMNAME"] == "BANK":
            form1 = BANKSForm(request.POST)
            if form1.is_valid():
                bname = form1.cleaned_data["BANKNAME"]
                cityname = form1.cleaned_data["CITYNAME"]
                details = bank_branches.objects.filter(bank_name = bname, city = cityname)
                if(len(details) != 0):
                    return render(request, "index.html" , {"query_results":details, "result": True})
            return render(request, "index.html", {"result": False})
            
            
def load_dataset(request):
    return HttpResponse("loaded")