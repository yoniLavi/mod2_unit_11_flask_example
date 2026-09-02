import os

from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']


@app.route("/")
def home():
    return redirect("/contact")


@app.route("/contact", methods=["GET"])
def contact():
    return render_template(
        "contact.html",
        errors=[],
        name="",
        email="",
        subject="",
        message=""
    )


@app.route("/contact", methods=["POST"])
def contact_submission():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    subject = request.form.get("subject", "").strip()
    message = request.form.get("message", "").strip()

    errors = []

    if not name:
        errors.append("Name is required.")
    if not email:
        errors.append("Email is required.")
    if not subject:
        errors.append("Subject is required.")
    if not message:
        errors.append("Message is required.")

    if errors:
        flash("Invalid - please fix any errors and try again", "danger")
        return render_template(
            "contact.html",
            errors=errors,
            name=name,
            email=email,
            subject=subject,
            message=message
        )

    flash(f"Thanks {name}, we'll be in contact soon.", "success")
    return redirect("/contact")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
