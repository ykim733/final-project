
from google.appengine.ext import ndb
import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class Productivity(ndb.Model):
    essay = ndb.StringProperty(required = False)
    username = ndb.StringProperty(required = True)
    password = ndb.StringProperty(required = False)



# Hai girl hai, so I got the user input working in the url input, but I haven't been able to link it in a form good luck!
# btw I just added a username input in the form with the essay entitle from.html

class MainHandler(webapp2.RequestHandler):
    def get(self):
            first_template = jinja_environment.get_template('form.html') #this isn't working
            user = Productivity(username=self.request.get("user"))
            user.put()
            qry = Productivity.query(Productivity.username == "nicki").fetch()
            self.response.out.write(first_template.render(user)) #this isn't working either
            self.response.out.write(qry)






app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
