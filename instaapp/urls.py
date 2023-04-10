from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('explore', explore, name ='explore'),
    path('notification', notification, name ='notification'),
    path('profile/update/', update_profile, name='update_profile'),
    path('profile/<str:user_id>/', profile, name='profile'),
    path('followings/<str:user_id>', followings, name='followings'),
    path('followers/<str:user_id>', followers, name='followers'),
    path('logout', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup', signup, name='signup'),
    path('create_post', create_post, name='create_post'),
    path('follow/<str:user_id>/', follow, name='follow'),
    path('unfollow/<str:user_id>/', unfollow, name='unfollow'),
    path('post/<int:post_id>/like/', toggle_like, name='toggle_like'),
    path('post/<int:post_id>/comment/', add_comment, name='add_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)