from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostModelForm


def blog_post_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_list_page(request):
    # Models have an objects attr. We can add filters to it with ModelManager

    # We can also call BlogPost.objects.all().recent() because of custom querrysets
    qs = BlogPost.objects.recent()

    template_name = 'blog/list.html'
    context = {"objects": qs}
    return render(request, template_name, context)


def blog_post_delete_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_update_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = {"object": obj}
    return render(request, template_name, context)


@login_required(redirect_field_name='next')
def blog_post_create_page(request):
    # Using Django Form
    # form = BlogPostForm(request.POST or None)
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     # dictionary unacking
    #     obj = BlogPost.objects.create(**form.cleaned_data)
    #     form = BlogPostForm()

    # Using ModelForm
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()

    template_name = 'blog/create.html'
    context = {'form': form}
    return render(request, template_name, context)
