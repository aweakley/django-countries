from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    """
    International Organization for Standardization (ISO) 3166-1 Country list
    
    * ``iso`` = ISO 3166-1 alpha-2
    * ``name`` = Official country names used by the ISO 3166/MA in capital letters
    * ``printable_name`` = Printable country names for in-text use
    * ``iso3`` = ISO 3166-1 alpha-3
    * ``numcode`` = ISO 3166-1 numeric
    """
    iso = models.CharField(_('ISO alpha-2'), max_length=2, primary_key=True)
    name = models.CharField(_('Official name (CAPS)'), max_length=128)
    printable_name = models.CharField(_('Country name'), max_length=128)
    iso3 = models.CharField(_('ISO alpha-3'), max_length=3, null=True)
    numcode = models.PositiveSmallIntegerField(_('ISO numeric'), null=True)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ('name',)

    def __unicode__(self):
        return self.printable_name

