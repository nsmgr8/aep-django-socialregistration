"""
Created on 22.09.2009

@author: alen
"""
from django.contrib.auth.models import User
from django.contrib.sites.models import Site

from socialregistration.models import (FacebookProfile, TwitterProfile, FriendFeedProfile, OpenIDProfile)

class Auth(object):
    def get_user(self, user_id):
        return User.get(user_id)

class FacebookAuth(Auth):
    def authenticate(self, uid=None):
        return FacebookProfile.all().filter('uid =', uid).get()

class TwitterAuth(Auth):
    def authenticate(self, twitter_id=None):
        return TwitterProfile.all().filter('twitter_id =', twitter_id).get()

class OpenIDAuth(Auth):
    def authenticate(self, identity=None):
        return OpenIDProfile.all().filter('identity =', identity).get()
