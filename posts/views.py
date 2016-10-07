from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import Context, loader
from django.views.defaults import page_not_found
from django.http import HttpResponse
import json
from .models import Posts
from .forms import CommentForm


# Create your views here.
def index(request):
    posts = Posts.objects.all()
    for post in posts:
        post.post_text = post.post_text[:400] + '.....'
    return render(request, 'post/index.html', {'posts': posts})


def showmore(request, post_url):
    if request.method == 'GET':
        post = get_object_or_404(Posts, post_url=post_url)
        post.post_views += 1
        post.save()
        return render(request, 'post/show_more.html', {'post': post})


def support(request):
    response_data = {}
    if request.method == 'POST':
        if request.is_ajax():
            post_id = request.POST.get('post_id')
            liked = request.POST.get('liked')
            post = Posts.objects.get(post_id=post_id)
            post.post_likes += 1
            post.save()
            response_data = {'status': 'success', 'data': post.post_likes}
        else:
            response_data = {'status': 'failure', 'message': 'not liked'}

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def comment_model(request):
    form = CommentForm()
    return render(request, 'post/comment_modal.html', {'form': form})


def comment(request):
    response_data = {'status': 'error', 'message': 'invalid data'}
    if request.method == 'POST':
        if request.is_ajax():
            post_id = request.POST.get('post_id')
            form = CommentForm(request.POST)
            if form.is_valid():
                name = form['name'].value()
                email_id = form['email_id'].value()
                comment_text = form['comment_text'].value()
                post = Posts.objects.get(post_id=post_id)
                post.comments_set.create(
                    commented_by=name,
                    commenter_mail_id=email_id,
                    comment_text=comment_text,
                )
                return render(request, 'post/comment.html', {'post': post})
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def error_500(request):
    return render(request,'post/500.html', status=500)


def custom_404(request):
    return render(request,'post/404.html',status=404)

# Create your views here.
