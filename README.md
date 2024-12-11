# Flashscore Project

## Team Members
- **Bagytzhan Zhalgas** (22B030317)  
- **Mussilimov Galymzhan** (22B031186)  
- **Kyanysh Farabi** (22B030489)

---

## Overview
Flashscore is a football-focused web application built with Django. It offers comprehensive data about football leagues, teams, players, coaches, and matches. The application supports multiple user roles, including Administrator, Journalist, and Regular User, each with distinct permissions and access levels.

---

## Project Structure

### 1. Users Application
**Purpose:** Manages user authentication and roles (Admin, Journalist, Regular User).  
**Key Features:**
- User registration and login.
- Role management and permissions.
- Profile updates.

### 2. News Application
**Purpose:** Facilitates the creation and viewing of football-related news articles.  
**Key Features:**
- CRUD operations for news articles (available to Journalists and Admins).
- Display of the latest football news for all users.

### 3. Scores Application
**Purpose:** Provides detailed data about football leagues, teams, players, coaches, and matches.  
**Key Features:**
- League tables and statistics.
- Team rosters, including player and coach details.
- Match schedules and results.

---

## Core Features

### 1. Models
- **Users:** Custom user model with roles and authentication settings.
- **News:** Models for creating and managing news articles.
- **Scores:** Models for leagues, teams, players, coaches, and matches.

**Relationships Between Models:**
- **One-to-Many:** A league can have many teams, but a team belongs to one league.
- **Many-to-Many:** Teams can play against multiple opponents in different matches.

**Custom Methods:** Business logic is implemented directly in models when required.

### 2. Views
- **CRUD Operations:** Create, Read, Update, and Delete functionality for managing data (e.g., news, matches).
- **GET Views:** List and detail views for entities like teams, leagues, and matches.
- **POST Views:** Form submissions for creating or updating content, such as news articles or profiles.

### 3. Templates
- At least six templates utilizing Django's template inheritance for consistent layouts.
- Styling incorporates Bootstrap or a similar CSS framework for a modern, responsive design.

### 4. API Development (DRF)
- **Endpoints:** CRUD API endpoints for teams, players, matches, and leagues.
- **Authentication:** Token-based authentication using JWT.
- **Testing:** Endpoints tested with tools like Postman or cURL.
- **Documentation:** API documentation available for developers.

---

## Authentication & Role-Based Access Control
- **JWT Authentication:** Secures API endpoints and user sessions.
- **Role Permissions:**
  - **Admin:** Full access to view, edit, and delete all data (users, teams, matches, etc.).
  - **Journalist:** Permissions to create and edit news articles.
  - **User:** Read-only access to news, teams, and matches, with the ability to comment.

---

## Scores Application

### 1. Sports
The fundamental model that holds a list of popular sports. Each sport entry consists of key attributes, including associated leagues.

### 2. Leagues
A model that represents different leagues, organized by countries or other relevant categories. Leagues are associated with specific sports.

### 3. Teams
This model manages sports teams, which are grouped under different leagues.

### 4. Matches
This model holds detailed information about games, including:
- Points and positions.
- Teams and other attributes.

### 5. Coaches
The Coaches model provides detailed information about coaches, including their team affiliations.

### Analytics
- **Basic Insights:** Tracks average team points and league standings.
- **Visualizations:** Created using libraries like Matplotlib to display charts and graphs.

---

## Database Setup
- **Schema:** Reflects relationships between models using Django's `ForeignKey` and `ManyToManyField`.
- **Optimization:** Indexing applied for faster query performance.

---

## Logging
- Logs track significant actions such as user logins, API access, and data modifications.

---

## Suggestions for Visual Enhancements
1. **User Roles and Permissions:** Add a diagram illustrating the hierarchy of roles and their permissions.
2. **News Creation:** Include a screenshot of the news creation interface or form.
3. **Scores Section:** Display a sample league table or match schedule.
4. **API Documentation:** Add a screenshot of API documentation or Postman tests.
5. **Analytics:** Include graphs showing team performance or match statistics.
6. **Landing Page:** Showcase the homepage with a clean and attractive design.

---

