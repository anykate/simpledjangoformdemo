from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'demoapp/index.html', {})


def success(request):
    if request.method == 'POST':
        # print('*' * 80)
        # print(request.POST)
        # print('*' * 80)
        return render(request, 'demoapp/success.html',
                      {'fname': request.POST['first_name'], 'lname': request.POST['last_name']})
    else:
        return redirect('/')
