from django.shortcuts import render

def home(request):
    template_name = "index.html"
    content = {"name":"Anooz Nepal"}
    return render(request,template_name,content)