from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .forms import NewsForm, CommentForm
from users.models import Profile
from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Comment

from django.shortcuts import render
from scores .models import Match

def match_list(request):
    # Получаем все матчи из базы данных
    matches = Match.objects.all().order_by('timestamp')  # Можно отсортировать по дате или другим полям
    return render(request, 'news/match_list.html', {'matches': matches})

class tokenAuth(APIView):
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]

def news_list(request):
    news = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news': news})

from django.shortcuts import render, get_object_or_404
from .models import News
from .forms import CommentForm

def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    comments = news_item.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news_item
            comment.author = request.user
            comment.save()
            return redirect('news_detail', news_id=news_id)
    else:
        form = CommentForm()

    return render(request, 'news/new_detail.html', {
        'news': news_item,
        'comments': comments,
        'form': form
    })


def check_role(user, role):
    profile = getattr(user, 'profile', None)
    return profile and profile.role == role

@login_required
@user_passes_test(lambda u: check_role(u, 'journalist'))
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/create_news.html', {'form': form})

@login_required
@user_passes_test(lambda u: check_role(u, 'journalist'))
def edit_news(request, news_id):
    news = get_object_or_404(News, id=news_id, author=request.user)

@login_required
@user_passes_test(lambda u: check_role(u, 'journalist'))
def edit_news(request, news_id):
    news = get_object_or_404(News, id=news_id, author=request.user)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news)
    return render(request, 'news/edit_news.html', {'form': form})

@login_required
@user_passes_test(lambda u: check_role(u, 'journalist'))
def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id, author=request.user)
    news.delete()
    return redirect('news_list')