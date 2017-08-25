from flask import Flask, render_template 
from tophashtags import hashtaglist

import numpy as np
app= Flask("My App")




@app.route('/')
def index():
	return render_template("index.html")

@app.route('/analysis')
def file():
	return render_template("analysis.html", arr = hashtaglist)


if __name__=="__main__":
	app.run(debug=True)
