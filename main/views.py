from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Football Station',
        'name': 'Levina Aurellia',
        'class': 'PBP D',
        'npm': '2406356776'
    }

    return render(request, "main.html", context)