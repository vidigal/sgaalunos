from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Curso(models.Model):
    nome = models.CharField(_('Nome'), max_length=100)
    descricao = models.TextField(_('Descrição'), max_length=500)
    carga_horaria = models.IntegerField(_('Carga Horária'))

    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')

    def __str__(self):
        return self.nome