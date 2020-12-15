from django.shortcuts import redirect


def login_required(func):
    def inner(request,*args,**kwargs):
        if request.session.get('email'):
            return func(request,*args,**kwargs)
        else:
            return redirect('/')
    return inner