
from google.appengine.ext import ndb
import webapp2
import jinja2
import os
import time
import threading
from google.appengine.api import users


jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))



class UserModel(ndb.Model):
    currentUser = ndb.StringProperty(required = True)
    essay = ndb.TextProperty(required = False)




class MainHandler(webapp2.RequestHandler):

    def get(self):

            first_template = jinja_environment.get_template('templates/form.html') #this isn't working #I added a templates directory so it should be good now
            self.response.out.write(first_template.render())
            for t in range(120,-1,-1):
                minutes = t / 60
                seconds = t % 60

                screenTime =  "%d:%2d" % (minutes,seconds)
                print screenTime #prints countdown to screen

                #time.sleep(1.0) # the sleep makes the website impossible to reload
                #my_time_dictionary = {"screenTime" : screenTime }
                #self.response.out.write(first_template.render(my_time_dictionary))



    def post(self):


        user = Productivity(username=self.request.get("user")) #gets user input from url in Productivity class
        template_vars = { "my_user" : user}
        user.put() #puts user into datastore
        #qry = Productivity.query(Productivity.username == "nicki").fetch()
        self.response.out.write(user.username)            #now instead of self writing it, make a template variable
        essayText = Productivity(essay=self.request.get("essay_text"))
        essay_vars = {"my_essay" : essayText}
        essayText.put()
        self.response.out.write(essayText.essay)
        #self.response.out.write(user) use this to view key after hitting submit

        userlogin = True
        if userlogin:
            self.response.out.write("<h1>Welcome!</h1>")
        else:
            self.response.out.write("Please login")
        template = jinja_environment.get_template('form.html')
        self.response.write(template.render())


        user = users.get_current_user()
        if user:
            self.response.write(user)
            user = UserModel(currentUser = user.user_id(), essay = self.request.get("essay"))
            user.put()
        else:
            self.redirect(users.create_login_url(self.request.uri))

        first_template = jinja_environment.get_template('templates/form.html') #this isn't working #I added a templates directory so it should be good now
        self.response.out.write(first_template.render())

        for t in range(120,-1,-1):
            minutes = t / 60
            seconds = t % 60

            screenTime =  "%d:%2d" % (minutes,seconds)
            print screenTime #prints countdown to screen


        def get(self):
            self.request.get(first_template.render('essay'))

                #qtime.sleep(1.0) # the sleep makes the website impossible to reload
                #my_time_dictionary = {"screenTime" : screenTime }
                #self.response.out.write(first_template.render(my_time_dictionary))

    # def post(self):

            #pass text to datastore from form
            # essayText = UserModel(essay=self.request.get("essay_text"))
            # essay_vars = {"my_essay" : essayText}
            # essayText.put()
            # self.response.out.write(essayText.essay)
            # #self.response.out.write(user) use this to view key after hitting submit


class ArchiveHandler(ndb.Model):
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
