# Salt of the Earth

![Welcome](https://res.cloudinary.com/dmux1cvft/image/upload/v1709805290/home_usuw0c.png)

### Savor the flavors of the Mediterranean at Salt of the Earth. From our django based website you can create a booking and indulge yourself into experience from grilled delicacies to fresh salads, the taste of the sun-kissed coast on your plate.

[Open](https://django-app-08f2d4b673c2.herokuapp.com/)

## Table of Contents

1. [Agile](#agile)

2. [Design](#design)

- [User Interface](#user-interface)
- [User Experience](#user-experience)

3. [Features](#features)

- [Existing Features](#existing-features)
- [Features Left to Implement](#features-left-to-implement)

4. [Technologies](#technologies)

5. [Testing](#testing)

- [Manual Testing](#manual-testing)

6. [Deployment](#deployment)

- [Heroku](#heroku)

7. [Credits](#credits)

## Agile

## Agile methodology, used Project Boards on Github, with epics and user stories, tasks templates to organise project

<details>
  <summary>User Journey</summary>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1709808810/userjourney_qehdm6.png"></a>
</details>
<br>

<details>
  <summary>Entity Relationship Diagram</summary>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1709809159/ERD_ikwjoz.png"></a>
</details>
<br>

<details>
  <summary>Epics</summary>
  <br>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725268995/Epics_ki1p3c.png"></a>
</details>
<br>

<details>
  <summary>Issues</summary>
  <br>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725268996/Issues_lrr7zh.png"></a>
</details>
<br>

<details>
  <summary>Milestones</summary>
  <br>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725268995/Milestones_h2vwmc.png"></a>
</details>
<br>

<details>
  <summary>Sprints</summary>
  <br>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725268997/Sprints_rxoh23.png"></a>
</details>
<br>

<details>
  <summary>Scrum Board</summary>
  <br>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725268996/ScrumBoard_g4uodg.png"></a>
</details>
<br>

<details>
  <summary>Task Board</summary>
  <br>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725268996/TaskBoard_fpvcru.png"></a>
</details>
<br>

## Design

### User Interface

<details>
  <summary>Logo, designed by me</summary>
  <br>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1702151125/Group_2_g4hezf.png"></a>
</details>
<br>

<details>
  <summary>Color Palette: #212529 #619b8a #727272 #ffffff</summary>
  <br>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725268213/Vector_a5isl2.png"></a>
</details>
<br>




### User Experience

#### First time user: intuitive navigation, user-friendly forms, clear validation errors, easy registration.

#### Registered User: easy authenticated login, quick booking, acess to review, update and delete reservations.

### Admin

#### Admin: Ability to add or delete tables with different capacities, and create and delete bookings.

### Wireframes
 ```
 If user is not authenticated
```
<details>
  <summary>Home Page</summary>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725265468/home01_uska5n.png"></a>
</details>
<details>
  <summary>Menu Page</summary>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725265468/menu01_qaeg81.png"></a>
</details>
<details>
  <summary>Login Page</summary>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725265468/login01_denxhy.png"></a>
</details>
<br>

```
 If user is authenticated
```
<details>
  <summary>Home Page</summary>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725265469/home02_c1d3r0.png"></a>
</details>
<details>
  <summary>Menu Page</summary>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725265469/menu02_ifsres.png"></a>
</details>
<details>
  <summary>Book Page</summary>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725265469/book02_crjy6p.png"></a>
</details>
<details>
  <summary>Bookings Page</summary>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725265468/bookings02_v9zxws.png"></a>
</details>
<details>
  <summary>Logout Page</summary>
<a><img src="https://res.cloudinary.com/dmux1cvft/image/upload/v1725265468/logout02_cqiyrn.png"></a>
</details>
<br>



## Features

### Existing Features

- Login, singup, signout
- create, read, update, delete booking

### Features Left to Implement

- create, read, update, delete reviews

## Technologies

- Codeanywhere
- VScode

### Languages

- HTML5
- CSS
- Python

### DB

- [ElephantSQL](https://www.elephantsql.com/)

### Frameworks

- [Bootstrap 5.3.2](https://blog.getbootstrap.com/2023/09/14/bootstrap-5-3-2/)
- [Django](https://www.djangoproject.com/)
- [Git](https://git-scm.com/)
- [Github](https://github.com/)
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/)

## Testing

### Manual Testing

```
 If user is not authenticated
```

| PAGE  | TEST                  | EXPECTED                                     | OUTCOME |
| ----- | --------------------- | -------------------------------------------- | ------- |
| HOME  | Click on Logo         | Redirect to Home Page                        | PASS    |
| HOME  | Click on Btn BOOK NOW | Redirect to Login Page                       | PASS    |
| HOME  | Click on Home         | Stays on Home Page                           | PASS    |
| HOME  | Click on Menu         | Redirect to Menu Page                        | PASS    |
| HOME  | Click on LOGIN        | Result02                                     | PASS    |
| HOME  | Test02                | Redirect to Login Page                       | PASS    |
| LOGIN | Fill form and signin  | Redirects to website for authenticated users | PASS    |
| LOGIN | Click on signup       | Redirects to website for authenticated users | PASS    |

```
 If user is authenticated
```

| PAGE   | TEST                     | EXPECTED                                         | OUTCOME |
| ------ | ------------------------ | ------------------------------------------------ | ------- |
| HOME   | Click on Logo            | Redirect to Home Page                            | PASS    |
| HOME   | Click on Home            | Stays on Home Page                               | PASS    |
| HOME   | Click on Menu            | Redirect to Menu Page                            | PASS    |
| HOME   | Click on Book            | Redirect to Book Page                            | PASS    |
| HOME   | Click on Bookings        | Redirect to Bookings Page                        | PASS    |
| HOME   | Click on LOGOUT          | Redirects ton confirmation form                  | PASS    |
| BOOK   | Click on LOGOUT          | Redirects ton confirmation form                  | PASS    |
| LOGOUT | Click on sign out button | Redirects to website for non authenticated users | PASS    |

```
 FORM Validation
```

| PAGE        | TEST                   | EXPECTED                                | OUTCOME |
| ----------- | ---------------------- | --------------------------------------- | ------- |
| BOOK        | if no available tables | error                                   | PASS    |
| BOOK        | if available tables    | redirect to booking                     | PASS    |
| BOOKINGS    | Update                 | redirects to update form                | PASS    |
| BOOKINGS    | Delete                 | deletes and redirects to bookings again | PASS    |
| UPDATE FORM | if no available tables | error                                   | PASS    |
| UPDATE FORM | if available tables    | redirect to booking                     | PASS    |

### BUGS

- updating form doesn't exlude current ocupied table, before updating and gives erro when attemp to change details for the same table.

## Deployment

### Fork

- Find github [repo](https://github.com/vikdts/django-app).
- Under the main navigation, click the Fork button, located second to last on the right.
- You have personal copy of the original repository in your GitHub account now.

### Clone

- Find github [repo](https://github.com/vikdts/django-app).
- Click the Code button, copy the local clone with HTTPS, SSH or GitHub CLI.
- Open the terminal and change the directory to the desired destination for your clone repo.
- Type git clone and paste the copied URL, then press enter, to create the local clone.

### Heroku

- Set DEBUG = False in the settings.py.
- Go to Heroku deploy tab.
- Connect to GitHub and correct repo.
- Click on Deploy Branch to deploy manually on bottom of the page.
- Click 'Open App' to view the deployed live site.

## Credits

- [Code Institue](https://codeinstitute.net/global/)
- [Django](https://www.djangoproject.com/)
- [Allauth](https://docs.allauth.org/en/latest/)
- [Gunicorn](https://gunicorn.org/)
- [Psycopg](https://pypi.org/project/psycopg2/)
- [Bootstrap 5.3.2](https://blog.getbootstrap.com/2023/09/14/bootstrap-5-3-2/)
- [Cloudinary](https://cloudinary.com/documentation)
- [Stack Overflow](https://stackoverflow.com/)
- [MDN](https://developer.mozilla.org/en-US/)
- [Pexels](https://www.pexels.com/)
- [Figma](https://www.figma.com/)
- [Github](https://github.com/)
- [Heroku](https://www.heroku.com/)
- [Codeanywhere](https://codeanywhere.com/signin)
- [VScode](https://code.visualstudio.com/)
