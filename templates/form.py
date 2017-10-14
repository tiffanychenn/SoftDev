from flask import Flask, render_template

jinjas_in_the_night = Flask(__name__)

@jinjas_in_the_night.route("/")
def root():
	return render_template("form.html")
	
if __name__ == "__main__":
	jinjas_in_the_night.debug = True
	jinjas_in_the_night.run()

