from django.shortcuts import render

# Landing Page/Routing View Page
def index(req):
    #Pass in the http request as well as the html template file to load
    return render(req,'community/index.html')



