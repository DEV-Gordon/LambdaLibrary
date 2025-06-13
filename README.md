# Lambda Library

The Lambda Library is a Django-based digital library platform designed for managing and sharing 3D models and other digital resources. It provides a robust system for organizing content, managing users, and facilitating content discovery through search and categorization.

## Features

* **Digital Resource Management:** Supports various file types for digital resources, including 3D models, and allows for custom preview images.
* **User and Content Management:** Includes an author management system (integrated with Django's built-in User model), category-based organization for resources, and download tracking.
* **Content Highlighting:** Ability to highlight featured content on the homepage.
* **Rich Media Support:** Supports multiple images per resource to provide comprehensive visual information.
* **Search and Filter:** Powerful search and filtering capabilities to help users quickly find the resources they need.
* **User Profiles:** Users can manage their uploaded posts through a dedicated profile page.
* **Authentication System:** Full-featured user authentication including login, logout, password change, and password reset functionalities.

## Technical Stack

* **Backend:** Python 3.x, Django 5.0.2
* **Database:** SQLite (for development), configurable for production databases like PostgreSQL, MySQL.
* **Image Processing:** Pillow 10.2.0
* **Frontend:** HTML, CSS, JavaScript (primarily Django's templating engine)

## Installation

Follow these steps to set up the Lambda Library locally:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/dev-gordon/lambdalibrary.git](https://github.com/dev-gordon/lambdalibrary.git)
    cd lambdalibrary
    ```

2.  **Create and activate a Python virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run database migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser** (for administrative access to the Django admin panel):

    ```bash
    python manage.py createsuperuser
    ```

6.  **Start the development server:**

    ```bash
    python manage.py runserver
    ```

## Project Structure
The project is organized as follows:
```
LambdaLibrary/
├── Lambda/                # Main Django project settings
│   ├── asgi.py
│   ├── settings.py        # Project settings
│   ├── urls.py            # Main URL configurations
│   └── wsgi.py
├── Library/               # Main digital library application
│   ├── admin.py           # Django admin configurations
│   ├── apps.py
│   ├── forms.py           # Forms for creating/updating posts
│   ├── migrations/        # Database migrations
│   │   ├── 0001_initial.py
│   │   └── 0002_alter_posts_author_delete_author.py
│   ├── models.py          # Database models (Category, Posts, PostImage)
│   ├── tests.py
│   ├── urls.py            # Application-specific URL configurations
│   └── views.py           # Logic for handling requests and rendering templates
├── media/                 # Directory for user-uploaded files (e.g., 3D models, images)
├── static/                # Directory for static files (CSS, JS, images)
├── templates/             # HTML templates for the project
│   ├── Library/           # Templates specific to the Library app
│   │   ├── backup.html
│   │   ├── category.html
│   │   ├── home.html
│   │   ├── post_detail.html
│   │   └── users/         # User-related post management templates
│   │       ├── manage_posts.html
│   │       ├── post_confirm_delete.html
│   │       └── post_form.html
│   ├── registration/      # Django authentication templates
│   │   ├── login.html
│   │   ├── password_change_done.html
│   │   ├── password_change_form.html
│   │   ├── password_reset_complete.html
│   │   ├── password_reset_confirm.html
│   │   ├── password_reset_done.html
│   │   └── password_reset_form.html
│   ├── users/             # User app templates
│   │   ├── profile.html
│   │   └── signup.html
│   └── base.html          # Base template for common layout
├── users/                 # User management application
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py           # User-related views (e.g., signup, profile)
├── manage.py              # Django's command-line utility
└── requirements.txt       # Python dependencies

    The application will be accessible at `http://127.0.0.1:8000/`.
```
## Database Models

### `Library` Application Models:

* **`Category`**: Represents categories for organizing digital resources.
* **`Posts`**: The core model for digital resources.
    * `file_attachments`: The actual digital resource file (e.g., 3D model).
    * `title`: Title of the post.
    * `description`: Detailed description of the resource.
    * `author`: Foreign key to Django's built-in `User` model.
    * `category`: Foreign key to the `Category` model.
    * `preview_image`: Optional preview image for the resource.
    * `date_posted`: Timestamp of creation.
    * `date_updated`: Timestamp of last update.
    * `download_count`: Tracks the number of downloads for the resource.
    * `is_published`: Boolean indicating if the post is publicly visible.
    * `is_featured`: Boolean indicating if the post should be highlighted.
* **`PostImage`**: Stores additional images associated with a `Posts` instance.

## Views and Functionality

The `Library` app's views provide the following functionalities:

* **`HomeView`**: Displays a paginated list of published posts, highlighting featured posts and categories.
* **`CategoryView`**: Shows paginated posts belonging to a specific category.
* **`PostDetailView`**: Displays detailed information for a single post, including related models from the same category.
* **`PostCreateView`**: Allows authenticated users to create new posts.
* **`PostUpdateView`**: Enables the author of a post to update its details.
* **`PostDeleteView`**: Allows the author of a post to delete it.
* **`UserPostsListView`**: Displays all posts created by the currently logged-in user.
* **`download_post`**: Handles file downloads and increments the download count for a post.

The `users` app handles user authentication and profile management, including:

* **`SignUpView`**: User registration.
* **`profile`**: Displays the user's profile and their uploaded models.

Django's built-in authentication views are utilized for login, logout, password change, and password reset.
