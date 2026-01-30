import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from django.core.validators import MaxValueValidator, MinValueValidator

from userauth.models import CustomUser

from modelcluster.models import ClusterableModel

from django.contrib.contenttypes.fields import GenericRelation
from wagtail.admin.panels import PublishingPanel
from wagtail.models import (
    DraftStateMixin, 
    RevisionMixin, 
    LockableMixin,
    PreviewableMixin,
)

from common.blocks import (
    TableBlock_3_Cols_10_Rows,
    TableBlock_3_Cols_12_Rows,
    TableBlock_5_Cols_5_Rows,
)

from wagtail.snippets.models import register_snippet

class BaseScoringModel(ClusterableModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

# TODO: Supercharging Archer Snippet with Advanced Features
class Archer(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    last_name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Last name"),
        help_text=_("format: required, max-64")
    )
    first_name = models.CharField(
        max_length=32,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("First name"),
        help_text=_("format: required, max-32")
    )
    middle_name = models.CharField(
        max_length=6,
        null=True,
        unique=False,
        blank=True,
        verbose_name=_("Middle name"),
        help_text=_("format: not required, max-6")
    )
    slug = AutoSlugField(populate_from='last_name',editable=True)
    archer_image = models.ForeignKey(
        'wagtailimages.Image', 
        null=True, 
        blank=True,
        on_delete=models.SET_NULL, 
        related_name='+'
    )
    union_number = models.PositiveIntegerField(
        unique=True,
        null=True,
        blank=False,
        verbose_name=_("Union number"),
        help_text=_("format: not required")
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("Author"),
        related_name='archer_author',
        help_text=_("format: not required, default=1 (superuser)"),
    )

    # Contact information
    
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Email"),
        help_text=_("format: not required, max-254")
    )
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Phone number"),
        help_text=_("format: not required, max-15")
    )
    address = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Address"),
        help_text=_("format: not required, max-128")
    )
    city = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("City"),
        help_text=_("format: not required, max-64")
    )
    zip_code = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Zip code"),
        help_text=_("format: not required, max-6")
    )
    province = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Province"),
        help_text=_("format: not required, max-64")
    )

    # Contact information end

    # Extra fields for archer information

    birth_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("Birth date"),
        help_text=_("format: Y-m-d, not required"),
    )
    
    # Extra fields for archer information end
       
    class Meta:
        db_table = 'archers'
        ordering = ['last_name']
        verbose_name = _("Archer")
        verbose_name_plural = _("Archers")

    def __str__(self):
        s_middle_name = ""
        if self.middle_name:
            s_middle_name = self.middle_name
        return f"{self.last_name} {self.first_name} {s_middle_name}"

    def __unicode__(self):
        s_middle_name = ""
        if self.middle_name:
            s_middle_name = self.middle_name
        return f"{self.last_name} {self.first_name} {s_middle_name}"

# Target Archery
# Indoor Archery
# Field Archery
# 3D Archery
# Flight Archery
# Clout Archery
# Ski Archery
# Para Archery
# Run archery
# Bowhunting

