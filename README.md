# Healthy-Living
> Healthy-Living is a ecommerce and online course website where the ecommerce portion is extended from EcoFashion, a website regarding sustainable ecommerce that was made in the past.

[website link](http://voidcodes.pythonanywhere.com/) - limited functionality: databases doesn't work

Table of contents
 - [Meet Our Team](#Meet-Our-Team)
 - [Technologies Used](#Technologies-Used)
 - [Objects folder](#Objects)
 - [Static folder](#Static)
 - [Templates folder](#Templates)

## Meet Our Team

Responsibilities | *Wei Heng* | *Harold* | *Leroy* | *Delsius*
--- | --- | --- | --- | ---
Provision of previous EcoFashion website with adjustments | ✔️ | | |
Integration of Subscription service + subscription management with Courses | ✔️ | | |
Additional Integration with Courses such as reviews, wishlist | ✔️ | | |
Account Management of Teachers | | ✔️ | |
Integration of Teachers and Students(Customer) with Courses | | ✔️ | |
Course Viewing for Students(Customer) | | | ✔️|
Course Creation GUI for Teachers | | | | ✔️

## Technologies Used
We use Flask for our backend, Bootstrap for styling, Jinja2 to link our Flask and HTML. We also use Shelve as our database.
 - For the Subscription service, we use Stripe.
 - For Automatic Emails in Account Creations, we use Sendgrid
 - 

## Objects
The object folder holds the python classes and shelves, which is neatly organized into folders of respective categories.

## Static
The static folder holds the css, img and javascript assets. It is not used as much, and should be deleted once the CSS is fixed.

## Templates
The template folder holds all the HTML and Jinja2. Our Flask application will retrieve these HTML pages and route them properly.

## To do list
Tasks of Wei Heng | Tasks of Harold 
--- | --- 
Fix CSS of Account | Teacher registration form (optionally have a verification process)
Integrate Admin and Customer properly | Teacher Profiles, which Teachers can add details about themselves, and automatically show all courses under them
Develop products related to courses | ""
Develop UI to subscribe and manage their subscription | Role-based Access control to differentiate teacher and student accounts
Documentation through README.md | Teacher Object creation, update, view and deletion
Help with Courses to lighten their workload | Help with Courses to lighten their workload 

Tasks of Leroy | Tasks of Delsius 
--- | --- 
Create Course Information page, similar to Product Information page | Design overall layout of GUI for course creation, including course sections, as well as saving all the course materials to a shelve file, which can be access by Leroy to display course materials
Create Input Form for teachers to enter their course details, including title, description, content and pricing | (optional) Implement file upload to add course materials
Display course sections and its contents as a sidebar | Allow Teachers to add Youtube links to their course. Need to explore visibility options, to ensure students who didn't purchase the subscription cannot access the video through youtube
Retrieve the course materials from shelve to display Youtube links as a integration Youtube video within the course | Allow Teachers to add a articles, which is a page of text and images for Students to read
Retrieve course materials to display articles and MCQ Quizzes | Allow Teachers to create a MCQ Quiz
