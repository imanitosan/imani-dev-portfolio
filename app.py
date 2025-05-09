from email.mime import application
from flask import Flask, redirect, render_template, request



app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("project.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        print(f"Message from {name} ({email}): {message}")
        return render_template("contact.html", success=True)
    return render_template("contact.html", success=False)


# Force HTTPS in production
@app.before_request
def force_https():
    if not request.is_secure and request.headers.get('X-Forwarded-Proto') == 'http':
        return redirect(request.url.replace('http://', 'https://', 1))

# Your existing routes here.............


if __name__ == "__main__":
    app.run(debug=True)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


