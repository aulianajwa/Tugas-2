from django import forms
from todolist.models import Task

class Task_Form(forms.ModelForm) :
    class Meta :
        model = Task
        fields = ['title','description']
    
    title_attrs ={
        'type' : 'text',
        'placeholder' :'Title',
        'class' : 'form-control'
    }
    desc_attrs = {
        'type' : 'text',
        'placeholder' : 'Description',
        'class' : 'form-control'
    }
    title = forms.CharField(label="Title", required=True, max_length=50,widget=forms.TextInput(attrs=title_attrs))
    description = forms.CharField(label="Description",required=True,max_length=50,widget=forms.TextInput(attrs=desc_attrs))