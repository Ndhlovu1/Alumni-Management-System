# Group Members
![WhatsApp Image 2023-10-28 at 11 14 49_7e22fd85](https://github.com/Ndhlovu1/Phoenix-2023-tertiary-hackathon/assets/83342122/03acf409-48fb-4ed6-b9cd-b7a2c5b8f6f5)

# Project Description
## Problem Statement
Alumni management system is a dedicated solution or software aimed at enabling organizations - 
usually colleges and universities, to be in constant touch with the Alumni. An Alumni (Alumnus) is a 
graduate or former student of a particular school, college, or university. AIMS provide a platform 
for Alumni members to connect among themselves and maintain a close relationship with their 
Alma Mater. Alma Mater is a school, college, or university which one has attended or from which 
one has graduated. Using a reliable Alumni information management software solution, the 
platform can allow Alumni members and other graduates to connect. 

## Problem Breakdown
### Brainstorming
As a team, the first thing to do when working on a project is brainstorm. Below are images that show the first stage of our project management, which is designing.

![IMG-4051](https://github.com/Ndhlovu1/Phoenix-2023-tertiary-hackathon/assets/83342122/dd9f089c-2e98-4b48-9903-05ff2de1a71e)

This drawing shows the front end of the system which basically exposes the user to content such as the gallery, career advice, upcoming events in the institution, news, elections, jobs available and also creation to of an account.

![IMG-4053](https://github.com/Ndhlovu1/Phoenix-2023-tertiary-hackathon/assets/83342122/cc7579e7-db6d-461e-bf63-22b458f932f5)

In addition, this is the event planning page that shows the upcoming events taking place at the institution.

# Solution Creation
Our solution is an AMS website, which provides a full platform for alumni to interact and communicate with their alma school. Alumni have access to a user-friendly site where they can log in and explore a variety of options on the front end. This includes updating personal information, staying up to date on forthcoming alumni events and news, interacting with other graduates via a directory, and gaining access to job prospects and professional resources. Our admin panel allows administrators to manage user accounts, manage content, events, and alumni directories. Our products are built with a heavy emphasis on security, scalability, and usability in mind.

# Databases
Sqlite
* We selected SQLite as our database for the Alumni Management System (AMS) website due to its lightweight, serverless, and efficient nature. SQLite's strong performance, data security features, and compatibility with various platforms made it a practical choice for our needs, ensuring a reliable and streamlined data storage solution.

# Design
## Flowchart
![WhatsApp Image 2023-10-28 at 11 05 57_4a2081ee](https://github.com/Ndhlovu1/Phoenix-2023-tertiary-hackathon/assets/83342122/b6d18d5a-ba9a-4000-ba8e-dd6511ef118a)

## Pseudocode

Alumni Management System

1.	Landing Page

Display the landing page with the following options:

* 	Home
* 	Gallery
* 	Login

2.	Cards
Display 6 cards on the landing page, each card leading to a different page:
* 	Card 1: Newsletter
* 	Card 2: Career Guidance
* 	Card 3: Upcoming Events
* 	Card 4: Elections
* 	Card 5: Vacancies
* 	Card 6: Community

SHOULD THE USER BE LOGGED IN SHOW ALL OPTIONS ELSE REDIRECT TO THE REGISTER PAGE

2.1.	Newsletter Page

Display the newsletter page with the following options:

* View newsletter
* Subscribe to newsletter

2.2.	Career Guidance Page

Display the career guidance page with the following options:
* View resources
* Book a consultation

2.3.	Upcoming Events Page

Display the upcoming events page with the following options:
* View all events
* View details of an event
* Register for an event

2.4.	Elections Page
Display the elections page with the following options:
* View candidates
* Vote for a candidate

2.5.	Vacancies Page

Display the vacancies page with the following options:
* View all vacancies
* Apply for a vacancy

2.6.	Community Page
Display the community page with the following options:
* Upload documents
* View documents
* Upload applications
* View applications

3.	Login Page
Display the login page with the following fields:
* Email address
* Password

4.	Dashboard
Display the dashboard with the following options:
* View profile information
* Update profile information
* View news and announcements
* View upcoming events
* View job postings
* Connect with other alumni

5.	User Actions
* User clicks on one of the 6 cards on the landing page to be taken to the corresponding page.
* Users logs in to their account to view their profile information, update their profile information, view news and announcements, view upcoming events, view job postings, and connect with other alumni.

6.	 Gallery Page
Gallery page has the  following options:
* View Previous Events
For each event:

    A card with the following information:

        * Event title

        * Event date

        * Event location

        * Event description

# Design (Screenshots of software)
![WhatsApp Image 2023-10-28 at 11 16 55_c6f86e4c](https://github.com/Ndhlovu1/Phoenix-2023-tertiary-hackathon/assets/83342122/c53abe92-1e90-4de8-897a-ceb3447325b4)

![WhatsApp Image 2023-10-28 at 11 16 56_fbd2566f](https://github.com/Ndhlovu1/Phoenix-2023-tertiary-hackathon/assets/83342122/156ce998-8b82-40be-9324-b8991facd95a)

![WhatsApp Image 2023-10-28 at 11 16 57_b1fbab30](https://github.com/Ndhlovu1/Phoenix-2023-tertiary-hackathon/assets/83342122/607bc041-7fdc-4cc1-8dab-31e77ec9bf2d)

![WhatsApp Image 2023-10-28 at 11 16 57_c9a1d7a8](https://github.com/Ndhlovu1/Phoenix-2023-tertiary-hackathon/assets/83342122/1ad8ba81-1cce-4d57-a8a0-f13de37095cf)

![WhatsApp Image 2023-10-28 at 11 16 58_f99751b1](https://github.com/Ndhlovu1/Phoenix-2023-tertiary-hackathon/assets/83342122/03cd5c09-637a-4e39-92a4-aded6465934f)

![WhatsApp Image 2023-10-28 at 11 16 59_f3e25a9a](https://github.com/Ndhlovu1/Phoenix-2023-tertiary-hackathon/assets/83342122/780d2348-8606-4147-9383-79e4805dea23)

![WhatsApp Image 2023-10-28 at 11 17 00_56e51aef](https://github.com/Ndhlovu1/Phoenix-2023-tertiary-hackathon/assets/83342122/3441dfc3-6e72-42a2-9490-dba0591dab74)

![WhatsApp Image 2023-10-28 at 11 17 00_14d43a70](https://github.com/Ndhlovu1/Phoenix-2023-tertiary-hackathon/assets/83342122/38dc6b76-3f4b-4d5f-91f2-6ffff28bfe4d)

# Technical Documentation
## Components of software:

Microservices Architecture: 

* For scalability and maintainability, the project is built using a microservices architecture, in which individual components are divided down into discrete, independent services.

Django Framework: 

* The system's backend is based on the Django web framework, which provides tools for developing online applications such as user authentication and data management.

Template Tags:
* Using template tags gave us the full functionality of the Django language library such as the use of try and conditional statements.
Template Variables
* To manipulate the database
HTML & CSS (with additional bootstrap)
* For functionality and maintained code

## Versions of the software:

Microservices Architecture: 
* Because it is a design approach, there is no specific version connected with it. It is vital to highlight, however, that each microservice should employ software components that are compliant with the project's needs.

Django Framework: 
* Django version 3.2 is used to build the project. This version offers stability as well as access to the most recent features and security upgrades. In addition, it is also a web based language with powerful Rest API's and frameworks.

## Requirements for the Operating System:

Microservices Architecture: 
* Microservices are often platform-independent and may be implemented on a variety of operating systems such as Windows, Linux, and macOS.
Django Framework: 
* Django is compatible with a variety of operating systems, including Windows, macOS, and Linux.

# Non-Technical Documentation

Easily Learn to Code

* We think that coding is accessible to all people, not just IT experts. Our platform provides a straightforward and approachable introduction to the world of coding. You don't need any prior experience; we'll walk you through every step of the process.

User Administration

* Our technology makes it simple to manage users. This means you can easily create, organize, and manage user accounts. Users can be assigned different roles and permissions based on their duties inside the platform.

Make and Share Posts

* Don't worry if you're a journalist or a marketing student and coding isn't your strong suit! You may use our platform to generate and publish blogs without any technical skills. You may design your content using our user-friendly tools and templates, making it easier than ever to share your thoughts with the world.
 
Simple to comprehend

* Our material has been created with you in mind. It is written in basic terms, so there is no technical jargon. We've provided pictures, images, and examples to help you understand everything.



