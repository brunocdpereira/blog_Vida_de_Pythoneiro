from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "novo/",
        views.criar_post,
        name="criar_post"
    ),

    path(
        "editar/<int:id>/",
        views.editar_post,
        name="editar_post"
    ),

    path(
        "deletar/<int:id>/",
        views.deletar_post,
        name="deletar_post"
    ),

    path(
        "like/<int:id>/",
        views.like_post,
        name="like_post"
    ),

    path(
        "dislike/<int:id>/",
        views.dislike_post,
        name="dislike_post"
    ),
]