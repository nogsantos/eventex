from django.shortcuts import render


def home(request):
    base_url = 'http://hbn.link/'
    speakers = [
        {'name': 'Grace Hopper', 'photo': base_url + 'hopper-pic'},
        {'name': 'Alan Turing', 'photo': base_url + 'turing-pic'},
    ]
    return render(request, 'index.html', {'speakers': speakers})
