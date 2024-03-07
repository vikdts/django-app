# Salt of the Earth

![Welcome](https://res.cloudinary.com/dmux1cvft/image/upload/v1709805290/home_usuw0c.png)

### Savor the flavors of the Mediterranean at Salt of the Earth. From our django based website you can create a booking and indulge yourself into experience from grilled delicacies to fresh salads, the taste of the sun-kissed coast on your plate.

[Open](https://django-app-08f2d4b673c2.herokuapp.com/)

## Table of Contents

1. [Design](#design)

- [User Interface](#user-interface)
- [User Experience](#user-experience)

2. [Features](#features)

- [Existing Features](#existing-features)
- [Features Left to Implement](#features-left-to-implement)

3. [Technologies](#technologies)

4. [Testing](#testing)

- [Manual Testing](#manual-testing)

5. [Deployment](#deployment)

- [Heroku](#heroku)

6. [Credits](#credits)

## Design

### User Interface

- Logo created by me.
- Color Palette #212529 #619b8a #727272 #ffffff

### User Experience

- First time user, intuitive navigation, user-friendly forms,
  clear validation errors, easy registration.

- Registered User, easy authenticated login, quick booking, acess to review, update and delete reservations.

### Admin

- Ability to add or delete tables with different capacities, and create and delete bookings.

### Agile

- Agile methodology using Project Boards on Github, with epics and user stories templates to organise project

- User Journey
  ![Journe](https://res.cloudinary.com/dmux1cvft/image/upload/v1709808810/userjourney_qehdm6.png)

- Entity Relationship Diagram
  ![Diagram](https://res.cloudinary.com/dmux1cvft/image/upload/v1709809159/ERD_ikwjoz.png)

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

- [ElephantSQL](https://www.elephantsql.com/) - PostgreSQL Database

### Frameworks

- [Bootstrap 5.3.2](https://blog.getbootstrap.com/2023/09/14/bootstrap-5-3-2/)
- [Django](https://www.djangoproject.com/)
- [Git](https://git-scm.com/) - Version control
- [Github](https://github.com/) - code host
- Jinja - Template engine

## Testing

### Manual Testing

```
 If user is not auathenticated
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
 If user is auathenticated
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
- [Bootstrap 5.3.2](https://blog.getbootstrap.com/2023/09/14/bootstrap-5-3-2/)
- [Cloudinary](https://cloudinary.com/documentation)
- [Stack Overflow](https://stackoverflow.com/)
- [MDN](https://developer.mozilla.org/en-US/)
- [Pexels](https://www.pexels.com/)
