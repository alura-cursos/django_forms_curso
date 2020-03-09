from django.db import models
from django.utils.translation import gettext_lazy as _

class ClasseViagem(models.TextChoices):
    ECONOMICA = 'ECONOMICA', _('Econômica')
    EXECUTIVA = 'EXECUTIVA', _('Executiva')
    PRIMEIRA_CLASSE = 'PRIMEIRA_CLASSE', _('Primeira classe')