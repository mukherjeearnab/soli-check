from django.shortcuts import render
from django.http import HttpResponse
from .forms import CheckBytecode

# Create your views here.


def index(response):
    if response.method == 'POST':
        form = CheckBytecode(response.POST)
        # check bytecode
        if form.is_valid():
            bytecode = form.cleaned_data['bytecode']
            if bytecode == 'hello':
                result = True
            else:
                result = False
    else:
        result = None
        form = CheckBytecode()
    return render(response, 'main/check.html', {'form': form, 'result': result})
