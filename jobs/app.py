from flask import Flask, render_template 

#Flask Instance
app = Flask(__name__)

#Create templates folder in jobs and an index.html in this templates folder

#Create a route
@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')