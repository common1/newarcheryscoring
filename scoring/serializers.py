from rest_framework import serializers

from .models import (
    Archer,
    Discipline,
    DisciplineMembership,
    Club,
    ClubMembership,
    Category,
    AgeGroup,
    CategoryMembership,
    Team,
    TeamMembership,
    ScoringSheet,
    TargetFaceNameChoice,
    TargetFace,
    Round,
    RoundMembership,
    Score,
    Competition,
    CompetitionMembership,
)

# Archer

class ArcherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archer
        fields = (
            'id',
            'created_at',
            'modified_at',
            'last_name',
            'first_name',
            'middle_name',
            'birth_date',
            'slug',
            'union_number',
            'email',
            'phone',
            'address',
            'city',
            'zip_code',
            'province',
            'info',
            'author',
        )

class  ArcherInfoSerializer(serializers.Serializer):
    archers = ArcherSerializer(many=True)
    count = serializers.FloatField()

# Discipline

class DisciplineSerializer(serializers.ModelSerializer):
    archers = ArcherSerializer(many=True, read_only=True)

    class Meta:
        model= Discipline
        fields = (
            'id',
            'name',
            'slug',
            'archers',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class  DisciplineInfoSerializer(serializers.Serializer):
    disciplines = DisciplineSerializer(many=True)
    count = serializers.FloatField()

# DisciplineMembership

class DisciplineMembershipSerializer(serializers.ModelSerializer):
    # discipline = DisciplineSerializer()
    # archer = ArcherSerializer()
    # discipline = serializers.CharField()
    # archer = serializers.CharField()

    class Meta:
        model = DisciplineMembership
        fields = (
            'id',
            'discipline',
            'archer',
            'slug',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class  DisciplineMembershipInfoSerializer(serializers.Serializer):
    disciplinememberships = DisciplineMembershipSerializer(many=True)
    count = serializers.FloatField()


# Club

class ClubSerializer(serializers.ModelSerializer):
    archers = ArcherSerializer(many=True, read_only=True)

    class Meta:
        model = Club
        fields = (
            'id',
            'name',
            'slug',
            'address',
            'zip_code',
            'town',
            'archers',
            'info',
            'author',
            'email',
            'phone',
            'website',
            'social_media',
            'created_at',
            'modified_at',
            'is_active',
        )

class  ClubInfoSerializer(serializers.Serializer):
    clubs = ClubSerializer(many=True)
    count = serializers.FloatField()

# ClubMembership

class ClubMembershipSerializer(serializers.ModelSerializer):
    # club = ClubSerializer()
    # archer = ArcherSerializer()
    # club = serializers.CharField()
    # archer = serializers.CharField()

    class Meta:
        model = ClubMembership
        fields = (
            'id',
            'club',
            'archer',
            'slug',
            'start_date',
            'end_date',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class ClubMembershipInfoSerializer(serializers.Serializer):
    clubmemberships = ClubMembershipSerializer(many=True)
    count = serializers.FloatField()

# Category

class CategorySerializer(serializers.ModelSerializer):
    archers = ArcherSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'archers',
            'info',
            'author',
            'created_at',
            'is_active',
            'modified_at',
        )

class CategoryInfoSerializer(serializers.Serializer):
    categories = CategorySerializer(many=True)
    count = serializers.FloatField()

# AgeGroup

class AgeGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeGroup
        fields = (
            'id',
            'name',
            'slug',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class AgeGroupInfoSerializer(serializers.Serializer):
    agegroups = AgeGroupSerializer(many=True)
    count = serializers.FloatField()

# CategoryMembership

class CategoryMembershipSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # archer = ArcherSerializer()
    # archer = serializers.CharField()
    # category = serializers.CharField()

    class Meta:
        model = CategoryMembership
        fields = (
            'id',
            'archer',
            'category',
            'agegroup',
            'slug',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class CategoryMembershipInfoSerializer(serializers.Serializer):
    categorymemberships = CategoryMembershipSerializer(many=True)
    count = serializers.FloatField()

# Team

class TeamSerializer(serializers.ModelSerializer):
    archers = ArcherSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'slug',
            'archers',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class TeamInfoSerializer(serializers.Serializer):
    teams = TeamSerializer(many=True)
    count = serializers.FloatField()

# TeamMembership

class TeamMembershipSerializer(serializers.ModelSerializer):
    # team = TeamSerializer()
    # archer = ArcherSerializer()
    # team = serializers.CharField()
    # archer = serializers.CharField()

    class Meta:
        model = TeamMembership
        fields = (
            'id',
            'team',
            'archer',
            'slug',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class TeamMembershipInfoSerializer(serializers.Serializer):
    teammemberships = TeamMembershipSerializer(many=True)
    count = serializers.FloatField()

# ScoringSheet

class ScoringSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoringSheet
        fields = (
            'id',
            'name',
            'slug',
            'columns',
            'rows',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class ScoringSheetInfoSerializer(serializers.Serializer):
    scoringsheets = ScoringSheetSerializer(many=True)
    count = serializers.FloatField()

# TargetFaceNameChoice

class TargetFaceNameChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetFaceNameChoice
        fields = (
            'id',
            'name',
            'slug',
            'environment',
            'discipline',
            'targetsize',
            'keyfeature',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class TargetFaceNameChoiceInfoSerializer(serializers.Serializer):
    targetfacenamechoices = TargetFaceNameChoiceSerializer(many=True)
    count = serializers.FloatField()

# TargetFace

class TargetFaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetFace
        fields = (
            'id',
            'name',
            'slug',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class TargetFaceInfoSerializer(serializers.Serializer):
    targetfaces = TargetFaceSerializer(many=True)
    count = serializers.FloatField()

# Round

class RoundSerializer(serializers.ModelSerializer):
    archers = ArcherSerializer(many=True, read_only=True)

    class Meta:
        model = Round
        fields = (
            'id',
            'name',
            'slug',
            'start_date',
            'start_time',
            'end_date',
            'end_time',
            'archers',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class RoundInfoSerializer(serializers.Serializer):
    rounds = RoundSerializer(many=True)
    count = serializers.FloatField()

# RoundMembership

class RoundMembershipSerializer(serializers.ModelSerializer):
    # round = RoundSerializer()
    # archer = ArcherSerializer()
    # round = serializers.CharField()
    # archer = serializers.CharField()

    class Meta:
        model = RoundMembership
        fields = (
            'id',
            'round',
            'archer',
            'slug',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class RoundMembershipInfoSerializer(serializers.Serializer):
    roundmemberships = RoundMembershipSerializer(many=True)
    count = serializers.FloatField()

# Score

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = (
            'id',
            'round_archer',
            'score',
            'number_of_arrows',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class ScoreInfoSerializer(serializers.Serializer):
    scores = ScoreSerializer(many=True)
    count = serializers.FloatField()

# Competition

class CompetitionSerializer(serializers.ModelSerializer):
    rounds = RoundSerializer(many=True, read_only=True)

    class Meta:
        model = Competition
        fields = (
            'id',
            'name',
            'slug',
            'rounds',
            'start_date',
            'end_date',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class CompetitionInfoSerializer(serializers.Serializer):
    competitions = CompetitionSerializer(many=True)
    count = serializers.FloatField()

# CompetitionMembership

class CompetitionMembershipSerializer(serializers.ModelSerializer):
    # competition = CompetitionSerializer()
    # round = RoundSerializer()
    # competition = serializers.CharField()
    # round = serializers.CharField()

    class Meta:
        model = CompetitionMembership
        fields = (
            'id',
            'competition',
            'round',
            'slug',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class CompetitionMembershipInfoSerializer(serializers.Serializer):
    competitionmemberships = CompetitionMembershipSerializer(many=True)
    count = serializers.FloatField()
