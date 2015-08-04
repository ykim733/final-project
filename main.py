
from google.appengine.ext import ndb
import webapp2
import jinja2
import os
import time
import threading

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
            self.response.out.write(user.username)
            #now instead of self writing it, make a template variable
            essayText = Productivity(essay=self.request.get("essay_text"))
            essay_vars = {"my_essay" : essayText}
            essayText.put()
            self.response.out.write(essayText.essay)
            #self.response.out.write(user) use this to view key after hitting submit

<<<<<<< HEAD

            userlogin = True
            if userlogin:
                self.response.out.write("<h1>Welcome!</h1>")
            else:
                self.response.out.write("Please login")
            template = jinja_environment.get_template('form.html')
            self.response.write(template.render())
=======
class ArchiveHandler(webapp2.RequestHandler):
    def get(self):
         archive_template = jinja_environment.get_template('templates/archive.html')
         self.response.out.write(archive_template.render())
        #
        #
        # userlogin = True
        # if userlogin:
        #     self.response.out.write("<h1>Welcome!</h1>")
        # else:
        #     self.response.out.write("Please login")
        # template = jinja_environment.get_template('form.html')
        # self.response.write(template.render())
>>>>>>> a11cda2261525b46f462a7339b4b49cac2bb766e


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/myessays', ArchiveHandler)
], debug=True)
