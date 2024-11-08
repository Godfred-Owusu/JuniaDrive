# juniaDrive

A web-based file storage and management system built with Django. This application allows users to authenticate, upload, move, copy, and delete files in a user-friendly dashboard. The project is containerized with Docker for easy deployment.

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Getting Started](#getting-started)
4. [Docker Deployment](#docker-deployment)
5. [Project Structure](#project-structure)
6. [Environment Variables](#environment-variables)
7. [Contributing](#contributing)
8. [License](#license)

---

## Features

- **User Authentication**: Register and login functionality.
- **File Management**: Upload, move, copy, and delete files and folders.
- **Metadata Display**: View folder and file metadata.
- **Dashboard**: Real-time file storage statistics.
- **Responsive Design**: Built with Tailwind CSS and Material UI for a modern look.
- **Dockerized**: Containerized for easy deployment with Docker.

## Tech Stack

```plaintext
Frontend: Tailwind CSS, Material UI, JavaScript
Backend: Django, Django REST Framework
Database: PostgreSQL (in Docker), SQLite (default)
Containerization: Docker

Get Started
                                                                                            
# Clone the repository
git clone https://github.com/your-username/juniaDrive.git
cd juniaDrive

# Create a virtual environment
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver


# Build the Docker image
docker build -t juniadrive .

# Run the Docker container
docker run -p 8000:8000 juniadrive
