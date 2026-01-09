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

class DisciplineSerializer(serializers.ModelSerializer):
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

class DisciplineMembershipSerializer(serializers.ModelSerializer):
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

class ClubSerializer(serializers.ModelSerializer):
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

class ClubMembershipSerializer(serializers.ModelSerializer):
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

class CategorySerializer(serializers.ModelSerializer):
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

class CategoryMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryMembership
        fields = (
            'id',
            'category',
            'archer',
            'agegroup',
            'slug',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

class TeamSerializer(serializers.ModelSerializer):
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

class TeamMembershipSerializer(serializers.ModelSerializer):
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

class RoundSerializer(serializers.ModelSerializer):
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

class RoundMembershipSerializer(serializers.ModelSerializer):
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

class CompetitionSerializer(serializers.ModelSerializer):
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

class CompetitionMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionMembership
        fields = (
            'id',
            'compeition',
            'round',
            'slug',
            'info',
            'author',
            'created_at',
            'modified_at',
            'is_active',
        )

