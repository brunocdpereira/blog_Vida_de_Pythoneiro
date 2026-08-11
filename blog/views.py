from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostForm


def home(request):

    posts = Post.objects.all().order_by("-criado_em")

    return render(
        request,
        "blog/index.html",
        {"posts": posts}
    )


def criar_post(request):

    if request.method == "POST":

        form = PostForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("home")

    else:

        form = PostForm()

    return render(
        request,
        "blog/post_form.html",
        {"form": form}
    )


def editar_post(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == "POST":

        form = PostForm(
            request.POST,
            instance=post
        )

        if form.is_valid():

            form.save()

            return redirect("home")

    else:

        form = PostForm(instance=post)

    return render(
        request,
        "blog/post_form.html",
        {
            "form": form,
            "post": post
        }
    )


def deletar_post(request, id):

    post = get_object_or_404(Post, id=id)

    if request.method == "POST":

        post.delete()

        return redirect("home")

    return render(
        request,
        "blog/post_confirm_delete.html",
        {"post": post}
    )


def like_post(request, id):

    post = get_object_or_404(Post, id=id)

    post.likes += 1

    post.save()

    return redirect("home")


def dislike_post(request, id):

    post = get_object_or_404(Post, id=id)

    post.dislikes += 1

    post.save()

    return redirect("home")