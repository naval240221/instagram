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
- Your applocation should be up and running and you can visit it using link [http://127.0.0.1/8000](http://127.0.0.1/8000)

# Sample Webpage Layout and design

## Home Page + Login Form

![homepageoriginal](https://user-images.githubusercontent.com/128895452/231014616-5b4147d0-c23c-43d3-854d-de604a85c664.jpg)

## Sign Up Form

![signup](https://user-images.githubusercontent.com/128895452/231014684-aa1df05a-d687-488b-a4e1-6a93d490644c.jpg)

## Insta Feed Home Page After Login

![instafeed](https://user-images.githubusercontent.com/128895452/231014733-352afffb-4a40-489f-abe6-e0fcde6911f4.jpg)


## Create Your First Post By clicking on Create button on top navbar

![create_post](https://user-images.githubusercontent.com/128895452/231015085-70c85cfc-efba-4e12-9dc2-203e6a6d6ed0.jpg)



## Visit Your profile by clicking profile icon

## Edit Profile (Click On Edit Profile Button)

![updateprofile](https://user-images.githubusercontent.com/128895452/231014925-167de953-bedc-4288-8367-baeaf1084cd4.jpg)


## See Followers and Followings

## View Comments

![showcomments](https://user-images.githubusercontent.com/128895452/231015020-17fefd9d-6c8d-4735-b214-1e56ea1bc6a4.jpg)








