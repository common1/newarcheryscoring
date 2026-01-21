from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField


class HomePage(Page):   
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + ["body"]

    # @classmethod
    # def can_create_at(cls, parent):
    #     # You can only create one of these!
    #     return super(HomePage, cls).can_create_at(parent) \
    #         and not cls.objects.exists()
