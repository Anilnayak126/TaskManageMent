# Task Management App with Google Login

This project is a Task Management application built with Django, featuring Google OAuth2 for user authentication. It was developed as an assessment project.

## Project Setup

### Django Project
- Create a new Django project.
- Set up an app for task management and user authentication.

### Google Cloud Platform
- Create a new Google Cloud Platform project.
- Enable the Google OAuth API.
- Create OAuth client ID and secret.
- Configure the OAuth consent screen.

## Authentication and Authorization

### Google Login
- Integrate Google OAuth2 client library into Django.
- Handle Google's OAuth flow (authorization code grant).
- Store user information (email, name) in Django's User model.

### User Permissions
- Implement admin and user roles.
- Use Django's built-in permissions system or custom permissions.
- Restrict admin actions to authorized users.

## Task Management

### Task Model
- Create a Task model with fields for title, description, and user.

### Task Views
- Create views for:
  - Displaying a list of tasks.
  - Creating new tasks.
  - Editing existing tasks.
  - Deleting tasks.

### Task Templates
- Design templates for:
  - Task list.
  - Task creation form.
  - Task edit form.

## Admin Panel

### Admin Interface
- Use Django's built-in admin interface to manage tasks and users.
- Customize the admin interface for a better user experience.

### OAuth Key Management
- Create an admin model to store Google OAuth client ID and secret.
- Allow admins to update these keys.

### User Invitation
- Implement a mechanism for admins to send invitation emails.
- Generate unique registration links for invited users.

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Anilnayak126/TaskManagement.git
    cd TaskManagement
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Configuration

1. Set up your Google OAuth credentials in the Django models socialaccountsModel:
    ```python
    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'your-client-id'
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'your-client-secret'
    ```

2. Configure the OAuth consent screen on Google Cloud Platform.

## Usage

- Access the application at `http://localhost:8000`.
- Log in using your Google account.
- Manage tasks through the user interface.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
