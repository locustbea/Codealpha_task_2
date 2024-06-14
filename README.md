# Job Board

## Overview
The Job Board is a web application that allows users to browse job listings, post job openings, and apply for jobs. It is built using Django (Python) for the backend framework by Olalekan Onifade.

## Features
- User registration and authentication
- Job posting by employers
- Job search and filtering
- Job application by users
- Employer dashboard for managing job postings

## Technologies Used
- Python
- Django
- SQLite (default database, can be replaced with PostgreSQL or MySQL)
- HTML/CSS for front-end

## Installation

### Prerequisites
- Python 3.8 or higher
- Django 4.0 or higher

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/locustbea/job_board.git
    cd job_board
    ```

2. Set up a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser for admin access:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and navigate to `http://127.0.0.1:8000/` to access the application.

## Directory Structure

job_board/
├── job_board/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
├── jobs/
│ ├── migrations/
│ ├── templates/
│ │ └── jobs/
│ │ ├── job_detail.html
│ │ ├── job_list.html
│ │ ├── index.html
│ │ ├── job_form.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
├── users/
│ ├── migrations/
│ ├── templates/
│ │ └── users/
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── dashboard.html
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
├── manage.py
└── requirements.txt

markdown


## Usage
1. Register and log in as a user.
2. Browse and search for jobs.
3. Apply for jobs.
4. Employers can post new job openings.
5. Employers can manage their job postings via the dashboard.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
