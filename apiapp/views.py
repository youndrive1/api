from django.shortcuts import render,get_object_or_404, redirect
from .forms import BoardForm, CommentForm
from .models import Board, Comment
from django.utils import timezone

# Create your views here.

def post(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit = False)
            board.update_date = timezone.now()
            board.save()
            return redirect('show')
    else:
        form = BoardForm()
        return render(request,'post.html', {'form':form})

def edit(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit = False)
            board.update_date = timezone.now()
            board.save()
            return redirect('show')
    else:
        form = BoardForm(instance=board)
        return render(request,'post.html', {'form':form})

        
def show(request):
    boards = Board.objects.order_by('-id') #최신순정렬
    return render(request, 'show.html',{'boards':boards})

def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        comment_form.instance.blog_id = board_id
        if comment_form.is_valid():
            comment = comment_form.save()
    comment_form = CommentForm()
    comments = board_detail.comments.all()
    return render(request, 'detail.html', {'board':board_detail, 'comments':
    comments, 'comment_form': comment_form})

def delete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('show')