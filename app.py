from flask import Flask, render_template
from affirm import get_random_affirmations

app = Flask(__name__, template_folder= "templates", static_folder="static")

@app.route("/")
def home():
    quote = get_random_affirmations()
    return render_template("index.html", affirmation=quote)

if __name__ == "__main__":
    app.run(debug=True)