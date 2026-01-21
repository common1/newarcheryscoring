from django.test import TestCase
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
from userauth.models import CustomUser
from django.urls import reverse
from rest_framework import status

class UserArcherTestCase(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create_user(username='user1', password='test')
        user2 = CustomUser.objects.create_user(username='user2', password='test')
        Archer.objects.create(author=user1)
        Archer.objects.create(author=user2)

        return super().setUp()

    def test_user_archer_endpoint_retrieves_only_authenticated_user_archers(self):
        user = CustomUser.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-archers'))

        assert response.status_code == status.HTTP_200_OK
        archers = response.json()
        self.assertTrue(all(archer['author'] == user.id for archer in archers))

    def test_user_archer_list_unauthenticated(self):
        response = self.client.get(reverse('user-archers'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserDisciplineTestCase(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create_user(username='user1', password='test')
        user2 = CustomUser.objects.create_user(username='user2', password='test')
        Discipline.objects.create(author=user1, name='discipline1')
        Discipline.objects.create(author=user2, name='discipline2')

        return super().setUp()

    def test_user_discipline_endpoint_retrieves_only_authenticated_user_disciplines(self):
        user = CustomUser.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-disciplines'))

        assert response.status_code == status.HTTP_200_OK
        disciplines = response.json()
        self.assertTrue(all(discipline['author'] == user.id for discipline in disciplines))

    def test_user_discipline_list_unauthenticated(self):
        response = self.client.get(reverse('user-disciplines'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserClubTestCase(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create_user(username='user1', password='test')
        user2 = CustomUser.objects.create_user(username='user2', password='test')
        Club.objects.create(author=user1, name='club1')
        Club.objects.create(author=user2, name='club2')

        return super().setUp()

    def test_user_club_endpoint_retrieves_only_authenticated_user_clubs(self):
        user = CustomUser.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-clubs'))

        assert response.status_code == status.HTTP_200_OK
        clubs = response.json()
        self.assertTrue(all(club['author'] == user.id for club in clubs))

    def test_user_club_list_unauthenticated(self):
        response = self.client.get(reverse('user-clubs'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserCategoryTestCase(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create_user(username='user1', password='test')
        user2 = CustomUser.objects.create_user(username='user2', password='test')
        Category.objects.create(author=user1, name='category1')
        Category.objects.create(author=user2, name='category2')

        return super().setUp()

    def test_user_category_endpoint_retrieves_only_authenticated_user_categories(self):
        user = CustomUser.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-categories'))

        assert response.status_code == status.HTTP_200_OK
        categories = response.json()
        self.assertTrue(all(category['author'] == user.id for category in categories))

    def test_user_category_list_unauthenticated(self):
        response = self.client.get(reverse('user-categories'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserAgeGroupTestCase(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create_user(username='user1', password='test')
        user2 = CustomUser.objects.create_user(username='user2', password='test')
        AgeGroup.objects.create(author=user1, name='agegroup1')
        AgeGroup.objects.create(author=user2, name='agegroup2')

        return super().setUp()

    def test_user_agegroup_endpoint_retrieves_only_authenticated_user_agegroups(self):
        user = CustomUser.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-agegroups'))

        assert response.status_code == status.HTTP_200_OK
        agegroups = response.json()
        self.assertTrue(all(agegroup['author'] == user.id for agegroup in agegroups))

    def test_user_agegroup_list_unauthenticated(self):
        response = self.client.get(reverse('user-agegroups'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserTeamTestCase(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create_user(username='user1', password='test')
        user2 = CustomUser.objects.create_user(username='user2', password='test')
        Team.objects.create(author=user1, name='team1')
        Team.objects.create(author=user2, name='team2')

        return super().setUp()

    def test_user_team_endpoint_retrieves_only_authenticated_user_teams(self):
        user = CustomUser.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-teams'))

        assert response.status_code == status.HTTP_200_OK
        teams = response.json()
        self.assertTrue(all(team['author'] == user.id for team in teams))

    def test_user_team_list_unauthenticated(self):
        response = self.client.get(reverse('user-teams'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserScoringSheetTestCase(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create_user(username='user1', password='test')
        user2 = CustomUser.objects.create_user(username='user2', password='test')
        ScoringSheet.objects.create(author=user1, name='scoringsheet1')
        ScoringSheet.objects.create(author=user2, name='scoringsheet2')

        return super().setUp()

    def test_user_scoringsheet_endpoint_retrieves_only_authenticated_user_scoringsheets(self):
        user = CustomUser.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-scoringsheets'))

        assert response.status_code == status.HTTP_200_OK
        scoringsheets = response.json()
        self.assertTrue(all(scoringsheet['author'] == user.id for scoringsheet in scoringsheets))

    def test_user_scoringsheet_list_unauthenticated(self):
        response = self.client.get(reverse('user-scoringsheets'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserTargetFaceNameChoiceTestCase(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create_user(username='user1', password='test')
        user2 = CustomUser.objects.create_user(username='user2', password='test')
        TargetFaceNameChoice.objects.create(author=user1, name='targetfacenamechoice1')
        TargetFaceNameChoice.objects.create(author=user2, name='targetfacenamechoice2')

        return super().setUp()

    def test_user_targetfacenamechoice_endpoint_retrieves_only_authenticated_user_targetfacenamechoices(self):
        user = CustomUser.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-targetfacenamechoices'))

        assert response.status_code == status.HTTP_200_OK
        targetfacenamechoices = response.json()
        self.assertTrue(all(targetfacenamechoice['author'] == user.id for targetfacenamechoice in targetfacenamechoices))

    def test_user_targetfacenamechoice_list_unauthenticated(self):
        response = self.client.get(reverse('user-targetfacenamechoices'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserTargetFaceTestCase(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create_user(username='user1', password='test')
        user2 = CustomUser.objects.create_user(username='user2', password='test')
        TargetFace.objects.create(author=user1, name='targetface1')
        TargetFace.objects.create(author=user2, name='targetface2')

        return super().setUp()

    def test_user_targetface_endpoint_retrieves_only_authenticated_user_targetfaces(self):
        user = CustomUser.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-targetfaces'))

        assert response.status_code == status.HTTP_200_OK
        targetfaces = response.json()
        self.assertTrue(all(targetface['author'] == user.id for targetface in targetfaces))

    def test_user_targetface_list_unauthenticated(self):
        response = self.client.get(reverse('user-targetfaces'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserRoundTestCase(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create_user(username='user1', password='test')
        user2 = CustomUser.objects.create_user(username='user2', password='test')
        Round.objects.create(author=user1, name='round1')
        Round.objects.create(author=user2, name='round2')

        return super().setUp()

    def test_user_round_endpoint_retrieves_only_authenticated_user_rounds(self):
        user = CustomUser.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-rounds'))

        assert response.status_code == status.HTTP_200_OK
        rounds = response.json()
        self.assertTrue(all(round['author'] == user.id for round in rounds))

    def test_user_round_list_unauthenticated(self):
        response = self.client.get(reverse('user-rounds'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserScoreTestCase(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create_user(username='user1', password='test')
        user2 = CustomUser.objects.create_user(username='user2', password='test')
        Score.objects.create(author=user1, score=270, number_of_arrows=30)
        Score.objects.create(author=user2, score=280, number_of_arrows=30)

        return super().setUp()

    def test_user_score_endpoint_retrieves_only_authenticated_user_scores(self):
        user = CustomUser.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-scores'))

        assert response.status_code == status.HTTP_200_OK
        scores = response.json()
        self.assertTrue(all(score['author'] == user.id for score in scores))

    def test_user_score_list_unauthenticated(self):
        response = self.client.get(reverse('user-scores'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class UserCompetitionTestCase(TestCase):
    def setUp(self):
        user1 = CustomUser.objects.create_user(username='user1', password='test')
        user2 = CustomUser.objects.create_user(username='user2', password='test')
        Competition.objects.create(author=user1, name='competition1')
        Competition.objects.create(author=user2, name='competition2')

        return super().setUp()

    def test_user_competition_endpoint_retrieves_only_authenticated_user_competitions(self):
        user = CustomUser.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-competitions'))

        assert response.status_code == status.HTTP_200_OK
        competitions = response.json()
        self.assertTrue(all(competition['author'] == user.id for competition in competitions))

    def test_user_competition_list_unauthenticated(self):
        response = self.client.get(reverse('user-competitions'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
