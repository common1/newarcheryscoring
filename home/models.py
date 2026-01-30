from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import (
    FieldPanel,
)

class HomePage(Page):   
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
        'scoring.ScoringPage',
        'scoring.ScoringSheetPage',
        'scoring.TargetFaceNameChoicePage',
        'scoring.TargetFacePage',
        'scoring.TeamMembershipPage',
        'scoring.TeamPage',
    ]

    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    body = RichTextField(blank=True)

    # content_panels = Page.content_panels + ["body"]
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
    ]

    # @classmethod
    # def can_create_at(cls, parent):
    #     # You can only create one of these!
    #     return super(HomePage, cls).can_create_at(parent) \
    #         and not cls.objects.exists()
