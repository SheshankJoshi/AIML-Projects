from flask import Flask

app=Flask(__name__)

@app.route("/")
def Entry_point():
    print("This is a test app, that is deployed on Heroku by Sheshank Joshi\n")
    print("This is just for testing purpose only")
    print("Very soon Links will be added here for all the data that I have used")
    return 
