from django.db import models


class Post(models.Model):

    titulo = models.CharField(max_length=200)

    autor = models.CharField(max_length=100)

    email = models.EmailField()

    conteudo = models.TextField()

    likes = models.PositiveIntegerField(default=0)

    dislikes = models.PositiveIntegerField(default=0)

    criado_em = models.DateTimeField(auto_now_add=True)

    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo