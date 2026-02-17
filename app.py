from flask import Flask, request, render_template_string
import random

app = Flask(__name__)
number_to_guess = random.randint(1, 20)

HTML = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Guess the Number Game</title>
  <style>
    body { 
      font-family: Arial, sans-serif; 
      background: linear-gradient(to right, #ffecd2, #fcb69f); 
      text-align: center; 
      padding-top: 50px;
    }
    h1 { color: #d64161; }
    input[type=number] { padding: 10px; font-size: 16px; width: 60px; }
    input[type=submit] { padding: 10px 20px; font-size: 16px; background-color: #6a2c70; color: white; border: none; border-radius: 5px; cursor: pointer; }
    input[type=submit]:hover { background-color: #b83b5e; }
    p { font-size: 20px; color: #1b262c; }
    .container { background: rgba(255,255,255,0.8); display: inline-block; padding: 30px; border-radius: 10px; }
  </style>
</head>
<body>
  <div class="container">
    <h1>Guess a number between 1 and 20!(version 2) </h1>
    <form method="POST">
      <input type="number" name="guess" min="1" max="20" required>
      <input type="submit" value="Guess!">
    </form>
    {% if message %}
    <p>{{ message }}</p>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    global number_to_guess
    message = ""
    if request.method == "POST":
        guess = int(request.form.get("guess", 0))
        if guess < number_to_guess:
            message = "⬆ Too low!"
        elif guess > number_to_guess:
            message = "⬇ Too high!"
        else:
            message = "🎉 Correct! I picked a new number."
            number_to_guess = random.randint(1, 20)
    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    