# Django-project
This project is a sports management platform inspired by Flashscore, aimed at creating a web application to track sports data such as teams, leagues, players, and coaches. The platform also allows users to register, manage profiles, and interact with sports content through a CRUD interface.

## Team Members:

      Bagytzhan Zhalgas (22B030317)
      Mussilimov Galymzhan (22B031186)
      Kyanysh Farabi (22B030489)
      
# Project Structure

This project consists of two main applications:

      Scores
      Users

# 1. Scores Application

The Scores app is responsible for managing sports data, including various models like Sports, Leagues, Teams, Players, and Coaches. Each of these models has full CRUD (Create, Read, Update, Delete) functionality.

Models Overview

      1.1 Sports
      
      The fundamental model that holds a list of popular sports. Each sport entry consists of key attributes, including associated leagues.
      
      1.2 Leagues
      
      A model that represents different leagues, organized by countries or other relevant categories. Leagues are associated with specific sports.
      
      1.3 Teams
      
      This model manages sports teams, which are grouped under different leagues.
      
      1.4 Players
      
      This model holds detailed information about players, including:
      
      Player's name
      Position
      Team affiliation
      Player's number, and other attributes.
      
      1.5 Coaches
      
      The Coaches model provides detailed information about coaches, including their team affiliation.

## CRUD Operations

Each model has its own set of CRUD operations to manage the data. Below are the URLs for the CRUD views of each model:

      Sport CRUD
      - Create:       /sport/create/
      - Detail:       /sport/<int:id>/
      - Update:       /sport/<int:id>/update/
      - Delete:       /sport/<int:id>/delete/


      League CRUD
      - Create:       /league/create/
      - Detail:       /league/<int:id>/
      - Update:       /league/<int:id>/update/
      - Delete:       /league/<int:id>/delete/


      Team CRUD
      - Create:       /team/create/
      - Detail:       /team/<int:id>/
      - Update:       /team/<int:id>/update/
      - Delete:       /team/<int:id>/delete/


      Player CRUD
      - Create:       /player/create/
      - Detail:       /player/<int:id>/
      - Update:       /player/<int:id>/update/
      - Delete:       /player/<int:id>/delete/

      Coach CRUD
      - Create:       /coach/create/
      - Detail:       /coach/<int:id>/
      - Update:       /coach/<int:id>/update/
      - Delete:       /coach/<int:id>/delete/



## Global Search

A search system allows users to search across all sports, teams, players, and coaches.

The search logic:

    def global_search(request):
    query = request.GET.get('q')
    sports = Sport.objects.filter(name__icontains=query) if query else []
    teams = Team.objects.filter(name__icontains=query) if query else []
    players = Player.objects.filter(firstname__icontains=query) | Player.objects.filter(lastname__icontains=query) if query else []
    coaches = Coach.objects.filter(firstname__icontains=query) | Coach.objects.filter(lastname__icontains=query) if query else []

    context = {
        'query': query,
        'sports': sports,
        'teams': teams,
        'players': players,
        'coaches': coaches
    }
    return render(request, 'scores/search_results.html', context)

# 2. Users Application

This app is focused on user authentication and profile management. It provides:

      User Registration: Users can create a profile.
      Login/Logout System: Registered users can log in to access additional features.
      Profile Management: Users can view and edit their profile details.
      
User Registration & Authentication

      Users can sign up, log in, and log out.
      Profile management allows users to modify their personal information.
