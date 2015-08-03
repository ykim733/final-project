

import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):

        userlogin = True
        if userlogin:
            self.response.out.write("Welcome!")
        else:
            self.response.out.write("Please login")
        template = jinja_environment.get_template('form.html')
        self.response.write(template.render())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
