from django.db import models

class Livros(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=20)
    idioma = models.CharField(max_length=15)

    def __str__(self):
        return self.titulo
