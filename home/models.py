from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import (
    FieldPanel,
)

class HomePage(Page):   
    body = RichTextField(blank=True)
    
    parent_page_types = ['wagtailcore.Page']

    subpage_types = [
        'scoring.AgeGroupPage',
        'scoring.ArcherPage',
        'scoring.CategoryMembershipPage',
        'scoring.CategoryPage',
        'scoring.ClubMembershipPage',
        'scoring.ClubPage',
        'scoring.CompetitionMembershipPage',
        'scoring.CompetitionPage',
        'scoring.DisciplineMembershipPage',
        'scoring.DisciplinePage',
        'scoring.RoundMembershipPage',
        'scoring.RoundPage',
        'scoring.ScorePage',
        'scoring.ScoringSheetPage',
        'scoring.TargetFaceNameChoicePage',
        'scoring.TargetFacePage',
        'scoring.TeamMembershipPage',
        'scoring.TeamPage',
    ]

    # content_panels = Page.content_panels + ["body"]
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    # @classmethod
    # def can_create_at(cls, parent):
    #     # You can only create one of these!
    #     return super(HomePage, cls).can_create_at(parent) \
    #         and not cls.objects.exists()
