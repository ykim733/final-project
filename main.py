

import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):

        userlogin = True
        if userlogin:

            self.response.out.write("There is a user")
        else:
            self.response.out.write("Hello world!")

    self.request.get(essay_text)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
