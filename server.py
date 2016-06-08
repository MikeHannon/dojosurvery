# This server will load 2 pages: the form, and the results.
# The various data that we pass to our results page will be held in session data!
# Our server needs to be able to listen for requests - Flask takes care of this!
# Our server needs to be able to render templates - Flask can take care of this, if we import render_template
# Our server needs to be able to redirect -  Flask can take care of this, if we import redirect
# Our server needs to hold session, or a subset of session (called Flash) -- Flask can take care of either of these if we import session and flash.

from flask import Flask, request, render_template, session, redirect, flash
import random
# our server object!
app = Flask(__name__)

app.secret_key = "293akljsdf;oaiur7897p987kajsdf;y8"
# we need a secret key to use session.
# our server listens for these routes!
@app.route('/')
def render_index():
    # we got render_template from the flask import!

    # templates that get rendered need to be in a templates folder
    return render_template("index.html")
# this '/result' <-- is catches any string that matches '/result' we type into our browser, after localhost:5000
@app.route('/result')
def render_result():
        # we got render_template from the flask import!

        # templates that get rendered need to be in a templates folder
    random_thing = random.randint(0,5000)
    print random_thing
    return render_template("results.html", somerandomthing = random_thing)


#We need another route to get the info from our form when we post <-- let's call it /process_data
@app.route('/process_data', methods = ['POST'])
def results():
    """
    request.form:
    1) it catches the data from a form!
        a) it only catches fields that have a name!
        b) it is only available for posts!
            i) request.args.get <-- for gets
    2) That form has an action associated with it <-- in this case '/process_data'

    """
    """
    session is a dictionary!

    """
    print ("*")*50
    print ("*")*50
    myDictionary = {}
    for key in request.form:
        if key == "name":
            if len(request.form['name']) < 3:
                myDictionary[key] = "name is too short"
            else:
                myDictionary[key] = request.form[key]
        else:
            myDictionary[key] = request.form[key]
        # print(session[key])
    flash(myDictionary)
    print ("*")*50
    print ("*")*50

    return redirect('/result')
# to turn our server on!
# debug = True <-- gives us debugging errors!
app.run(debug=True)

"""
Session! <-- Gets stored!
If you quite the browser session gets deleted
Session <-- its a dictionary!
Jinja2 -- , using {{ session ['key'] }} and/or flash messages
app.run  - changing port (port=8821) e.g. so we can run on localhost:8821 and run multiple python servers at once!  (we are already potentially starting to run a sql server and a python server)
"""
