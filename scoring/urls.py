import uuid
from django.urls import path
from . import views

urlpatterns = [
    path('archers/', views.archer_list),
    path('archers/info/', views.archer_info),
    path('archers/<uuid:pk>/', views.archer_detail),

    path('disciplines/', views.discipline_list),
    path('disciplines/info/', views.discipline_info),
    path('disciplines/<uuid:pk>/', views.discipline_detail),

    path('disciplinememberships/', views.discipline_memberships_list),
    path('disciplinememberships/info/', views.discipline_memberships_info),
    path('disciplinememberships/<uuid:pk>/', views.discipline_memberships_detail),

    path('clubs/', views.club_list),
    path('clubs/info/', views.club_info),
    path('clubs/<uuid:pk>/', views.club_detail),

    path('clubmemberships/', views.club_memberships_list),
    path('clubmemberships/info/', views.club_memberships_info),
    path('clubmemberships/<uuid:pk>/', views.club_memberships_detail),

    path('categories/', views.category_list),
    path('categories/info/', views.category_info),
    path('categories/<uuid:pk>/', views.category_detail),

    path('agegroups/', views.agegroup_list),
    path('agegroups/info/', views.agegroup_info),
    path('agegroups/<uuid:pk>/', views.agegroup_detail),

    path('categorymemberships/', views.category_memberships_list),
    path('categorymemberships/info/', views.category_memberships_info),
    path('categorymemberships/<uuid:pk>/', views.category_memberships_detail),

    path('teams/', views.team_list),
    path('teams/info/', views.team_info),
    path('teams/<uuid:pk>/', views.team_detail),

    path('teammemberships/', views.team_memberships_list),
    path('teammemberships/info/', views.team_memberships_info),
    path('teammemberships/<uuid:pk>/', views.team_memberships_detail),

    path('scoringsheets/', views.scoringsheet_list),
    path('scoringsheets/info/', views.scoringsheet_info),
    path('scoringsheets/<uuid:pk>/', views.scoringsheet_detail),
    
    path('targetfacenamechoices/', views.targetfacenamechoice_list),
    path('targetfacenamechoices/info/', views.targetfacenamechoice_info),
    path('targetfacenamechoices/<uuid:pk>/', views.targetfacenamechoice_detail),
    
    path('targetfaces/', views.targetface_list),
    path('targetfaces/info/', views.targetface_info),
    path('targetfaces/<uuid:pk>/', views.targetface_detail),

    path('rounds/', views.round_list),
    path('rounds/info/', views.round_info),
    path('rounds/<uuid:pk>/', views.round_detail),

    path('roundmemberships/', views.round_memberships_list),
    path('roundmemberships/info/', views.round_memberships_info),
    path('roundmemberships/<uuid:pk>/', views.round_memberships_detail),

    path('scores/', views.score_list),
    path('scores/info/', views.score_info),
    path('scores/<uuid:pk>/', views.score_detail),

    path('competitions/', views.competition_list),
    path('competitions/info/', views.competition_info),
    path('competitions/<uuid:pk>/', views.competition_detail),

    path('competitionmemberships/', views.competition_memberships_list),
    path('competitionmemberships/info/', views.competition_memberships_info),
    path('competitionmemberships/<uuid:pk>/', views.competition_memberships_detail),
]

