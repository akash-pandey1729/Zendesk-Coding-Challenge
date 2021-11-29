# Zendesk-Coding-Challenge
Django Based Ticket Viewer

The assignment has been made using Django. Important methods have been scripted in [views.py](https://github.com/milind-prajapat/Zendesk-Coding-Challenge/blob/main/ticket/views.py). Exception handling has been put in place, and Unit testing codes have been written in [test.py](https://github.com/milind-prajapat/Zendesk-Coding-Challenge/blob/main/ticket/views.py).

It has also been hosted on <> for quick reference.

## Installation
#### Method 1: Website
<>

#### Method 2: Manually 
1. Clone this repository
2. Activate the virtual environment ```source env/Scripts/activate``` 
3. Install the packages using [requirement.txt](https://github.com/milind-prajapat/Zendesk-Coding-Challenge/blob/main/requirements.txt) ```python3 -m pip install -r requirements.txt```
4. Finally, start the server using ```python3 manage.py runserver```

#### Method 3:
Alternatively, if you have Visual Studio, open the [Zendesk-Coding-Challenge.sln](https://github.com/milind-prajapat/Zendesk-Coding-Challenge/blob/main/Zendesk-Coding-Challenge.sln) and run the server directly from Visual Studio.

## Instructions to Use:
1. Once at the Home page in your browser, you will be asked to enter: 
   1. E-mail Id
   2. Sub-domain
   3. API Token
2. On the top bar, there are three buttons:
   1. Home
   2. About
   3. Login/Logout

On the homepage, you can see available tickets for your account. There will be a list of 25 tickets on each page. At the bottom, there are options for navigating to other pages. </br>
The individual ticket heading is clickable. It is a hyperlink to the individual ticket details. You can redirect back to the home page using the home button or to the previous page using the browsers back button.
