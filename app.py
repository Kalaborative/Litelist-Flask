from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)

# Why choose us?
# We offer full control over your tasks combined with a hint of flair.

# You decide how secure you want your lists to be: private to yourself or share w/ others

# Many customization options, a real-time progress bar, and much more!