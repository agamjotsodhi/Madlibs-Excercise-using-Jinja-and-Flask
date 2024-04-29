from flask import Flask, render_template, request
from stories import story
app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"

@app.route("/")
def fill_questions():
    """ Show form and ask madlib questions"""
    prompts = story.prompts
    
    return render_template("homepage.html", prompts=prompts)

@app.route("/story")
def show_story():
    """Show story result."""

    text = story.generate(request.args)

    return render_template("story.html", text=text)


