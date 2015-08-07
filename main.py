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
    title = ndb.TextProperty(required = True)
    essay = ndb.TextProperty(required = True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_environment.get_template('templates/welcome.html')
        self.response.out.write(welcome_template.render())

class EssayHandler(webapp2.RequestHandler):
    def get(self):
            first_template = jinja_environment.get_template('templates/form.html')
            self.response.out.write(first_template.render())

            user = users.get_current_user()

            if user:
                self.response.write("Welcome, ")
                self.response.write(str(user) + '<br><br><br>')
                user = UserModel(currentUser = user.user_id())
                user.put()
            else:
                self.redirect(users.create_login_url(self.request.uri))

    def post(self):
        user_essay_text = self.request.get("essay_text")
        user_essay_title = self.request.get("essay_title")
        essay = EssayModel(essay = user_essay_text, title = user_essay_title)
        essay.put()
        redirect_template = jinja_environment.get_template('templates/form.html')
        self.response.out.write(redirect_template.render())
        time = self.request.get("user_time")

class ArchiveHandler(webapp2.RequestHandler):
    all = EssayModel(essay = 'this is an essay')
    #print all
    def get(self):
        #q = Person.all()
#q.filter("last_name =", "Smith")
        all_essays = EssayModel.query().fetch()
        #  all_essays.filter('essay')
        archive_template = jinja_environment.get_template('templates/archive.html')
        self.response.out.write(archive_template.render({'essays': all_essays}))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        message_template = jinja_environment.get_template('templates/about.html')
        self.response.out.write(message_template.render())

class ViewHandler(webapp2.RequestHandler):
    def post(self):
        essay_id = self.request.get("essay_id")
        essay_key = ndb.Key(EssayModel, int(essay_id))
        users_essay = essay_key.get()
        view_template = jinja_environment.get_template('templates/essay_view.html')
        self.response.out.write(view_template.render({"essay" : users_essay}))

class RemoveHandler(webapp2.RequestHandler):
    def post(self):
        essay_id = self.request.get("essay_id")
        essay_key = ndb.Key(EssayModel, int(essay_id))
        essay = essay_key.get()
        essay_title = essay.title

        users_essay = essay_key.delete()
        view_template = jinja_environment.get_template('templates/remove.html')

        self.response.out.write(view_template.render({"essay_title": essay_title}))
        # self.response.out.write(essay_key)
        # self.response.out.write(users_essay)
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/write', EssayHandler),
    ('/myessays', ArchiveHandler),
    ('/about', AboutHandler),
    ('/essay_view', ViewHandler),
    ('/remove', RemoveHandler)
], debug=True)
