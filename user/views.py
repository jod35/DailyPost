from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

posts=[
    {
        "author":"Ssali Jonathan",
        "title":"Bored In the House",
        "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsa corrupti sint at consequuntur ab non! Aliquam est, pariatur quae explicabo possimus sequi Quaerat iure veniam dolores! Totam impedit explicabo recusandae!"
    }
    ,
      {
        "author":"Nassali Jannet",
        "title":"How to make an apple cake",
        "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsa corrupti sint at consequuntur ab non! Aliquam est, pariatur quae explicabo possimus sequi Quaerat iure veniam dolores! Totam impedit explicabo recusandae!"
    },
      {
        "author":"Mirembe Jerusha",
        "title":"5 ways to control spread of Corona Virus",
        "content":"Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsa corrupti sint at consequuntur ab non! Aliquam est, pariatur quae explicabo possimus sequi Quaerat iure veniam dolores! Totam impedit explicabo recusandae!"
    }
]

def index(request):
    context={"posts":posts,"title":"Home Page"}
    return render(request,'user/index.html',context)


def about(request):
    return render(request,'user/about.html')


def login(request):
    return render(request,'user/login.html')


def signup(request):
    form=UserCreationForm()

    if request.method == 'POST': #if we have a Post request
        form=UserCreationForm(request.POST) #passing into a new instance

        if form.is_valid():
            form.save()
            #login
            return redirect('user_home')

    else:
        form=UserCreationForm()

        
    context={
        'form':form,
        'title':"Create an Account"
    }  
    return render(request,'user/signup.html',context)
