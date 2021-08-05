from django.contrib.auth.forms import UserModel
from django.core.checks import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Message
from django.utils import timezone
from .forms import MessageForm
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model

# Create your views here.
def home(request):
    messages = Message.objects.all()
    return render(request, 'index.html', {'messages':messages})

def detail(request, id):
    message = get_object_or_404(Message, pk = id)
    return render(request, 'detail2.html', {'message':message})

def new(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.upload_date = timezone.now()
            new_post.sender_id = request.user
            new_post.save()
            return redirect('messenger:detail', new_post.id)
        return redirect('messenger:home')
    else:
        form = MessageForm()
        return render(request, 'new2.html', {'form': form})