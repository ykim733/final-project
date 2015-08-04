from google.appengine.ext import ndb
import webapp2
import jinja2
import os
import time
import threading
from google.appengine.api import users
import sys


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))



class UserModel(ndb.Model):
    currentUser = ndb.StringProperty(required = True)


class EssayModel(ndb.Model):
    essay = ndb.TextProperty(required = True)

class MainHandler(webapp2.RequestHandler):

    def get(self):

            first_template = jinja_environment.get_template('templates/form.html') 
            self.response.out.write(first_template.render())

            user = users.get_current_user()

            if user:


                self.response.write(user)
                user = UserModel(currentUser = user.user_id())
                user.put()

            else:


                self.redirect(users.create_login_url(self.request.uri))



    def post(self):
        user_essay_text = self.request.get("essay_text")
        self.response.write("my essay text is : " + user_essay_text)

        essay = EssayModel(essay = user_essay_text)
        essay.put()




class ArchiveHandler(webapp2.RequestHandler):


    def get(self):
         archive_template = jinja_environment.get_template('templates/archive.html')
         self.response.out.write(archive_template.render())
         userlogin = True

class MessageHandler(ndb.Model):
    def get(self):
        message_template = jinja_environment.get_template('templates/messages.html')
        self.response.out.write(message_template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/myessays', ArchiveHandler),
    ('/messages', MessageHandler)
], debug=True)
