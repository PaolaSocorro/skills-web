from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    # Return this as a strange
    # return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def form_page():
    firstname = request.form.get("fname");
    lastname = request.form.get("lname");
    salary = request.form.get("sal");
    jobselect = request.form.get("job");
    return render_template("response.html", fname=firstname,lname=lastname,job=jobselect,sal=salary)

if __name__ == "__main__":
    app.run(debug=True)

# Thank you, {{fname}} {{lname}}, for applying to be a {{job}}. 
#             Your nminimum salary requirement is {{sal}} dollars.

# methods=["POST"]