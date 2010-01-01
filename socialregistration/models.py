"""
Created on 22.09.2009

@author: alen

Modified on 01.01.2010

@author: nasim
"""

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from google.appengine.ext import db

class FacebookProfile(db.Model):
    user = db.ReferenceProperty(User)
    uid = db.StringProperty()

    def __unicode__(self):
        return '%s: %s' % (self.user, self.uid)

    def authenticate(self):
        return authenticate(uid=self.uid)

class TwitterProfile(db.Model):
    user = db.ReferenceProperty(User)
    twitter_id = db.IntegerProperty()

    def __unicode__(self):
        return '%s: %s' % (self.user, self.twitter_id)

    def authenticate(self):
        return authenticate(twitter_id=self.twitter_id)

class FriendFeedProfile(db.Model):
    user = db.ReferenceProperty(User)

class OpenIDProfile(db.Model):
    user = db.ReferenceProperty(User)
    identity = db.TextProperty()

    def authenticate(self):
        return authenticate(identity=self.identity)

class OpenIDStore(db.Model):
    server_url = db.StringProperty()
    handle = db.StringProperty()
    secret = db.TextProperty()
    issued = db.IntegerProperty()
    lifetime = db.IntegerProperty()
    assoc_type = db.TextProperty()

class OpenIDNonce(db.Model):
    server_url = db.StringProperty()
    timestamp = db.IntegerProperty()
    salt = db.StringProperty()
    date_created = db.DateTimeProperty()

