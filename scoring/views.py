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
    IsAdminUser,
    AllowAny,
)
from rest_framework.views import APIView

# Archer

class ArcherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Archer.objects.all()
    serializer_class = ArcherSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class ArcherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Archer.objects.all()
    serializer_class = ArcherSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserArcherListAPIView(generics.ListAPIView):
    queryset = Archer.objects.all()
    serializer_class = ArcherSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class ArcherInfoAPIView(APIView):
    def get(self, request):
        archers = Archer.objects.all()
        serializer = ArcherInfoSerializer({
            'archers': archers,
            'count': len(archers),
        })
        
        return Response(serializer.data)

# Discipline

class DisciplineListCreateAPIView(generics.ListCreateAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class DisciplineDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserDisciplineListAPIView(generics.ListAPIView):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class DisciplineInfoAPIView(APIView):
    def get(self, request):
        disciplines = Discipline.objects.prefetch_related(
            'archers',
        )
        serializer = DisciplineInfoSerializer({
            'disciplines': disciplines,
            'count': len(disciplines),
        })
        
        return Response(serializer.data)

# DisciplineMembership

class DisciplineMembershipListCreateAPIView(generics.ListCreateAPIView):
    queryset = DisciplineMembership.objects.all()
    serializer_class = DisciplineMembershipSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class DisciplineMembershipDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DisciplineMembership.objects.all()
    serializer_class = DisciplineMembershipSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserDisciplineMembershipListAPIView(generics.ListAPIView):
    queryset = DisciplineMembership.objects.all()
    serializer_class = DisciplineMembershipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class DisciplineMembershipInfoAPIView(APIView):
    def get(self, request):
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

class ClubListCreateAPIView(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class ClubDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserClubListAPIView(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class ClubInfoAPIView(APIView):
    def get(self, request):
        clubs = Club.objects.prefetch_related(
            'archers',
        )
        serializer = ClubInfoSerializer({
            'clubs': clubs,
            'count': len(clubs),
        })
        
        return Response(serializer.data)

# ClubMembership

class ClubMembershipListCreateAPIView(generics.ListCreateAPIView):
    queryset = ClubMembership.objects.all()
    serializer_class = ClubMembershipSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class ClubMembershipDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClubMembership.objects.all()
    serializer_class = ClubMembershipSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserClubMembershipListAPIView(generics.ListAPIView):
    queryset = ClubMembership.objects.all()
    serializer_class = ClubMembershipSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class ClubMembershipInfoAPIView(APIView):
    def get(self, request):
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

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserCategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class CategoryInfoAPIView(APIView):
    def get(self, request):
        categories = Category.objects.prefetch_related(
            'archers',
        )
        serializer = CategoryInfoSerializer({
            'categories': categories,
            'count': len(categories),
        })
        
        return Response(serializer.data)

# AgeGroup

class AgeGroupListCreateAPIView(generics.ListCreateAPIView):
    queryset = AgeGroup.objects.all()
    serializer_class = AgeGroupSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class AgeGroupDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgeGroup.objects.all()
    serializer_class = AgeGroupSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserAgeGroupListAPIView(generics.ListAPIView):
    queryset = AgeGroup.objects.all()
    serializer_class = AgeGroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class AgeGroupInfoAPIView(APIView):
    def get(self, request):
        agegroups = AgeGroup.objects.all()
        serializer = AgeGroupInfoSerializer({
            'agegroups': agegroups,
            'count': len(agegroups),
        })
        
        return Response(serializer.data)

# CategoryMembership

class CategoryMembershipListCreateAPIView(generics.ListCreateAPIView):
    queryset = CategoryMembership.objects.all()
    serializer_class = CategoryMembershipSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class CategoryMembershipDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryMembership.objects.all()
    serializer_class = CategoryMembershipSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserCategoryMembershipListAPIView(generics.ListAPIView):
    queryset = CategoryMembership.objects.all()
    serializer_class = CategoryMembershipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class CategoryMembershipInfoAPIView(APIView):
    def get(self, request):
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

class TeamListCreateAPIView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class TeamDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserTeamListAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class TeamInfoAPIView(APIView):
    def get(self, request):
        teams = Team.objects.prefetch_related(
            'archers',
        )
        serializer = TeamInfoSerializer({
            'teams': teams,
            'count': len(teams),
        })
        
        return Response(serializer.data)

# TeamMembership

class TeamMembershipListCreateAPIView(generics.ListCreateAPIView):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class TeamMembershipDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserTeamMembershipListAPIView(generics.ListAPIView):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class TeamMembershipInfoAPIView(APIView):
    def get(self, request):
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

class ScoringSheetListCreateAPIView(generics.ListCreateAPIView):
    queryset = ScoringSheet.objects.all()
    serializer_class = ScoringSheetSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class ScoringSheetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScoringSheet.objects.all()
    serializer_class = ScoringSheetSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserScoringSheetListAPIView(generics.ListAPIView):
    queryset = ScoringSheet.objects.all()
    serializer_class = ScoringSheetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class ScoringSheetInfoAPIView(APIView):
    def get(self, request):
        scoringsheets = ScoringSheet.objects.all()
        serializer = ScoringSheetInfoSerializer({
            'scoringsheets': scoringsheets,
            'count': len(scoringsheets),
        })
        
        return Response(serializer.data)

# TargetFaceNameChoice

class TargetFaceNameChoiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = TargetFaceNameChoice.objects.all()
    serializer_class = TargetFaceNameChoiceSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class TargetFaceNameChoiceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TargetFaceNameChoice.objects.all()
    serializer_class = TargetFaceNameChoiceSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserTargetFaceNameChoiceListAPIView(generics.ListAPIView):
    queryset = TargetFaceNameChoice.objects.all()
    serializer_class = TargetFaceNameChoiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class TargetFaceNameChoiceInfoAPIView(APIView):
    def get(self, request):
        targetfacenamechoices = TargetFaceNameChoice.objects.all()
        serializer = TargetFaceNameChoiceInfoSerializer({
            'targetfacenamechoices': targetfacenamechoices,
            'count': len(targetfacenamechoices),
        })
        
        return Response(serializer.data)

# TargetFace

class TargetFaceListCreateAPIView(generics.ListCreateAPIView):
    queryset = TargetFace.objects.all()
    serializer_class = TargetFaceSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class TargetFaceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TargetFace.objects.all()
    serializer_class = TargetFaceSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserTargetFaceListAPIView(generics.ListAPIView):
    queryset = TargetFace.objects.all()
    serializer_class = TargetFaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class TargetFaceInfoAPIView(APIView):
    def get(self, request):
        targetfaces = TargetFace.objects.all()
        serializer = TargetFaceInfoSerializer({
            'targetfaces': targetfaces,
            'count': len(targetfaces),
        })
        
        return Response(serializer.data)

# Round

class RoundListCreateAPIView(generics.ListCreateAPIView):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class RoundDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer

class UserRoundListAPIView(generics.ListAPIView):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class RoundInfoAPIView(APIView):
    def get(self, request):
        rounds = Round.objects.prefetch_related(
            'archers',
        )
        serializer = RoundInfoSerializer({
            'rounds': rounds,
            'count': len(rounds),
        })
        
        return Response(serializer.data)

# RoundMembership

class RoundMembershipListCreateAPIView(generics.ListCreateAPIView):
    queryset = RoundMembership.objects.all()
    serializer_class = RoundMembershipSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class RoundMembershipDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoundMembership.objects.all()
    serializer_class = RoundMembershipSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserRoundMembershipListAPIView(generics.ListAPIView):
    queryset = RoundMembership.objects.all()
    serializer_class = RoundMembershipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class RoundMembershipInfoAPIView(APIView):
    def get(self, request):
        roundmemberships = RoundMembership.objects.prefetch_related(
            'round',
            'archer',
        )
        serializer = RoundMembershipInfoSerializer({
            'roundmemberships': roundmemberships,
            'count': len(roundmemberships),
        })
        
        return Response(serializer.data)

# Score

class ScoreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class ScoreDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserScoreListAPIView(generics.ListAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class ScoreInfoAPIView(APIView):
    def get(self, request):
        scores = Score.objects.prefetch_related(
            'round_archer',
        )
        serializer = ScoreInfoSerializer({
            'scores': scores,
            'count': len(scores),
        })
        
        return Response(serializer.data)

# Competition

class CompetitionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class CompetitionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserCompetitionListAPIView(generics.ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class CompetitionInfoAPIView(APIView):
    def get(self, request):
        competitions = Competition.objects.prefetch_related(
            'rounds',
        )
        serializer = CompetitionInfoSerializer({
            'competitions': competitions,
            'count': len(competitions),
        })
        
        return Response(serializer.data)

# CompetitionMembership

class CompetitionMembershipListCreateAPIView(generics.ListCreateAPIView):
    queryset = CompetitionMembership.objects.all()
    serializer_class = CompetitionMembershipSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class CompetitionMembershipDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompetitionMembership.objects.all()
    serializer_class = CompetitionMembershipSerializer

    def get_permissions(self):
        self.permission_classes = [AllowAny]
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class UserCompetitionMembershipListAPIView(generics.ListAPIView):
    queryset = CompetitionMembership.objects.all()
    serializer_class = CompetitionMembershipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author=self.request.user)

class CompetitionMembershipInfoAPIView(APIView):
    def get(self, request):
        competitionmemberships = CompetitionMembership.objects.prefetch_related(
            'competition',
            'round',
        )
        serializer = CompetitionMembershipInfoSerializer({
            'competitionmemberships': competitionmemberships,
            'count': len(competitionmemberships),
        })
        
        return Response(serializer.data)

