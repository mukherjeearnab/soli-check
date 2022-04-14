from django.shortcuts import render
from django.http import HttpResponse
from .forms import CheckBytecode

# Create your views here.


def index(response):
    if response.method == 'POST':
        form = CheckBytecode(response.POST)
        # check bytecode
        pass
    else:
        form = CheckBytecode()
    return render(response, 'main/check.html', {'form': form})
