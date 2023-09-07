from django.db import models
from django.utils.translation import activate, gettext_lazy as _, get_language
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import RichTextField

from .filetools import filename_creation


def class_folder(instance, filename):
    create_name = filename_creation(instance, filename)
    return f"adv/{create_name}"


class Announcement(Page):
    body = RichTextField(blank=True)
    date_start = models.DateField(verbose_name=_('Початок'), auto_now_add=False, blank=True, null=True, )
    date_end = models.DateField(verbose_name=_('Закінчення'), auto_now_add=False, blank=True, null=True, )
    time_end = models.TimeField(verbose_name=_('Час закінчення подачі'), blank=True, null=True)
    template_document = models.FileField(upload_to=class_folder, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('date_start'),
        FieldPanel('date_end'),
        FieldPanel('time_end'),
        FieldPanel('template_document'),
    ]

    def __str__(self):
        return f"({self.id}) {self.title} "

