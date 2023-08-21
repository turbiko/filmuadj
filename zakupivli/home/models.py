from django.db import models
from django.utils.translation import activate, gettext_lazy as _, get_language

from wagtail.models import Page


class HomePage(Page):
    subpage_types = ['announcement.Announcement']
    page_description = _("announcements index page")

    def get_context(self, request):
        context = {}
        all_items = self.get_children().live()
        print("all items: ", all_items)

        context['announcements'] = all_items
        return context

    content_panels = Page.content_panels + []
