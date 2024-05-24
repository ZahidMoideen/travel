Installation Instructions:
Clone the repository:
Command: git clone https://github.com/ZahidMoideen/travel.git
Command: cd travel_app
Set up virtual environment:
Command: python -m venv venv
Command: venv\Scripts\activate.bat
Install dependencies:
Command: pip install -r requirements.txt
Apply migrations:
Command: py manage.py migrate
Run the server:
Command: py manage.py runserver
create superuser: 
command: py manage.py createsuperuser
login with super user:
command: (http://127.0.0.1:8000/admin)
Access the application:
URL: http://127.0.0.1:8000/
Usage Instructions
Register a new user at: http://127.0.0.1:8000/register/
Add destinations at: http://127.0.0.1:8000/destinations/
Edit or delete destinations by appending the destination ID to: http://127.0.0.1:8000/destinations/{id}
Project Structure

travel_app/ - Main project folder.
manage.py - Django's command-line utility for administrative tasks.
requirements.txt - List of required packages.