from django import forms


class CheckBytecode(forms.Form):
    bytecode = forms.CharField(
        label='Enter Bytecode of Smart Contract', max_length='20480', widget=forms.Textarea)
