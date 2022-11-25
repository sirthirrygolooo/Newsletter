# Newsletter 

## Introduction

- This is a newsletter v1 written and tested in [**python 3.8**](https://www.python.org/downloads/release/python-382/) for [BSK Esport](https://teambsk.fr)

- Made for Windows but can easily be adapted for Linux or other OS with a few changes.

- It is composed of different parts :
```
~ NEWSLETTER ~ 
├── main.py --> 
├── check_adress.py -->
├── account.json --> 
├── subscribed.json --> 
└── ./message_content
    ├── html.py --> 
    ├── message.py --> 
    └── text.py --> 
```

## Send Email 

First, you need to install the required modules with the command `pip install -r requirements.txt` in the folder where you downloaded the newsletter.

Then, you need to fill the [`account.json`](./account.json) file with your email address and password.
```
{
    "email": "your_email_address",
    "password": "your_password"
}
```
Then, it is recommended to use your own smtp server but if you don't have one, you can use the one provided by gmail. To do so, you need to go to the [**Less secure app access**](https://myaccount.google.com/lesssecureapps) page and allow access to less secure apps.

After launching the [`main.py`](./main.py) file, just follow instructions, entering a smtp server and a running port and then, your message.   
It will be sent to all the persons in the [`subscribed.json`](./subscribed.json) file.

The mail content will be asked during the execution of the program. It can be a simple text or a html template. If you want to use a html template, you need to put it in the [`html_content.py`](./message_content/html.py) file and then enter the content in html of your mail. You don't need to do it before because the program will ask you if you want to use a html template or not and then open a text editor to write your message.

## The [`check_adress.py`](./check_adress.py) file

This file is mainly used to add a new email adress to the [`subscribed.json`](./subscribed.json) file. It can also be used to check if an email adress is already in the file or is valid (validity criteria are if the structure of email adress is correct : yourmail@extension.something where the @extension.something exist).

