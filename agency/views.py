from django.shortcuts import render

# Create your views here.
# Function Views
def home(request):
    context = {
        'cars': ['C1','C2','C3']
    }
    return render(request, 'agency/home.html', context)