# Lambda Library

A Django-based digital library platform for managing and sharing 3D models and digital resources.

## Features

- Digital resource management system
- Support for multiple file types and preview images
- Author management system
- Category-based organization
- Download tracking
- Featured content highlighting
- Multiple image support per resource
- Search and filter capabilities

## Tech Stack

- Python 3.x
- Django 5.0.2
- Pillow 10.2.0
- SQLite (Development)
- HTML/CSS/JavaScript

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/lambda-library.git
cd lambda-library
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
LambdaLibrary/
├── Library/              # Main application
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── urls.py          # URL routing
│   └── admin.py         # Admin interface configuration
├── templates/           # HTML templates
├── media/              # User-uploaded files
├── static/             # Static files
└── manage.py           # Django management script
```

## Models

- **Category**: Resource categorization
- **Author**: Content creator management
- **Posts**: Main resource model with file attachments
- **PostImage**: Additional images for resources

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)
Project Link: [https://github.com/yourusername/lambda-library](https://github.com/yourusername/lambda-library) 
