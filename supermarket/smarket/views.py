from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import SmarketUsers
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')  # to render signin.html file as defined in urls.py [ path('signin', views.signin, name='signin'),]

def homepage(request):
    return render(request, 'homepage.html')

def delete(request):
    return render(request, 'delete.html')

def update(request):
    return render(request, 'update.html')

def create_user(request): # in request have fd data
    try:
            Smarket_user_record = SmarketUsers()
            un = request.POST.get('username', 'dummyusername')
            pwd = request.POST.get('password', 'dummypassword')
            em = request.POST.get('email', 'dummyemail')
            # Smarket_user_record = SmarketUsers.objects.create
            # (
            # username=un,
            # password=pwd,
            # email=em
            # )
            Smarket_user_record.username=un
            Smarket_user_record.password=pwd
            Smarket_user_record.email=em
            Smarket_user_record.save()
            data = {"status_code":"your account created successfully with the name:"+un }
            payload = {
                'usersignupresponse': data
            }
    except:
       
        data = {"status_code":"error in account creation"}
        payload = {
            'usersignupresponse': data
        }
    return JsonResponse(payload)

def signin_user(request):   # to capture and verify the entered username and password  against user table entry
    currentLineNumber=0
    text_message = "empty"
    try:
            currentLineNumber = 1
            Smarket_user_record = SmarketUsers()
            currentLineNumber = 2
            un_em = request.POST.get('username_or_email', 'dummyusername_dummyemail')
            currentLineNumber = 3
            pwd = request.POST.get('password', 'dummypassword')
            currentLineNumber = 4
          
         
            if SmarketUsers.objects.filter(username=un_em).count()>0 :
                currentLineNumber = 5
                Smarket_user_record= SmarketUsers.objects.get(username=un_em)
                currentLineNumber = 6
                text_message= Smarket_user_record.password
                currentLineNumber = 15
                if Smarket_user_record.password==pwd:
                    currentLineNumber = 7
                     
                    data = {"status_code":"1","status_message":"signin success"}
                    currentLineNumber = 8
                    payload = {
                    'usersignupresponse': data
                 }
                    return JsonResponse(payload)
                else:
                    currentLineNumber = 9
                    data = {"status_code":"0","status_message":"signin failed"}
                    payload = {
                    'usersignupresponse': data
                    }
                    return JsonResponse(payload)
            else:
                currentLineNumber = 10
                data = {"status_code":"0","status_message":"username wrong and not available"}
                payload = {
                'usersignupresponse': data
                }
                return JsonResponse(payload)
                         
    
    except:
       
        data = {"status_code":"error in account creation","currentLineNumber":currentLineNumber, "text_message":text_message+","+un_em  }
        payload = {
            'usersignupresponse': data
        }
    return JsonResponse(payload)



def delete_user(request):
    currentLineNumber=0
    text_message = "empty"
    try:
            currentLineNumber = 1
            Smarket_user_record = SmarketUsers()
            currentLineNumber = 2
            un_em = request.POST.get('username_or_email', 'dummyusername_dummyemail')
            currentLineNumber = 3
            
            currentLineNumber = 4
          
         
            if SmarketUsers.objects.filter(username=un_em).count()>0 :
                currentLineNumber = 5
                Smarket_user_record= SmarketUsers.objects.get(username=un_em)
                currentLineNumber = 6
                Smarket_user_record.delete()
                
                data = {"status_code":"1","status_message":"record deleted success"}
                payload = {
                'usersignupresponse': data
                }
                return JsonResponse(payload)
            else:
                currentLineNumber = 10
                data = {"status_code":"0","status_message":"username "+un_em+" is wrong and not available , cannot delete"}
                payload = {
                'usersignupresponse': data
                }
                return JsonResponse(payload)
                         
    
    except:
       
        data = {"status_code":"error in account creation","currentLineNumber":currentLineNumber, "text_message":text_message+","+un_em  }
        payload = {
            'usersignupresponse': data
        }
    return JsonResponse(payload)



def update_user(request):
    currentLineNumber=0
    text_message = "empty"
    try:
            currentLineNumber = 1
            Smarket_user_record = SmarketUsers()
            currentLineNumber = 2
            un_em = request.POST.get('username_or_email', 'dummyusername_dummyemail')
            currentLineNumber = 3
            pwd = request.POST.get('password', 'dummypassword')
            currentLineNumber = 4
          
         
            if SmarketUsers.objects.filter(username=un_em).count()>0 :
                currentLineNumber = 5
                Smarket_user_record= SmarketUsers.objects.get(username=un_em)
                currentLineNumber = 6
                Smarket_user_record.password=pwd
                Smarket_user_record.save()
                
                data = {"status_code":"1","status_message":"record updated success"}
                payload = {
                'usersignupresponse': data
                }
                return JsonResponse(payload)
            else:
                currentLineNumber = 10
                data = {"status_code":"0","status_message":"username "+un_em+" is wrong and not available , cannot update"}
                payload = {
                'usersignupresponse': data
                }
                return JsonResponse(payload)
                         
    
    except:
       
        data = {"status_code":"error in account creation","currentLineNumber":currentLineNumber, "text_message":text_message+","+un_em  }
        payload = {
            'usersignupresponse': data
        }
    return JsonResponse(payload)