# TODO: Supercharging Discipline Snippet with Advanced Features
class Discipline(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = models.CharField(
        max_length=64,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("Name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(
        populate_from='name',
        editable=True
    )
    archers = models.ManyToManyField(
        Archer,
        through='DisciplineMembership',
        blank=True,
        help_text=_("format: not required"),
        related_name='discipline_archers',
        verbose_name=_("Archers"),
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='discipline_author',
        verbose_name=_("Author"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'disciplines'
        ordering = ['name']
        verbose_name = _("Discipline")
        verbose_name_plural = _("Disciplines")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

# TODO: Supercharging DisciplineMembership Snippet with Advanced Features
class DisciplineMembership(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    discipline = models.ForeignKey(
        Discipline,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("Discipline"),
        help_text=_("format: required"),
        related_name='disciplinememberships'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("Archer"),
        help_text=_("format: required"),
        related_name='archer_disciplinemembership'
    )
    slug = AutoSlugField(populate_from=('archer__last_name', 'discipline__name'), editable=True)
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='discipline_membership_author',
        verbose_name=_("Author"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'disciplinememberships'
        ordering = ['discipline__name']
        verbose_name = _("Discipline Membership")
        verbose_name_plural = _("Discipline Memberships")

    def __str__(self):
        return f"{str(self.archer)} - {str(self.discipline)}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.discipline)}"

# TODO: Supercharging Club Snippet with Advanced Features
class Club(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._meta.get_field('slug').populate_from = 'name'

    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    address = models.CharField(
        max_length=128,
        null=True,
        unique=False,
        blank=True,
        verbose_name=_("Address"),
        help_text=_("format: not required, max-128")
    )
    zip_code = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Zip code"),
        help_text=_("format: not required, max-6")
    )
    town = models.CharField(
        max_length=64,
        null=True,
        unique=False,
        blank=True,
        verbose_name=_("Town"),
        help_text=_("format: not required, max-64")
    )
    archers = models.ManyToManyField(
        Archer,
        through='ClubMembership',
        blank=True,
        help_text=_("format: not required"),
        related_name='clubs',
        verbose_name=_("Archers"),
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='author_club',
        verbose_name=_("Author"),
        help_text=_("format: not required, default=1 (superuser)"),
    )

    # Extra fields for club information

    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Email"),
        help_text=_("format: not required, max-254")
    )
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Phone number"),
        help_text=_("format: not required, max-15")
    )
    website = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Website"),
        help_text=_("format: not required, max-200")
    )
    social_media = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Social media"),
        help_text=_("format: not required, max-128")
    )
     
    # Extra fields for club information end        
    
    class Meta:
        db_table = 'clubs'
        ordering = ['name']
        verbose_name = _("Club")
        verbose_name_plural = _("Clubs")

    def __str__(self):
        return self.name

    def __unicode__(self):       
        return self.name

# TODO: Supercharging ClubMembership Snippet with Advanced Features
class ClubMembership(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    club = models.ForeignKey(
        Club,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("Club"),
        help_text=_("format: required"),
        related_name='memberships'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("Archer"),
        help_text=_("format: required"),
        related_name='clubmember_archer'
    )
    slug = AutoSlugField(populate_from=('archer__last_name', 'club__name'), editable=True)
    start_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("Start date"),
        help_text=_("format: Y-m-d, not required"),
    )
    end_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("End date"),
        help_text=_("format: Y-m-d, not required"),
    )
    
    # Extra fields for membership information
    
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='membership_author',
        verbose_name=_("Author"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    # Extra fields for membership information end

    class Meta:
        db_table = 'clubmemberships'
        ordering = ['start_date']
        verbose_name = _("Club Membership")
        verbose_name_plural = _("Club Memberships")

    def __str__(self):
        return f"{str(self.archer)} - {str(self.club)} {self.club.town}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.club)} {self.club.town}"

# Olympic Recurve
# Compound
# Barebow
# Longbow
# Traditional
# TODO: Supercharging Category Snippet with Advanced Features
class Category(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._meta.get_field('slug').populate_from = 'name'
        
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    archers = models.ManyToManyField(
        Archer,
        through='CategoryMembership',
        blank=True,
        help_text=_("format: not required"),
        related_name='category_archers',
        verbose_name=_("Archers"),
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("Author"),
        related_name='category_author',
        help_text=_("format: required, default=1 (superuser)"),
    )
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

# TODO: Supercharging AgeGroup Snippet with Advanced Features
class AgeGroup(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._meta.get_field('slug').populate_from = 'name'

    name = models.CharField(
        max_length=32,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("Name"),
        help_text=_("format: required, max-32")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='agegroup_author',
        verbose_name=_("Author"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'agegroups'
        ordering = ['name']
        verbose_name = _("Age Group")
        verbose_name_plural = _("Age Groups")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

# TODO: Supercharging CategoryMembership Snippet with Advanced Features
class CategoryMembership(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("Category"),
        help_text=_("format: required"),
        related_name='categorymembership_category_items'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("Archer"),        
        related_name='categorymembership_archer_items',
        help_text=_("format: required"),
    )
    agegroup = models.ForeignKey(
        AgeGroup,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Age Group"),
        related_name='categorymembership_agegroup',
        help_text=_("format: required"),
    )

    # Extra fields for membership information

    slug = AutoSlugField(populate_from=('category__name', 'archer__last_name',), editable=True)
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='categorymembership_author',
        verbose_name=_("Author"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    # Extra fields for membership information end

    class Meta:
        db_table = 'categorymemberships'
        ordering = ['category__name']
        verbose_name = _("Category Membership")
        verbose_name_plural = _("Category Memberships")

    def __str__(self):
        return f"{str(self.archer)} - {str(self.category)}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.category)}"

# TODO: Supercharging Team Snippet with Advanced Features
class Team(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._meta.get_field('slug').populate_from = 'name'

    name = models.CharField(
        max_length=64,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("Name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name', editable=True)
    archers = models.ManyToManyField(
        Archer,
        through='TeamMembership',
        blank=True,
        help_text=_("format: not required"),
        related_name='team_archers',
        verbose_name=_("Archers"),
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='team_author',
        verbose_name=_("Author"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'teams'
        ordering = ['name']
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

# TODO: Supercharging TeamMembership Snippet with Advanced Features
class TeamMembership(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("Team"),
        help_text=_("format: required"),
        related_name='teammembership_team'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("Archer"),
        help_text=_("format: required"),
        related_name='teammembership_archer'
    )
    slug = AutoSlugField(
        populate_from=('team__name', 'archer__last_name',), 
        editable=True,
    )

    # Extra fields for teammembership information
    
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='teammembership_author',
        verbose_name=_("Author"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    # Extra fields for teammembership information end

    class Meta:
        db_table = 'teammemberships'
        ordering = ['team__name']
        verbose_name = _("Team Membership")
        verbose_name_plural = _("Team Memberships")

    def __str__(self):
        return f"{str(self.archer)} - {str(self.team)}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.team)}"
    
# TODO: Supercharging ScoringSheet Snippet with Advanced Features
class ScoringSheet(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("Name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    columns = models.PositiveIntegerField(
        unique=False,
        null=False,
        blank=False,
        default=3,
        validators=[MinValueValidator(3), MaxValueValidator(20)],
        verbose_name=_("Columns"),
        help_text=_("format: required min-3, max-20")
    )
    rows = models.PositiveIntegerField(
        unique=False,
        null=False,
        blank=False,
        default=10,
        validators=[MinValueValidator(3), MaxValueValidator(20)],
        verbose_name=_("Rows"),
        help_text=_("format: required min-3, max-20")
    )
        
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='scoringsheet_author',
        verbose_name=_("Author"),
        help_text=_("format: required, default=1 (superuser)"),
    )
    
    class Meta:
        db_table = 'scoringsheets'
        ordering = ['name']
        verbose_name = _("Scoring Sheet")
        verbose_name_plural = _("Scoring Sheets")

    def __str__(self):
        return f"{self.name} ( rows : {self.rows}, columns : {self.columns} )"

    def __unicode__(self):
        return f"{self.name} ( rows : {self.rows}, columns : {self.columns} )"

# TODO: Supercharging TargetFaceNameChoide Snippet with Advanced Features
class TargetFaceNameChoice(BaseScoringModel):
    ENVIRONMENTS = [
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    ]
    
    DISCIPLINES = [
        ('Target Archery', 'Target Archery'),
        ('Field Archery', 'Field Archery'),
    ]
    
    TARGETSIZES = [
        ('122 cm', '122 cm'),
        ('80 cm', '80 cm'),
        ('65 cm', '65 cm'),
        ('60 cm', '60 cm'),
        ('50 cm', '50 cm'),
        ('40 cm', '40 cm'),
        ('35 cm', '30 cm'),
        ('30 cm', '30 cm'),
        ('20 cm', '20 cm'),
    ]
    
    KEYFEATURES = [
        ('5-Zone', '5-Zone'),
        ('6-Zone', '6-Zone'),
        ('10-Zone', '10-Zone'),
    ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = models.CharField(
        max_length=128,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("Name"),
        help_text=_("format: required, max-128")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    environment = models.CharField(
        max_length=32,
        null=False,
        unique=False,
        blank=False,
        choices=ENVIRONMENTS,
        verbose_name=_("Environment"),
        help_text=_("format: required, max-32")
    )
    discipline = models.CharField(
        max_length=32,
        null=False,
        unique=False,
        blank=False,
        choices=DISCIPLINES,
        verbose_name=_("Discipline"),
        help_text=_("format: required, max-32")
    )
    targetsize = models.CharField(
        max_length=32,
        null=False,
        unique=False,
        blank=False,
        choices=TARGETSIZES,
        verbose_name=_("Target size"),
        help_text=_("format: required, max-32")
    )
    keyfeature = models.CharField(
        max_length=32,
        null=False,
        unique=False,
        blank=False,
        choices=KEYFEATURES,
        verbose_name=_("Key feature"),
        help_text=_("format: required, max-32")
    )
    
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='targetfacenamechoice_author',
        verbose_name=_("Author"),
        help_text=_("format: required, default=1 (superuser)"),
    )
    
    class Meta:
        db_table = 'targetfacenamechoices'
        ordering = ['name']
        verbose_name = _("Target Face Name Choice")
        verbose_name_plural = _("Target Faces Name Choices")
                   
    def __str__(self):
        return f"{self.name} )"

    def __unicode__(self):
        return f"{self.name} )"  

# TODO: Supercharging TargetFace Snippet with Advanced Features
class TargetFace(BaseScoringModel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
    name = models.CharField(
        max_length=64,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("Name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    # TODO: Insert image field
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='targetface_author',
        verbose_name=_("Author"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'targetfaces'
        ordering = ['name']
        verbose_name = _("Target Face")
        verbose_name_plural = _("Target Faces")

    def __str__(self):
        return f"{self.name} )"

    def __unicode__(self):
        return f"{self.name} )"

# TODO: Supercharging Round Snippet with Advanced Features
class Round(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = models.CharField(
        max_length=64,
        null=False,
        unique=True,
        blank=False,
        default='',
        verbose_name=_("Name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(
        populate_from='name',
        editable=True
    )
    start_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("Start date"),
        help_text=_("format: Y-m-d, not required"),
    )
    start_time = models.TimeField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("Start time"),
        help_text=_("format: H:M:S, not required"),
    )
    end_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("End date"),
        help_text=_("format: Y-m-d, not required"),
    )
    end_time = models.TimeField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("End time"),
        help_text=_("format: H:M:S, not required"),
    )
    # TODO: Insert location
    archers = models.ManyToManyField(
        Archer,
        through='RoundMembership',
        blank=True,
        help_text=_("format: not required"),
        related_name='round_archers',
        verbose_name=_("Archers"),
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='round_author',
        verbose_name=_("Author"),
        help_text=_("format: not required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'rounds'
        ordering = ['name']
        verbose_name = _("Round")
        verbose_name_plural = _("Rounds")

    def __str__(self):
        return self.name

    def __unicode__(self):       
        return self.name

# TODO: Supercharging RoundMembership Snippet with Advanced Features
class RoundMembership(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    round = models.ForeignKey(
        Round,
        on_delete=models.PROTECT,
        unique=False,
        default=1,
        verbose_name=_("Round"),
        help_text=_("format: required"),
        related_name='roundmembership_round'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("Archer"),
        help_text=_("format: required"),
        related_name='roundmembership_archer'
    )
    slug = AutoSlugField(
        populate_from=('archer__last_name', 'round__name'), 
        editable=True
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='roundmembership_author',
        verbose_name=_("Author"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'roundmemberships'
        ordering = ['round__name']
        verbose_name = _("Round Membership")
        verbose_name_plural = _("Round Memberships")

    def __str__(self):
        return f"{str(self.archer)} - {str(self.round)}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.round)}"

# TODO: Supercharging Score Snippet with Advanced Features
class Score(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    round_archer = models.ForeignKey(
        RoundMembership,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        unique=False,
        related_name='score_round_archer',
        verbose_name="Round & Archer,",
        help_text=_("format: required"),
    )
    score = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name=_("Score"),
        help_text=_("format: not required")
    )
    number_of_arrows = models.PositiveIntegerField(
        null=False,
        blank=False,
        default=0,
        verbose_name=_("Number of arrows")  ,      
        help_text=_("format: not required"),
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='score_author',
        verbose_name=_("Author"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'scores'
        verbose_name = _("Score")
        verbose_name_plural = _("Scores")

    # TODO: 119
    def __str__(self):
        if self.round_archer:
            return f"{str(self.score)} - {str(self.round_archer.archer)}"
        else:
            return f"{str(self.score)} - No Archer"

    def __unicode__(self):
        if self.round_archer:
            return f"{str(self.score)} - {str(self.round_archer.archer)}"
        else:
            return f"{str(self.score)} - No Archer"

# TODO: Can be removed probably
# class ScoreMembership(BaseScoringModel):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

# TODO: Supercharging Competition Snippet with Advanced Features
class Competition(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = models.CharField(
        max_length=64,
        null=False,
        unique=True,
        blank=False,
        default='',
        verbose_name=_("Name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(
        populate_from='name',
        editable=True
    )
    rounds = models.ManyToManyField(
        Round,
        through='CompetitionMembership',
        blank=True,
        help_text=_("format: not required"),
        related_name='competition_rounds',
        verbose_name=_("Competition rounds"),
    )
    start_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("Start date"),
        help_text=_("format: Y-m-d, not required"),
    )
    end_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("End date"),
        help_text=_("format: Y-m-d, not required"),
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='competition_author',
        verbose_name=_("Author"),
        help_text=_("format: not required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'competitions'
        ordering = ['name']
        verbose_name = _("Competitions")
        verbose_name_plural = _("Competitions")

    def __str__(self):
        return self.name

    def __unicode__(self):       
        return self.name

# TODO: Supercharging CompetitionMembership Snippet with Advanced Features
class CompetitionMembership(BaseScoringModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    competition = models.ForeignKey(
        Competition,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("Competition"),
        help_text=_("format: required"),
        related_name='competitionmembership_competition'
    )
    round = models.ForeignKey(
        Round,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("Round"),
        help_text=_("format: required"),
        related_name='competitionmembership_round'
    )
    slug = AutoSlugField(
        populate_from=('competition__name', 'round__name',), 
        editable=True,
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.PROTECT,
        default=1,
        related_name='competitionmembership_author',
        verbose_name=_("Author"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'competitionmemberships'
        ordering = ['competition__name']
        verbose_name = _("Competition Membership")
        verbose_name_plural = _("Competition Memberships")

    def __str__(self):
        return f"{str(self.competition)} - {str(self.round)}"

    def __unicode__(self):
        return f"{str(self.competition)} - {str(self.round)}"

#----------------------------------------
# Wagtail
#----------------------------------------

from wagtail.blocks import DateBlock, IntegerBlock
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField, StreamBlock
from wagtail.admin.panels import (
    FieldPanel,
    HelpPanel,
    MultiFieldPanel,
    InlinePanel,
    PageChooserPanel,
    FieldRowPanel,
    MultipleChooserPanel,
    TitleFieldPanel,
)
from modelcluster.fields import (
    ParentalKey,
    ParentalManyToManyField,
)
from django import forms

from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

class BaseScoringPage(Page):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

# Archer

class ArcherPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ArcherPage',
        related_name='tagged_archerpage_items',
        on_delete=models.CASCADE
    )

class ArcherPage(BaseScoringPage):
    # parent_page_types = ['home.HomePage']
    # subpage_types = []

    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="ArcherPage image",
    )
    body = RichTextField(blank=True)
   
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=ArcherPageTag, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'archer_members',
            heading="Archers",
            label="Archer",
            chooser_field_name='archer',
            help_text="Select archers to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class ArcherPageMembers(Orderable):
    page = ParentalKey('ArcherPage', on_delete=models.CASCADE, related_name='archer_members')
    archer = models.ForeignKey(Archer, on_delete=models.PROTECT)

    panels = [
        FieldPanel('archer', heading="Record"),        
    ]

# Discipline

class DisciplinePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'DisciplinePage',
        related_name='tagged_disciplinepage_items',
        on_delete=models.CASCADE
    )

class DisciplinePage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    body = RichTextField(blank=True)
    
    authors = ParentalManyToManyField(CustomUser, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="DisciplinePage image",
    )
    tags = ClusterTaggableManager(through=DisciplinePageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'discipline_members',
            heading="Disciplines",
            label="Discipline",
            chooser_field_name='discipline',
            help_text="Select disciplines to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class DisciplinePageMembers(Orderable):
    page = ParentalKey('DisciplinePage', on_delete=models.CASCADE, related_name='discipline_members')
    discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT)

    panels = [
        FieldPanel('discipline', heading="Record"),
    ]
    
class DisciplineMembershipPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'DisciplineMembershipPage',
        related_name='tagged_disciplinemembershippage_items',
        on_delete=models.CASCADE
    )
    
class DisciplineMembershipPage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="DisciplineMembershipPage image",
    )
    body = RichTextField(blank=True)
    
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=DisciplineMembershipPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'disciplinemembership_members',
            heading="Discipline Memberships",
            label="Discipline Membership",
            chooser_field_name='disciplinemembership',
            help_text="Select discipline memberships to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class DisciplineMembershipPageMembers(Orderable):
    page = ParentalKey('DisciplineMembershipPage', on_delete=models.CASCADE, related_name='disciplinemembership_members')
    disciplinemembership = models.ForeignKey(DisciplineMembership, on_delete=models.PROTECT)

    panels = [
        FieldPanel('disciplinemembership', heading="Record"),
    ]

class ClubPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ClubPage',
        related_name='tagged_clubpage_items',
        on_delete=models.CASCADE
    )

class ClubPage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="ClubPage image",
    )
    body = RichTextField(blank=True)
   
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=ClubPageTag, blank=True)
 
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'club_members',
            heading="Clubs",
            label="Club",
            chooser_field_name='club',
            help_text="Select clubs to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class ClubPageMembers(Orderable):
    page = ParentalKey('ClubPage', on_delete=models.CASCADE, related_name='club_members')
    club = models.ForeignKey(Club, on_delete=models.PROTECT)

    panels = [
        FieldPanel('club', heading="Record"),
    ]
       
class ClubMembershipPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ClubMembershipPage',
        related_name='tagged_clubmembershippage_items',
        on_delete=models.CASCADE
    )
       
class ClubMembershipPage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="ClubMembershipPage image",
    )
    body = RichTextField(blank=True)
    
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=ClubMembershipPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'clubmembership_members',
            heading="Club Memberships",
            label="Club Membership",
            chooser_field_name='clubmembership',
            help_text="Select club memberships to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class ClubMembershipPageMembers(Orderable):
    page = ParentalKey('ClubMembershipPage', on_delete=models.CASCADE, related_name='clubmembership_members')
    clubmembership = models.ForeignKey(ClubMembership, on_delete=models.PROTECT)

    panels = [
        FieldPanel('clubmembership', heading="Record"),
    ]

class CategoryPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'CategoryPage',
        related_name='tagged_categorypage_items',
        on_delete=models.CASCADE
    )

class CategoryPage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="CategoryPage image",
    )
    body = RichTextField(blank=True)
    
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=CategoryPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'category_members',
            heading="Categories",
            label="Category",
            chooser_field_name='category',
            help_text="Select categories to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class CategoryPageMembers(Orderable):
    page = ParentalKey('CategoryPage', on_delete=models.CASCADE, related_name='category_members')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    panels = [
        FieldPanel('category', heading="Record"),
    ]

class AgeGroupPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'AgeGroupPage',
        related_name='tagged_agegrouppage_items',
        on_delete=models.CASCADE
    )

class AgeGroupPage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="AgeGroupPage image",
    )
    body = RichTextField(blank=True)
    
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=AgeGroupPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'agegroup_members',
            heading="Age Groups",
            label="Age Group",
            chooser_field_name='agegroup',
            help_text="Select age groups to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class AgeGroupPageMembers(Orderable):
    page = ParentalKey('AgeGroupPage', on_delete=models.CASCADE, related_name='agegroup_members')
    agegroup = models.ForeignKey(AgeGroup, on_delete=models.PROTECT)

    authors = ParentalManyToManyField(CustomUser, blank=True)

    panels = [
        FieldPanel('agegroup', heading="Record"),
    ]

class CategoryMembershipPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'CategoryMembershipPage',
        related_name='tagged_categorymembershippage_items',
        on_delete=models.CASCADE
    )

class CategoryMembershipPage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="ArcherPage image",
    )
    body = RichTextField(blank=True)
    
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=CategoryMembershipPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'categorymembership_members',
            heading="Category Memberships",
            label="Category Membership",
            chooser_field_name='categorymembership',
            help_text="Select category memberships to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class CategoryMembershipPageMembers(Orderable):
    page = ParentalKey('CategoryMembershipPage', on_delete=models.CASCADE, related_name='categorymembership_members')
    categorymembership = models.ForeignKey(CategoryMembership, on_delete=models.PROTECT)

    panels = [
        FieldPanel('categorymembership', heading="Record"),
    ]

class TeamPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'TeamPage',
        related_name='tagged_teampage_items',
        on_delete=models.CASCADE
    )

class TeamPage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="TeamPage image",
    )
    body = RichTextField(blank=True)
    
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=TeamPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'team_members',
            heading="Teams",
            label="Team",
            chooser_field_name='team',
            help_text="Select teams to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class TeamPageMembers(Orderable):
    page = ParentalKey('TeamPage', on_delete=models.CASCADE, related_name='team_members')
    team = models.ForeignKey(Team, on_delete=models.PROTECT)

    panels = [
        FieldPanel('team', heading="Record"),
    ]

class TeamMembershipPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'TeamMembershipPage',
        related_name='tagged_teammembershippage_items',
        on_delete=models.CASCADE
    )

class TeamMembershipPage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="TeamMembershipPage image",
    )
    body = RichTextField(blank=True)
    
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=TeamMembershipPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'teammembership_members',
            heading="Team Memberships",
            label="Team Membership",
            chooser_field_name='teammembership',
            help_text="Select team memberships to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class TeamMembershipPageMembers(Orderable):
    page = ParentalKey('TeamMembershipPage', on_delete=models.CASCADE, related_name='teammembership_members')
    teammembership = models.ForeignKey(TeamMembership, on_delete=models.PROTECT)

    panels = [
        FieldPanel('teammembership', heading="Record"),
    ]

class ScoringSheetPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ScoringSheetPage',
        related_name='tagged_scoringsheetpage_items',
        on_delete=models.CASCADE
    )

class ScoringSheetPage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="ScoringSheetPage image",
    )
    body = RichTextField(blank=True)
    
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=ScoringSheetPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'scoringsheet_members',
            heading="Scoring Sheets",
            label="Scoring Sheet",
            chooser_field_name='scoringsheet',
            help_text="Select scoring sheets to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class ScoringSheetPageMembers(Orderable):
    page = ParentalKey('ScoringSheetPage', on_delete=models.CASCADE, related_name='scoringsheet_members')
    scoringsheet = models.ForeignKey(ScoringSheet, on_delete=models.PROTECT)

    panels = [
        FieldPanel('scoringsheet', heading="Record"),
    ]

class TargetFaceNameChoicePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'TargetFaceNameChoicePage',
        related_name='tagged_targetfacenamechoicepage_items',
        on_delete=models.CASCADE
    )

class TargetFaceNameChoicePage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="TargetFaceNameChoicePage image",
    )
    body = RichTextField(blank=True)

    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=TargetFaceNameChoicePageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'targetfacenamechoice_members',
            heading="Target Face Name Choices",
            label="Target Face Name Choice",
            chooser_field_name='targetfacenamechoice',
            help_text="Select target face name choices to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]
    
class TargetFaceNameChoicePageMembers(Orderable):
    page = ParentalKey('TargetFaceNameChoicePage', on_delete=models.CASCADE, related_name='targetfacenamechoice_members')
    targetfacenamechoice = models.ForeignKey(TargetFaceNameChoice, on_delete=models.PROTECT)

    panels = [
        FieldPanel('targetfacenamechoice', heading="Record"),
    ]

class TargetFacePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'TargetFacePage',
        related_name='tagged_targetfacepage_items',
        on_delete=models.CASCADE
    )

class TargetFacePage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="TargetFacePage image",
    )
    body = RichTextField(blank=True)
    
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=TargetFacePageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'targetface_members',
            heading="Target Faces",
            label="Target Face",
            chooser_field_name='targetface',
            help_text="Select target faces to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class TargetFacePageMembers(Orderable):
    page = ParentalKey('TargetFacePage', on_delete=models.CASCADE, related_name='targetface_members')
    targetface = models.ForeignKey(TargetFace, on_delete=models.PROTECT)

    panels = [
        FieldPanel('targetface', heading="Record"),
    ]

class RoundPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'RoundPage',
        related_name='tagged_roundpage_items',
        on_delete=models.CASCADE
    )
    
class RoundPage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="RoundPage image",
    )
    body = RichTextField(blank=True)
    
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=RoundPageTag, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'round_members',
            heading="Rounds",
            label="Round",
            chooser_field_name='round',
            help_text="Select rounds to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]
    
