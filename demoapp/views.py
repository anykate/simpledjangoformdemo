from django.shortcuts import render, redirect
from .forms import NameForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        # checking the form is valid or not
        if form.is_valid():
            # if valid rendering new view with values
            # the form values contains in cleaned_data dictionary
            return render(request, 'demoapp/success.html', {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
            })
    else:
        # Create a new form
        form = NameForm()

    return render(request, 'demoapp/index.html', {'form': form})


def success(request):
    if request.method == 'POST':
        # print('*' * 80)
        # print(request.POST)
        # print('*' * 80)
        return render(request, 'demoapp/success.html',
                      {'fname': request.POST['first_name'], 'lname': request.POST['last_name']})
    else:
        return redirect('/')
