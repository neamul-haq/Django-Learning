from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.

def add_post(request):
    if request.method == 'POST': 
        post_form = forms.PostForm(request.POST) # user er post request data ekhane capture korlam
        if post_form.is_valid(): # post kora data gula amra valid kina check kortechi
            post_form.save() # jodi data valid hoy taile database e save korbo
            return redirect('add_post')
    
    else: # user normally website e gele blank form pabe
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form' : post_form})


def edit_post(request, id):
    post = models.Post.objects.get(pk=id) 
    post_form = forms.PostForm(instance=post)
    # print(post.title)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post) 
        if post_form.is_valid(): 
            post_form.save()
            return redirect('homepage') 
    
    return render(request, 'add_post.html', {'form' : post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id) 
    post.delete()
    return redirect('homepage')