class RoundPageMembers(Orderable):
    page = ParentalKey('RoundPage', on_delete=models.CASCADE, related_name='round_members')
    round = models.ForeignKey(Round, on_delete=models.PROTECT)

    panels = [
        FieldPanel('round', heading="Record"),
    ]
    
class RoundMembershipPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'RoundMembershipPage',
        related_name='tagged_roundmembershippage_items',
        on_delete=models.CASCADE
    )
    
class RoundMembershipPage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="RoundMembershipPage image",
    )
    body = RichTextField(blank=True)

    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=RoundMembershipPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'roundmembership_members',
            heading="Round Memberships",
            label="Round Membership",
            chooser_field_name='roundmembership',
            help_text="Select round memberships to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class  RoundMembershipPageMembers(Orderable):
    page = ParentalKey('RoundMembershipPage', on_delete=models.CASCADE, related_name='roundmembership_members')
    roundmembership = models.ForeignKey(RoundMembership, on_delete=models.PROTECT)

    panels = [
        FieldPanel('roundmembership', heading="Record"),
    ]

class ScorePageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ScorePage',
        related_name='tagged_scorepage_items',
        on_delete=models.CASCADE
    )

class ScorePage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="ScorePage image",
    )
    body = RichTextField(blank=True)
    
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=ScorePageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'score_members',
            heading="Scores",
            label="Score",
            chooser_field_name='score',
            help_text="Select scores to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class ScorePageMembers(Orderable):
    page = ParentalKey('ScorePage', on_delete=models.CASCADE, related_name='score_members')
    score = models.ForeignKey(Score, on_delete=models.PROTECT)

    panels = [
        FieldPanel('score', heading="Record"),
    ]

class CompetitionPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'CompetitionPage',
        related_name='tagged_competitionpage_items',
        on_delete=models.CASCADE
    )

class CompetitionPage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="CompetitionPage image",
    )
    body = RichTextField(blank=True)
    
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=CompetitionPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'competition_members',
            heading="Competitions",
            label="Competition",
            chooser_field_name='competition',
            help_text="Select competitions to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]
    
class CompetitionPageMembers(Orderable):
    page = ParentalKey('CompetitionPage', on_delete=models.CASCADE, related_name='competition_members')
    competition = models.ForeignKey(Competition, on_delete=models.PROTECT)

    panels = [
        FieldPanel('competition', heading="Record"),
    ]
    
class CompetitionMembershipPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'CompetitionMembershipPage',
        related_name='tagged_competitionmembershippage_items',
        on_delete=models.CASCADE
    )

class CompetitionMembershipPage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="CompetitionMembershipPage image",
    )
    body = RichTextField(blank=True)
    
    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=CompetitionMembershipPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('is_active'),
        MultipleChooserPanel(
            'competitionmembership_members',
            heading="Competition Memberships",
            label="Competition Membership",
            chooser_field_name='competitionmembership',
            help_text="Select competition memberships to be associated with this page."
        ),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]

class CompetitionMembershipPageMembers(Orderable):
    page = ParentalKey('CompetitionMembershipPage', on_delete=models.CASCADE, related_name='competitionmembership_members')
    competitionmembership = models.ForeignKey(CompetitionMembership, on_delete=models.PROTECT)

    panels = [
        FieldPanel('competitionmembership', heading="Record"),
    ]

class ScoringPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'ScoringPage',
        related_name='tagged_scoringpage_items',
        on_delete=models.CASCADE
    )

class ScoringPage(BaseScoringPage):
    subtitle = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="ScoringPage image",
    )
    body = RichTextField(blank=True)

    authors = ParentalManyToManyField(CustomUser, blank=True)
    tags = ClusterTaggableManager(through=ScoringPageTag, blank=True)

    grid = StreamField(
        [
            ('scoring', StreamBlock([
                ('Date', DateBlock(
                    required=False,
                    help_text=_("format: Y-m-d, not required"),
                )),
                ('Score', IntegerBlock(
                    required=False,
                    help_text=_("Total score. format: not required")
                )),
                ('Arrows', IntegerBlock(
                    required=False,
                    help_text=_("Number of arrows. format: not required")
                )),
                ('Sheet_10x3',TableBlock_3_Cols_10_Rows(
                    required=False,
                    help_text=_("Scores per arrow. format: not required")
                )),
                ('Sheet_12x3',TableBlock_3_Cols_12_Rows(
                    required=False,
                    help_text=_("Scores per arrow. format: not required")
                )),               
                ('Sheet_5x5',TableBlock_5_Cols_5_Rows(
                    required=False,
                    help_text=_("Scores per arrow. format: not required")
                )),               
            ])),
        ]
    )
   
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('grid'),
        FieldPanel('authors', widget=forms.CheckboxSelectMultiple),
        FieldPanel('tags'),
    ]
    
