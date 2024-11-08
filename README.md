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
- **File and Folder Navigation**: Browse files and folders easily on a user-friendly web UI.
- **File Properties and Metadata Display**: View detailed properties and metadata for each file.
- **File Upload and Folder Creation**: Upload files (up to 40 MB) and create folders to organize files efficiently.
- **File Management**: Move and copy files and folders within the app for better organization.
- **Storage Limits**: Each account has a drive limit of 100 MB, preventing individual folders from exceeding this storage cap.
- **Account Info Dashboard**: Visualize storage usage with statistics and graphics, including space distribution by file format (images, documents, videos, etc.).
- **File Previews**: Preview common file types, including images, videos, PDFs, source code, and documents, for convenient access.
- **Responsive Design**: Beautiful, responsive UX designed for both laptops and smartphones, ensuring optimal experience across devices.
- **Enhanced Media Capabilities**: Open text files, view images, and play videos directly within the app 
- **Dockerized**: Containerized with Docker for streamlined deployment and development.

## Tech Stack

```plaintext
Frontend: Tailwind CSS, Material UI, JavaScript
Backend: Django, Django REST Framework
Database: SQLite (default)
Containerization: Docker


## 🛠️ **Getting Started with JuniaDrive**

JuniaDrive offers two setup options: Docker or a local development environment

### Option 1: Running with Docker

1. Ensure Docker is Installed: Make sure Docker and Docker Compose are installed on your machine.

2. Build and Run the Docker Containers:
   ```bash
   docker-compose up --build
   ```
3.Access the Application: Go to [http://localhost:8000](http://localhost:8000) to start using JuniaDrive.

### Option 2: Run Locally (Development Mode)

1. **Install Dependencies**:
   - Ensure Python and pip are installed on your machine.
   - Install required packages:
     ```bash
     pip install -r requirements.txt
     ```

2. **Set Up Database**:
   - If running locally, use the SQLite database by uncommenting the relevant section in `settings.py`.

3. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

4. **(Optional) Create an Admin User:** If you’d like to access the admin panel, create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. Access the application at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 🖼️ **Screenshots**

Take a look at some screenshots of SkyVault in action:

### 1️⃣ **Sign Up**
![Home](/juniaDrive/accounts/static/images//signup.png)

> *Signup Page*

### 2️⃣ **Login**
![Dashboard](/juniaDrive/accounts/static/images/login.png)

> *Login page*

### 3️⃣ **Home Page**
![Home](/juniaDrive/accounts/static/images/home.png)

> *Users home page*


### 4️⃣ **Empty Folder**
![Trash](/juniaDrive/accounts/static/images/empty_folder.png)


### 5️⃣ **File Upload**
![Info](/juniaDrive/accounts/static/images/file_upload.png)

> *Gives you access to copy, delete, download a file, and to also move a file to a different folder*

### 6️⃣ **File Dashboar**
![Info](/juniaDrive/accounts/static/images/dashboard.png)

> *Access detailed information and usage statistics for your account.*

---

---

## 📝 **License**

JuniaDrive is licensed under the MIT License.

--- 

