from django import template
from ..models import Post
from django.db.models import Count
from django.urls import reverse


register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=3):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]

@register.simple_tag
def anchor(url_name, section_id_):
    return reverse(url_name) + '+' + section_id

@register.inclusion_tag('blog/post/about.html')
def about_me_post():
    about=Post.objects.filter(title='about_me').order_by()
    return {'about': about}

@register.simple_tag
def get_about_me_post():
    return Post.objects.filter(title__exact='about_me')