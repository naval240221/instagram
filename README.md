# instagram
Instagram clone web app with functionalities
- SignUp/Login
- Create Post
- Like Post, Comment on Post
- User Profile View
- Edit User Profile
- Follow/Unfollow different user
- View all comments


# Prerequisites
- Any editor you user for coding
- Python>=3.10.9
- Postgres Db Setup

# Installation Or Setup Requirements
To setup this repo in your local machine you have to follow these steps
- Git clone this repo, this will create a repo in your current working directory named `**instagram**`
- run `cd instagram` and then Create a virtual environment named `python3 -m venv instaapp`
- activate the virtual environment by running command `source ./bin/activate`
- Install all dependencies by running command `pip3 install -r requirements.txt`
- After that run `python3 manage.py makemigrations`
- After that run `python3 manage.py migrate`
- These two above commands will create tables in your local database (before this create a db named `myinstaapp` using command in psql `CREATE DATABASE myinstaapp;` or you can choose name according to youe need and update it in settings.py)
- After all these steps run a final command `python3 manage.py runserver`
- Your applocation should be up and running and you can visit it using link [http://127.0.0.1/8000]|(http://127.0.0.1/8000)





