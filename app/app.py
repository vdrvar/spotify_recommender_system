from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Placeholder functionality for resetting any 'favorites' related variable
    # This could be where you reset a session variable or similar in the future
    return render_template('index.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/recommend')
def recommend():
    return render_template('recommend.html')


if __name__ == '__main__':
    app.run(debug=True)
