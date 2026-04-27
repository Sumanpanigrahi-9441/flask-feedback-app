from flask import Flask, render_template, request, redirect

app = Flask(__name__)

feedbacks = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        email = request.form.get("email")
        
        if not name or not message or not email:
            return "❌ Please fill all fields"

        feedbacks.append((name, message , email))
        return redirect("/")

    return render_template("feedback.html", feedbacks=feedbacks)

if __name__ == "__main__":
    app.run(debug=True)
