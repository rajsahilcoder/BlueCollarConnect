# Django Project README

BlueCollarConnect is a Django project that aims to provide a web-based platform that addresses the employment needs of skilled workers by providing job opportunities in close proximity to their residences. Leveraging modern web technologies, the platform aims to connect service providers and job seekers in a seamless manner. [Link: https://github.com/rajsahilcoder/BlueCollarConnect]

## Table of Contents

- [Problem Statement](#problem-statement)
- [Abstract](#abstract)
- [Objectives](#objectives)
- [Outcomes](#outcomes)
- [Project Implementation (Code Snippets)](#project-implementation-code-snippets)
- [Getting Started](#getting-started)
- [Install Project Dependencies](#install-project-dependencies)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [Support and Feedback](#support-and-feedback)

## Problem Statement

In today's fast-paced world, providing employment opportunities to a larger number of individuals while addressing their need for proximity to family is a critical challenge. Many skilled workers are forced to travel far from their homes, leading to a disruption in their family lives. To address this issue, we aim to create a comprehensive platform that connects household service providers with job opportunities, all while ensuring that workers can find employment near their homes. This platform will incorporate advanced technology to recommend suitable jobs to workers, creating a win-win scenario for both employers and employees.

## Abstract

The project focuses on the development of a web-based platform that addresses the employment needs of skilled workers by providing job opportunities in close proximity to their residences. Leveraging modern web technologies, the platform aims to connect service providers and job seekers in a seamless manner. To enhance user experience and security, the platform will utilize JWT authentication. Real-time data management will be facilitated by integrating a MongoDB database. A key feature of this platform is the implementation of a recommendation system that employs machine learning techniques to suggest suitable job opportunities to workers based on their skills and preferences. By offering convenience, employment opportunities, and enhanced quality of life, the platform aims to revolutionize the way household services are accessed and delivered.

## Objectives

1. **Web Design:** Develop a user-friendly and visually appealing website using HTML, CSS, and JavaScript to ensure an intuitive user interface.

2. **Authentication:** Implement JSON Web Token (JWT) authentication to ensure secure access to the platform and protect user data.

3. **Databases:** Utilize MongoDB, a real-time database, to efficiently manage and store user data, job listings, and preferences.

4. **Recommendation:** Design and implement a recommendation system using machine learning algorithms to match skilled workers with suitable job opportunities.

## Outcomes

1. The platform will provide a convenient and efficient way for job seekers to access employment opportunities without compromising their family life.

2. By suggesting tailored job options to users based on their skills and preferences, the platform will enhance the overall job-seeking experience.

3. Workers and employers alike will benefit from reduced travel time and costs, leading to increased job satisfaction and productivity.

4. The recommendation system's implementation will lead to improved job matches, increasing the likelihood of long-term employment relationships.

5. The success of the platform will contribute to the growth of the local economy by fostering job creation and supporting small-scale service providers.

## Project Implementation (Code Snippets)

The following code snippets represent views from the Django project that implement the platform's functionality.

```python
# views.py

# Import necessary libraries and modules
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .utils import main
from .utils2 import main2

# Define views for different functionalities
def home(request):
    return render(request, "home.html")

def content_based(request):
    if request.method == "POST":
        address = request.POST.get("address")
        specialty = request.POST.get("specialty")
        # Call your model's main function with address and specialty as arguments
        results = main(address, specialty)
        return render(request, "content_based.html", {"results": results})
    return render(request, "content_based.html")
```

## Getting Started

1. Clone this repository to your local machine:

```bash
   git clone https://github.com/your-username/your-project.git
```

```bash
   cd your-project
```

2. Create a virtual environment named `venv` using the following command:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

## Install Project Dependencies

To install the required dependencies, execute the following command:

```bash
pip install -r requirements.txt
```

## Running the Project

Before running the project, ensure that you have properly configured the database settings in `settings.py`.

1. Apply Migrations: Create the necessary database tables by executing the following command:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

2. Create a Superuser (Optional): If you need access to the admin panel, create a superuser with administrative privileges:

```bash
python manage.py createsuperuser
```

3. Start the Development Server: Launch the development server to run the project locally:

```bash
python manage.py runserver
```

## Usage

Follow these steps to explore the project's functionalities:

Open Your Web Browser: Launch your preferred web browser and navigate to http://127.0.0.1:8000/.

1. Home Page: The home page welcomes users with a variety of services, including cooking, cleaning, plumbing, barber, and more. Each service is presented along with its brief description, offering users a glimpse of the available options.

2. Content-based Recommendation: To make the most of the content-based recommendation feature, users can navigate to specific service pages such as cooking or cleaning. After selecting a service, users can provide additional preferences, such as location and specialty. The system will then suggest tailored job opportunities that align with the user's preferences.

3. Collaborative Recommendation: Utilizing the collaborative filtering feature is easy. Users can access the collaborative recommendation section and provide their preferences or choices. Based on the preferences of other users with similar tastes, the system will recommend relevant services that the user might find appealing.

4. Signup and Login: To begin exploring the platform, users can create an account by clicking on the "Sign up" link. They will be prompted to provide their details and create a password. Once registered, users can log in using their credentials and access the platform's comprehensive range of services, recommendations, and user-specific functionalities.

## Support and Feedback

If you encounter any issues or have suggestions for improvement, please feel free to open an issue on our GitHub repository. Your feedback is valuable to us and will help make this project better.
