from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

# notify.send(actor, recipient, verb, action_object, target, level, description, public, timestamp, **kwargs)
