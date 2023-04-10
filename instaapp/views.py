from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404


from .models import *
from .forms import *


'''
The @login_required declarator limits access of view function to only 
authenticated users
'''

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            request.user = user
            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            print(form.errors)
    return redirect('home')


# @login_required
def home(request):
    all_users = Profile.objects.all()
    all_posts = InstaPost.objects.order_by('-createdat').prefetch_related('likes', 'comments')
    following_users = [f.following for f in Follower.objects.filter(follower=request.user.id)]
    exclude_users = following_users + [request.user]
    users_to_follow = User.objects.exclude(id__in=[u.id for u in exclude_users])
    user_likes = set()
    context = {
        "all_users": all_users,
        'all_posts': all_posts,
        'user_likes': user_likes,
        'follower_suggestions': users_to_follow
    }
    return render(request, 'instaapp/home.html',  context)


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = request.user
            if user is not None:
                return redirect('home')
            else:
                print('user is none')
        else:
            form = UserCreationForm()
            context['form'] = form
            return render(request, 'users/signup.html', context)
        # context['form'] = form
    if request.method == 'GET':
        form = UserCreationForm()
        context['form'] = form
        return render(request, 'users/signup.html', context)


# VIEW FUNCTIONS HERE!

#Explore page view function
@login_required(login_url='login')
def explore(request):
    return render(request, 'instaapp/explore.html')

#Notification page view function
@login_required(login_url='login')
def notification(request):
    return render(request, 'instaapp/notification.html')

#Profile page view function
@login_required(login_url='login')
def profile(request, user_id):
    user = User.objects.get(username=user_id)
    profile = Profile.objects.get(user=user)
    followers = Follower.objects.filter(following=user).count()
    following = Follower.objects.filter(follower=user).count()
    postscount = InstaPost.objects.filter(user=user).count()
    context = {
        'profile': profile,
        'postscount': postscount,
        'followers': followers,
        'following': following
    }
    return render(request, 'instaapp/userprofile.html', context)

@login_required(login_url='login')
def follow(request, user_id):
    user_to_follow = get_object_or_404(User, username=user_id)
    Follower.objects.create(follower=request.user, following=user_to_follow)
    return redirect('profile', request.user.username)

@login_required(login_url='login')
def unfollow(request, user_id):
    user_to_unfollow = get_object_or_404(User, username=user_id)
    Follower.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    return redirect('profile', request.user.username)


@login_required(login_url='login')
def followings(request, user_id):
    followings = Follower.objects.filter(follower=user_id)
    following_list = [{'username': f.following.username, 'profile_url': f.following.profile.profile_pic.url, 'profile_image_url': f.following.profile.profile_pic.url} for f in followings]
    return JsonResponse(following_list, safe=False)

@login_required(login_url='login')
def followers(request, user_id):
    followers = Follower.objects.filter(following=user_id)
    followers_list = [{'username': f.follower.username, 'profile_url': f.follower.profile.profile_pic.url, 'profile_image_url': f.follower.profile.profile_pic.url} for f in followers]
    return JsonResponse(followers_list, safe=False)


@login_required(login_url='login')
def update_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        profile.first_name = request.POST.get('first_name')
        profile.last_name = request.POST.get('last_name')
        profile.bio = request.POST.get('bio')
        if request.FILES.get('profile_pic'):
            profile.profile_pic = request.FILES.get('profile_pic')
        if request.FILES.get('profile_avatar'):
            profile.profile_avatar = request.FILES.get('profile_avatar')
        if request.POST.get('date_of_birth'):
            profile.date_of_birth = request.POST.get('date_of_birth')
        profile.gender = request.POST.get('gender')
        profile.save()
        context = {'profile': profile}
        return render(request, 'instaapp/userprofile.html', context)
    context = {'profile': profile}
    return render(request, 'instaapp/updateprofile.html', context)


@login_required(login_url='login')
def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('home')
        else:
            print(form.errors)
            return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'instaapp/createpost.html', {"form": form})


@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(InstaPost, id=post_id)
    if post:
        like, created = Like.objects.get_or_create(user=request.user, instapost=post)
        if not created:
            like.delete()
    return redirect('home')


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(InstaPost, id=post_id)
    comment = PostComments(author=request.user, post=post, comment=request.POST.get('comment'))
    comment.save()
    return redirect('home')


#Log-Out page view function
def logout(request):
    return render(request, 'users/logout.html')