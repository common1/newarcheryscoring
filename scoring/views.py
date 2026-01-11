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

# Archer
@api_view(['GET'])
def archer_list(request):
    archers = Archer.objects.all()
    serializer = ArcherSerializer(archers, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def archer_detail(request, pk):
    archer = get_object_or_404(Archer, pk=pk)
    serializer = ArcherSerializer(archer)

    return Response(serializer.data)

@api_view(['GET'])
def archer_info(request):
    archers = Archer.objects.all()
    serializer = ArcherInfoSerializer({
        'archers': archers,
        'count': len(archers),
    })

    return Response(serializer.data)

# Discipline
@api_view(['GET'])
def discipline_list(request):
    disciplines = Discipline.objects.all()
    serializer = DisciplineSerializer(disciplines, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def discipline_detail(request, pk):
    discipline = get_object_or_404(Discipline, pk=pk)
    serializer = DisciplineSerializer(discipline)

    return Response(serializer.data)

@api_view(['GET'])
def discipline_info(request):
    disciplines = Discipline.objects.all()
    serializer = DisciplineInfoSerializer({
        'disciplines': disciplines,
        'count': len(disciplines),
    })

    return Response(serializer.data)

# DisciplineMembership
@api_view(['GET'])
def discipline_memberships_list(request):
    disciplinememberships = DisciplineMembership.objects.all()
    serializer = DisciplineMembershipSerializer(disciplinememberships, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def discipline_memberships_detail(request, pk):
    disciplinemembership = get_object_or_404(DisciplineMembership, pk=pk)
    serializer = DisciplineMembershipSerializer(disciplinemembership)

    return Response(serializer.data)

@api_view(['GET'])
def discipline_memberships_info(request):
    disciplinememberships = DisciplineMembership.objects.all()
    serializer = DisciplineMembershipInfoSerializer({
        'disciplinememberships': disciplinememberships,
        'count': len(disciplinememberships),
    })

    return Response(serializer.data)

    return Response(serializer.data)

# Club
@api_view(['GET'])
def club_list(request):
    clubs = Club.objects.all()
    serializer = ClubSerializer(clubs, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def club_detail(request, pk):
    club = get_object_or_404(Club, pk=pk)
    serializer = ClubSerializer(club)

    return Response(serializer.data)

@api_view(['GET'])
def club_info(request):
    clubs = Club.objects.all()
    serializer = ClubInfoSerializer({
        'clubs': clubs,
        'count': len(clubs),
    })

    return Response(serializer.data)

# ClubMembership
@api_view(['GET'])
def club_memberships_list(request):
    clubmemberships = ClubMembership.objects.all()
    serializer = ClubMembershipSerializer(clubmemberships, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def club_memberships_detail(request, pk):
    clubmembership = get_object_or_404(ClubMembership, pk=pk)
    serializer = ClubMembershipSerializer(clubmembership)

    return Response(serializer.data)

@api_view(['GET'])
def club_memberships_info(request):
    clubmemberships = ClubMembership.objects.all()
    serializer = ClubMembershipInfoSerializer({
        'clubmemberships': clubmemberships,
        'count': len(clubmemberships)
    })

    return Response(serializer.data)

# Category
@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)

    return Response(serializer.data)

@api_view(['GET'])
def category_info(request):
    categories = Category.objects.all()
    serializer = CategoryInfoSerializer({
        'categories': categories,
        'count': len(categories),
    })

    return Response(serializer.data)

# AgeGroup
@api_view(['GET'])
def agegroup_list(request):
    agegroups = AgeGroup.objects.all()
    serializer = AgeGroupSerializer(agegroups, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def agegroup_detail(request, pk):
    agegroup = get_object_or_404(agegroup, pk=pk)
    serializer = AgeGroupSerializer(agegroup)

    return Response(serializer.data)

@api_view(['GET'])
def agegroup_info(request):
    agegroups = AgeGroup.objects.all()
    serializer = AgeGroupInfoSerializer({
        'agegroups': agegroups,
        'count': len(agegroups),
    })

    return Response(serializer.data)

# CategoryMembership
@api_view(['GET'])
def category_memberships_list(request):
    categorymemberships = CategoryMembership.objects.all()
    serializer = CategoryMembershipSerializer(categorymemberships, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def category_memberships_detail(request, pk):
    categorymembership = get_object_or_404(CategoryMembership, pk=pk)
    serializer = CategoryMembershipSerializer(categorymembership)

    return Response(serializer.data)

@api_view(['GET'])
def category_memberships_info(request):
    categorymemberships = CategoryMembership.objects.all()
    serializer = CategoryMembershipInfoSerializer({
        'categorymemberships': categorymemberships,
        'count': len(categorymemberships),
    })

    return Response(serializer.data)

# Team
@api_view(['GET'])
def team_list(request):
    teams = Team.objects.all()
    serializer = TeamSerializer(teams, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    serializer = TeamSerializer(team)

    return Response(serializer.data)

@api_view(['GET'])
def team_info(request):
    teams = Team.objects.all()
    serializer = TeamInfoSerializer({
        'teams': teams,
        'count': len(teams),
    })

    return Response(serializer.data)

# TeamMembership
@api_view(['GET'])
def team_memberships_list(request):
    teammemberships = TeamMembership.objects.all()
    serializer = TeamMembershipSerializer(teammemberships, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def team_memberships_detail(request, pk):
    teammembership = get_object_or_404(TeamMembership, pk=pk)
    serializer = TeamMembershipSerializer(teammembership)

    return Response(serializer.data)

@api_view(['GET'])
def team_memberships_info(request):
    teammemberships = TeamMembership.objects.all()
    serializer = TeamMembershipInfoSerializer({
        'teammemberships': teammemberships,
        'count': len(teammemberships),
    })

    return Response(serializer.data)

# ScoringSheet
@api_view(['GET'])
def scoringsheet_list(request):
    scoringsheets = ScoringSheet.objects.all()
    serializer = ScoringSheetSerializer(scoringsheets, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def scoringsheet_detail(request, pk):
    scoringsheets = get_object_or_404(ScoringSheet, pk=pk)
    serializer = ScoringSheetSerializer(scoringsheets)

    return Response(serializer.data)

@api_view(['GET'])
def scoringsheet_info(request):
    scoringsheets = ScoringSheet.objects.all()
    serializer = ScoringSheetInfoSerializer({
        'scoringsheets': scoringsheets,
        'count': len(scoringsheets),
    })

    return Response(serializer.data)

# TargetFaceNameChoice
@api_view(['GET'])
def targetfacenamechoice_list(request):
    targetfacenamechoices = TargetFaceNameChoice.objects.all()
    serializer = TargetFaceNameChoiceSerializer(targetfacenamechoices, many = True)

    return Response(serializer.data)

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
@api_view(['GET'])
def targetface_list(request):
    targetfaces = TargetFace.objects.all()
    serializer = TargetFaceSerializer(targetfaces, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def targetface_detail(request, pk):
    targetface = get_object_or_404(TargetFace, pk=pk)
    serializer = TargetFaceSerializer(targetface)

    return Response(serializer.data)

@api_view(['GET'])
def targetface_info(request):
    targetfaces = TargetFace.objects.all()
    serializer = TargetFaceInfoSerializer({
        'targetfaces': targetfaces,
        'count': len(targetfaces),
    })

    return Response(serializer.data)

# Round
@api_view(['GET'])
def round_list(request):
    rounds = Round.objects.all()
    serializer = RoundSerializer(rounds, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def round_detail(request, pk):
    round = get_object_or_404(Round, pk=pk)
    serializer = RoundSerializer(round)

    return Response(serializer.data)

@api_view(['GET'])
def round_info(request):
    rounds = Round.objects.all()
    serializer = RoundInfoSerializer({
        'rounds': rounds,
        'count': len(rounds),
    })

    return Response(serializer.data)

# RoundMembership
@api_view(['GET'])
def round_memberships_list(request):
    roundmemberships = RoundMembership.objects.all()
    serializer = RoundMembershipSerializer(roundmemberships, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def round_memberships_detail(request, pk):
    roundmembership = get_object_or_404(RoundMembership, pk=pk)
    serializer = RoundMembershipSerializer(roundmembership)

    return Response(serializer.data)

@api_view(['GET'])
def round_memberships_info(request):
    roundmemberships = RoundMembership.objects.all()
    serializer = RoundMembershipInfoSerializer({
        'roundmemberships': roundmemberships,
        'count': len(roundmemberships),
    })

    return Response(serializer.data)

# Score
@api_view(['GET'])
def score_list(request):
    scores = Score.objects.all()
    serializer = ScoreSerializer(scores, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def score_detail(request, pk):
    score = get_object_or_404(Score, pk=pk)
    serializer = ScoreSerializer(score)

    return Response(serializer.data)

@api_view(['GET'])
def score_info(request):
    scores = Score.objects.all()
    serializer = ScoreInfoSerializer({
        'scores': scores,
        'count': len(scores),
    })

    return Response(serializer.data)

# Competition
@api_view(['GET'])
def competition_list(request):
    competitions = Competition.objects.all()
    serializer = CompetitionSerializer(competitions, many = True)

    return Response(serializer.data)

@api_view(['GET'])
def competition_detail(request, pk):
    competition = get_object_or_404(Competition, pk=pk)
    serializer = CompetitionSerializer(competition)

    return Response(serializer.data)

@api_view(['GET'])
def competition_info(request):
    competitions = Competition.objects.all()
    serializer = CompetitionInfoSerializer({
        'competitions': competitions,
        'count': len(competitions),
    })

    return Response(serializer.data)

# CompetitionMembership
@api_view(['GET'])
def competition_memberships_list(request):
    competitionmemberships = CompetitionMembership.objects.all()
    serializer = CompetitionMembershipSerializer(competitionmemberships, many=True)

    return Response(serializer.data)

def competition_memberships_detail(request, pk):
    competitionmembership = get_object_or_404(CompetitionMembership, pk=pk)
    serializer = CompetitionMembershipSerializer(competitionmembership)

    return Response(serializer.data)

@api_view(['GET'])
def competition_memberships_info(request):
    competitionmemberships = CompetitionMembership.objects.all()
    serializer = CompetitionMembershipInfoSerializer({
        'competitionmemberships': competitionmemberships,
        'count': len(competitionmemberships),
    })

    return Response(serializer.data)
