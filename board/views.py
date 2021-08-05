from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from django.utils import timezone
from .forms import BoardForm
from django.core.paginator import Paginator
from django.core.mail import EmailMessage, send_mail
# Create your views here.

def home(request):
    allPost = Board.objects.all()
    board_list = Board.objects.all()
    paginator = Paginator(board_list, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'allPost': allPost, 'posts':posts})

def detail(request, id):
    boardPost = get_object_or_404(Board, pk = id)
    return render(request, 'detail.html', {'boardPost': boardPost})
    
def new(request):
  if request.method == 'POST':
    form = BoardForm(request.POST, request.FILES)
    if form.is_valid():
      new_post = form.save(commit=False)
      new_post.upload_date = timezone.now()
      new_post.author = request.user
      new_post.save()
      return redirect('board:detail', new_post.id)
    return redirect('home')
  else:
    form = BoardForm()
    return render(request, 'new.html', {'form': form})
    

def edit(request, id):
  post = get_object_or_404(Board, pk = id)
  if request.method == 'GET': 
    board_form = BoardForm(instance = post)
    return render(request, 'edit.html', {'edit_form':board_form})
  else: 
    board_form = BoardForm(request.POST, request.FILES, instance = post)
    if board_form.is_valid():
      edit_post = board_form.save(commit=False)
      edit_post.upload_date = timezone.now()
      edit_post.save()
    return redirect('/board/post/'+str(id))


def delete(request, id):
  delete_post = Board.objects.get(id = id)
  delete_post.delete()
  return redirect('home')


def sendmail(request):
  # email = EmailMessage(
  #     'Hello',                # 제목
  #     'Body goes here hello ggg',       # 내용
  #     'from@gmail.com',     # 보내는 이메일 (settings에서 설정해서 작성안해도 됨)
  #     to=['sigan0826@likelion.org'],  # 받는 이메일 리스트
  # )
  # email.send()
  if request.method == 'GET': 
      return render(request, 'sendmail.html')
  else:
    send_mail(
      subject=request.POST.get('title'), 
      message=request.POST.get('body'), 
      from_email="sample@gmail.com", 
      recipient_list=[request.POST.get('email')], 
      html_message=None
    )
  return redirect('board:sendmail')