from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .serializers import (
    ArcherSerializer,
    ArcherInfoSerializer,
    DisciplineSerializer,
    DisciplineInfoSerializer,
    DisciplineMembershipSerializer,
    DisciplineMembershipInfoSerializer,
    ClubSerializer,
    ClubInfoSerializer,
    ClubMembershipSerializer,
    ClubMembershipInfoSerializer,
    CategorySerializer,
    CategoryInfoSerializer,
    AgeGroupSerializer,
    AgeGroupInfoSerializer,
    CategoryMembershipSerializer,
    CategoryMembershipInfoSerializer,
    TeamSerializer,
    TeamInfoSerializer,
    TeamMembershipSerializer,
    TeamMembershipInfoSerializer,
    ScoringSheetSerializer,
    ScoringSheetInfoSerializer,
    TargetFaceNameChoiceSerializer,
    TargetFaceNameChoiceInfoSerializer,
    TargetFaceSerializer,
    TargetFaceInfoSerializer,
    RoundSerializer,
    RoundInfoSerializer,
    RoundMembershipSerializer,
    RoundMembershipInfoSerializer,
    ScoreSerializer,
    ScoreInfoSerializer,
    CompetitionSerializer,
    CompetitionInfoSerializer,
    CompetitionMembershipSerializer,
    CompetitionMembershipInfoSerializer,
)
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
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
)

# Archer

class ArcherListAPIView(generics.ListAPIView):
    queryset = Archer.objects.all()
    serializer_class = ArcherSerializer

class ArcherDetailAPIView(generics.RetrieveAPIView):
    queryset = Archer.objects.all()
    serializer_class = ArcherSerializer

class UserArcherListAPIView(generics.ListAPIView):
    queryset = Archer.objects.all()
    serializer_class = ArcherSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

@api_view(['GET'])
def archer_info(request):
    archers = Archer.objects.all()
    serializer = ArcherInfoSerializer({
        'archers': archers,
        'count': len(archers),
    })

    return Response(serializer.data)

# Discipline

