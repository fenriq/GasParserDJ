from django.shortcuts import render
from .scripts.liner import liner


# Create your views here.
def index(request):
    data = liner()
    context = {
        'ai92': data["ai92"],
        'ai95': data["ai95"],
        'ai98': data["ai98"],
    }
#    ai92 = data['ai92']
#    ai95 = data['ai95']
#    ai98 = data['ai98']
    return render(request, "index.html", context)


#def gas_view(request):
#    data = liner()
#    ai92 = data['ai92']
#    ai95 = data['ai95']
#    ai98 = data['ai98']
#    return render(request, 'index', {'ai92': ai92, 'ai95': ai95, 'ai98': ai98})