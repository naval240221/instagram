from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    
    class GenderChoices(models.TextChoices):
        M = 'Male', _('Male')
        F = 'Female', _('Female')
        O = 'Other', _('Other')
        P = 'Prefer Not To Say', _('Prefer Not To Say')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to="profilepictures/", blank=False)
    profile_avatar = models.ImageField(upload_to="avatarpictures/", blank=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=350)
    date_of_birth = models.DateField(null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=True)
    gender = models.CharField(
        choices=GenderChoices.choices,
        default=GenderChoices.P,
    )

    """Method to filter database results"""

    def __str__(self):
        return self.user.username


### Class Posts


class InstaPost(models.Model):
    # Attributes of Posts Class
    """
    userid: Foreign key of the user table
    image_urls: Array [urls of images that is uploaded in the post]
    date: auto added date, represent when the post was added
    caption: textarea, Any Caption is added to the the post
    hashtags: Array, any tags added to the post
    tags: Array, user profiles, whom we have tagged
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to="posts/")
    caption = models.TextField()
    location = models.CharField(max_length=50)
    hashtags = models.CharField(max_length=50)
    createdat = models.DateTimeField(auto_now_add=True, null=False)
    updatedat = models.DateTimeField(auto_now_add=True, null=False)
    likes = models.ManyToManyField(User, related_name='liked_post', through='Like')

    """Method to filter database results"""

    def __str__(self):
        return self.caption


# ... Class Like Starts Here ....
class Like(models.Model):
    """
    - user: Foreign Key of the user table
    - instapost: Foreign Key of posts which has been liked
    - liked_at: Date time at which the post has been liked
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instapost = models.ForeignKey(InstaPost, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

## Class For storing comments to a post
class PostComments(models.Model):
    post = models.ForeignKey(InstaPost, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    commenter_profile = models.ForeignKey(
        "Profile", related_name="commenter", on_delete=models.CASCADE, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.commenter_profile

# Follwer relation table
class Follower(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')