## Development Setup

Clone the repository

    git clone https://github.com/9bit-Jedi/JumbleApp.git

Setup Virtual Environment

    py -m venv .venv

    .\.venv\Scripts\activate

Enter working directory

    cd .\JumbleApp\

Install dependencies
   
    pip install -r requirements.txt

Migrate & Create super user (Only if recreating DB)
https://docs.djangoproject.com/en/5.0/topics/migrations/#module-django.db.migrations

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

Run Development server (ASGI apps)

    daphne JumbleApp.asgi:application