class DisciplineListAPIView(generics.ListAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

class DisciplineDetailAPIView(generics.RetrieveAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

class UserDisciplineListAPIView(generics.ListAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

@api_view(['GET'])
def discipline_info(request):
    disciplines = Discipline.objects.prefetch_related(
        'archers',
    )
    serializer = DisciplineInfoSerializer({
        'disciplines': disciplines,
        'count': len(disciplines),
    })

    return Response(serializer.data)

# DisciplineMembership

class DisciplineMembershipListAPIView(generics.ListAPIView):
    queryset = DisciplineMembership.objects.all()
    serializer_class = DisciplineMembershipSerializer

class DisciplineMembershipDetailAPIView(generics.RetrieveAPIView):
    queryset = DisciplineMembership.objects.all()
    serializer_class = DisciplineMembershipSerializer

class UserDisciplineMembershipListAPIView(generics.ListAPIView):
    queryset = DisciplineMembership.objects.all()
    serializer_class = DisciplineMembershipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

@api_view(['GET'])
def discipline_memberships_info(request):
    disciplinememberships = DisciplineMembership.objects.prefetch_related(
        'discipline',
        'archer',
    )
    serializer = DisciplineMembershipInfoSerializer({
        'disciplinememberships': disciplinememberships,
        'count': len(disciplinememberships),
    })

    return Response(serializer.data)

# Club

class ClubListAPIView(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class ClubDetailAPIView(generics.RetrieveAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class UserClubListAPIView(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

@api_view(['GET'])
def club_info(request):
    clubs = Club.objects.prefetch_related(
        'archers',
    )
    serializer = ClubInfoSerializer({
        'clubs': clubs,
        'count': len(clubs),
    })

    return Response(serializer.data)

# ClubMembership

class ClubMembershipListAPIView(generics.ListAPIView):
    queryset = ClubMembership.objects.all()
    serializer_class = ClubMembershipSerializer

class ClubMembershipDetailAPIView(generics.RetrieveAPIView):
    queryset = ClubMembership.objects.all()
    serializer_class = ClubMembershipSerializer

class UserClubMembershipListAPIView(generics.ListAPIView):
    queryset = ClubMembership.objects.all()
    serializer_class = ClubMembershipSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

@api_view(['GET'])
def club_memberships_info(request):
    clubmemberships = ClubMembership.objects.prefetch_related(
        'club',
        'archer',
    )
    serializer = ClubMembershipInfoSerializer({
        'clubmemberships': clubmemberships,
        'count': len(clubmemberships)
    })

    return Response(serializer.data)

# Category

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class UserCategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

# @api_view(['GET'])
# def category_detail(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     serializer = CategorySerializer(category)

#     return Response(serializer.data)

@api_view(['GET'])
def category_info(request):
    categories = Category.objects.prefetch_related(
        'archers',
    )
    serializer = CategoryInfoSerializer({
        'categories': categories,
        'count': len(categories),
    })

    return Response(serializer.data)

# AgeGroup

class AgeGroupListAPIView(generics.ListAPIView):
    queryset = AgeGroup.objects.all()
    serializer_class = AgeGroupSerializer

class AgeGroupDetailAPIView(generics.RetrieveAPIView):
    queryset = AgeGroup.objects.all()
    serializer_class = AgeGroupSerializer

# @api_view(['GET'])
# def agegroup_detail(request, pk):
#     agegroup = get_object_or_404(agegroup, pk=pk)
#     serializer = AgeGroupSerializer(agegroup)

#     return Response(serializer.data)

@api_view(['GET'])
def agegroup_info(request):
    agegroups = AgeGroup.objects.all()
    serializer = AgeGroupInfoSerializer({
        'agegroups': agegroups,
        'count': len(agegroups),
    })

    return Response(serializer.data)

# CategoryMembership

class CategoryMembershipListAPIView(generics.ListAPIView):
    queryset = CategoryMembership.objects.all()
    serializer_class = CategoryMembershipSerializer

class CategoryMembershipDetailAPIView(generics.RetrieveAPIView):
    queryset = CategoryMembership.objects.all()
    serializer_class = CategoryMembershipSerializer

# @api_view(['GET'])
# def category_memberships_detail(request, pk):
#     categorymembership = get_object_or_404(CategoryMembership, pk=pk)
#     serializer = CategoryMembershipSerializer(categorymembership)

#     return Response(serializer.data)

@api_view(['GET'])
def category_memberships_info(request):
    categorymemberships = CategoryMembership.objects.prefetch_related(
        'category',
        'archer',
        'agegroup',
    )
    serializer = CategoryMembershipInfoSerializer({
        'categorymemberships': categorymemberships,
        'count': len(categorymemberships),
    })

    return Response(serializer.data)

# Team

class TeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetailAPIView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

# @api_view(['GET'])
# def team_detail(request, pk):
#     team = get_object_or_404(Team, pk=pk)
#     serializer = TeamSerializer(team)

#     return Response(serializer.data)

@api_view(['GET'])
def team_info(request):
    teams = Team.objects.prefetch_related(
        'archers',
    )
    serializer = TeamInfoSerializer({
        'teams': teams,
        'count': len(teams),
    })

    return Response(serializer.data)

# TeamMembership

class TeamMembershipListAPIView(generics.ListAPIView):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipSerializer

class TeamMembershipDetailAPIView(generics.RetrieveAPIView):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipSerializer

# @api_view(['GET'])
# def team_memberships_detail(request, pk):
#     teammembership = get_object_or_404(TeamMembership, pk=pk)
#     serializer = TeamMembershipSerializer(teammembership)

#     return Response(serializer.data)

@api_view(['GET'])
def team_memberships_info(request):
    teammemberships = TeamMembership.objects.prefetch_related(
        'team',
        'archer',
    )
    serializer = TeamMembershipInfoSerializer({
        'teammemberships': teammemberships,
        'count': len(teammemberships),
    })

    return Response(serializer.data)

# ScoringSheet

class ScoringSheetListAPIView(generics.ListAPIView):
    queryset = ScoringSheet.objects.all()
    serializer_class = ScoringSheetSerializer

class ScoringSheetDetailAPIView(generics.RetrieveAPIView):
    queryset = ScoringSheet.objects.all()
    serializer_class = ScoringSheetSerializer

# @api_view(['GET'])
# def scoringsheet_detail(request, pk):
#     scoringsheets = get_object_or_404(ScoringSheet, pk=pk)
#     serializer = ScoringSheetSerializer(scoringsheets)

#     return Response(serializer.data)

@api_view(['GET'])
def scoringsheet_info(request):
    scoringsheets = ScoringSheet.objects.all()
    serializer = ScoringSheetInfoSerializer({
        'scoringsheets': scoringsheets,
        'count': len(scoringsheets),
    })

    return Response(serializer.data)

# TargetFaceNameChoice

class TargetFaceNameChoiceListAPIView(generics.ListAPIView):
    queryset = TargetFaceNameChoice.objects.all()
    serializer_class = TargetFaceNameChoiceSerializer

class TargetFaceNameChoiceDetailAPIView(generics.RetrieveAPIView):
    queryset = TargetFaceNameChoice.objects.all()
    serializer_class = TargetFaceNameChoiceSerializer

@api_view(['GET'])
def targetfacenamechoice_detail(request, pk):
    targetfacenamechoice = get_object_or_404(TargetFaceNameChoice, pk=pk)
    serializer = TargetFaceNameChoiceSerializer(targetfacenamechoice)

    return Response(serializer.data)

@api_view(['GET'])
def targetfacenamechoice_info(request):
    targetfacenamechoices = TargetFaceNameChoice.objects.all()
    serializer = TargetFaceNameChoiceInfoSerializer({
        'targetfacenamechoices': targetfacenamechoices,
        'count': len(targetfacenamechoices),
    })

    return Response(serializer.data)

# TargetFace

class TargetFaceListAPIView(generics.ListAPIView):
    queryset = TargetFace.objects.all()
    serializer_class = TargetFaceSerializer

class TargetFaceDetailAPIView(generics.RetrieveAPIView):
    queryset = TargetFace.objects.all()
    serializer_class = TargetFaceSerializer

# @api_view(['GET'])
# def targetface_detail(request, pk):
#     targetface = get_object_or_404(TargetFace, pk=pk)
#     serializer = TargetFaceSerializer(targetface)

#     return Response(serializer.data)

@api_view(['GET'])
def targetface_info(request):
    targetfaces = TargetFace.objects.all()
    serializer = TargetFaceInfoSerializer({
        'targetfaces': targetfaces,
        'count': len(targetfaces),
    })

    return Response(serializer.data)

# Round

class RoundListAPIView(generics.ListAPIView):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer

class RoundDetailAPIView(generics.RetrieveAPIView):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer

# @api_view(['GET'])
# def round_detail(request, pk):
#     round = get_object_or_404(Round, pk=pk)
#     serializer = RoundSerializer(round)

#     return Response(serializer.data)

@api_view(['GET'])
def round_info(request):
    rounds = Round.objects.prefetch_related(
        'archers',
    )
    serializer = RoundInfoSerializer({
        'rounds': rounds,
        'count': len(rounds),
    })

    return Response(serializer.data)

# RoundMembership

class RoundMembershipListAPIView(generics.ListAPIView):
    queryset = RoundMembership.objects.all()
    serializer_class = RoundMembershipSerializer

class RoundMembershipDetailAPIView(generics.RetrieveAPIView):
    queryset = RoundMembership.objects.all()
    serializer_class = RoundMembershipSerializer

# @api_view(['GET'])
# def round_memberships_detail(request, pk):
#     roundmembership = get_object_or_404(RoundMembership, pk=pk)
#     serializer = RoundMembershipSerializer(roundmembership)

#     return Response(serializer.data)

@api_view(['GET'])
def round_memberships_info(request):
    roundmemberships = RoundMembership.objects.prefetch_related(
        'round',
        'archer',
    ).all()
    serializer = RoundMembershipInfoSerializer({
        'roundmemberships': roundmemberships,
        'count': len(roundmemberships),
    })

    return Response(serializer.data)

# Score

class ScoreListAPIView(generics.ListAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

class ScoreDetailAPIView(generics.RetrieveAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

# @api_view(['GET'])
# def score_detail(request, pk):
#     score = get_object_or_404(Score, pk=pk)
#     serializer = ScoreSerializer(score)

#     return Response(serializer.data)

@api_view(['GET'])
def score_info(request):
    scores = Score.objects.prefetch_related(
        'round_archer',
    )
    serializer = ScoreInfoSerializer({
        'scores': scores,
        'count': len(scores),
    })

    return Response(serializer.data)

# Competition

class CompetitionListAPIView(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

class CompetitionDetailAPIView(generics.RetrieveAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

# @api_view(['GET'])
# def competition_detail(request, pk):
#     competition = get_object_or_404(Competition, pk=pk)
#     serializer = CompetitionSerializer(competition)

#     return Response(serializer.data)

@api_view(['GET'])
def competition_info(request):
    competitions = Competition.objects.prefetch_related(
        'rounds',
    )
    serializer = CompetitionInfoSerializer({
        'competitions': competitions,
        'count': len(competitions),
    })

    return Response(serializer.data)

# CompetitionMembership

class CompetitionMembershipListAPIView(generics.ListAPIView):
    queryset = CompetitionMembership.objects.all()
    serializer_class = CompetitionMembershipSerializer

class CompetitionMembershipDetailAPIView(generics.RetrieveAPIView):
    queryset = CompetitionMembership.objects.all()
    serializer_class = CompetitionMembershipSerializer

# def competition_memberships_detail(request, pk):
#     competitionmembership = get_object_or_404(CompetitionMembership, pk=pk)
#     serializer = CompetitionMembershipSerializer(competitionmembership)

#     return Response(serializer.data)

@api_view(['GET'])
def competition_memberships_info(request):
    competitionmemberships = CompetitionMembership.objects.prefetch_related(
        'competition',
        'round',
    )
    serializer = CompetitionMembershipInfoSerializer({
        'competitionmemberships': competitionmemberships,
        'count': len(competitionmemberships),
    })

    return Response(serializer.data)
