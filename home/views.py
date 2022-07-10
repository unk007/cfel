from django.shortcuts import render
from users.models import search_user_with_domain

# Create your views here.
def homepage(request):
    user_info = {}
    try:
        unkid = request.COOKIES['unkid']  
        user_info = search_user_with_domain(unkid)
    except:
        pass
    data = {}
    if user_info:
        pass
    data = {
        'user' : user_info.users if user_info else 0,  
    }
    return render(request, 'homepage.html', data)