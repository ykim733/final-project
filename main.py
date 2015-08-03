
from google.appengine.ext import ndb
import webapp2
import jinja2
import os
import time

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Productivity(ndb.Model):
    essay = ndb.StringProperty(required = False)
    username = ndb.StringProperty(required = False)
    password = ndb.StringProperty(required = False)





# Hai girl hai, so I got the user input working in the url input, but I haven't been able to link it in a form good luck!
# btw I just added a username input in the form with the essay entitle from.html

class MainHandler(webapp2.RequestHandler):
    def get(self):
            first_template = jinja_environment.get_template('templates/form.html') #this isn't working #I added a templates directory so it should be good now
            self.response.out.write(first_template.render())
            for t in range(120,-1,-1):
                minutes = t / 60
                seconds = t % 60
            #   print  "%d:%2d" % (minutes,seconds)
                # time.sleep(1.0) This will print a live countdown to the console, but even without printing, the sleep makes the website impossible to reload 

    def post(self):


            user = Productivity(username=self.request.get("user")) #gets user input from url in Productivity class
            template_vars = { "my_user" : user}
            user.put() #puts user into datastore
            #qry = Productivity.query(Productivity.username == "nicki").fetch()
            self.response.out.write(user.username)
            #now instead of self writing it, make a template variable
            essayText = Productivity(essay=self.request.get("essay_text"))
            essay_vars = {"my_essay" : essayText}
            essayText.put()
            self.response.out.write(essayText.essay)
            #self.response.out.write(user) use this to view key after hitting submit







app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
