from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("password_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""
    suggestion = ""
    color = "black"
    score = 0

    length = 0
    upper = 0
    lower = 0
    digit = 0
    special = 0

    if request.method == "POST":

        password = request.form["password"]

        length = len(password)
        upper = sum(1 for c in password if c.isupper())
        lower = sum(1 for c in password if c.islower())
        digit = sum(1 for c in password if c.isdigit())
        special = sum(1 for c in password if not c.isalnum())

        prediction = model.predict(
            [[length, upper, lower, digit, special]]
        )[0]

        if prediction == "weak":
            suggestion = "Use uppercase letters, numbers and special characters."
            color = "red"
            score = 30

        elif prediction == "medium":
            suggestion = "Increase password length and add more special characters."
            color = "orange"
            score = 70

        else:
            suggestion = "Excellent! Your password looks strong."
            color = "green"
            score = 100

    return render_template(
        "index.html",
        prediction=prediction,
        suggestion=suggestion,
        color=color,
        score=score,
        length=length,
        upper=upper,
        lower=lower,
        digit=digit,
        special=special
    )

if __name__ == "__main__":
    app.run(debug=True)