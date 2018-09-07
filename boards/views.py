from django.shortcuts import render,redirect,get_object_or_404
from .models import  Board,Topic,Post

from django.contrib.auth.models import User

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method=='POST':
        subject=request.POST['subject']
        message=request.POST['message']

        user=User.objects.first()

        topic=Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )
        post=Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )
        return redirect('board_topics',pk=board.pk)
    return render(request, 'new_topic.html', {'board': board})


def home(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})
def board_topics(request,pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html',{'board':board})

