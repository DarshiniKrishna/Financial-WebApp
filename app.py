from flask import Flask, render_template, request, jsonify
import google.generativeai as palm
import os
import numpy as np

api = os.getenv("MAKERSUITE_API_TOKEN")
model = {"model": "models/chat-bison-001"}
palm.configure(api_key=api)

if not api:
    raise ValueError("MAKERSUITE_API_TOKEN environment variable is not set")

app = Flask(__name__)
user_name = ""
flag = 1

@app.route("/",methods=["GET","POST"])
def index():
    global flag
    flag = 1
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    global flag, user_name
    if flag == 1:
        user_name = request.form.get("q")
        flag = 0 
    return(render_template("main.html",r=user_name))

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return(render_template("prediction.html"))

@app.route("/common_joke", methods=["GET", "POST"])
def common_joke():
    joke = "In Singapore, we don't need perfumes—we have durian. It’s nature’s way of saying, 'love me or leave me.'"
    return render_template("common_joke.html", j=joke)

@app.route("/DBS",methods=["GET","POST"])
def DBS():
    return(render_template("DBS.html"))

@app.route("/DBS_prediction",methods=["GET","POST"])
def DBS_prediction():
    q = float(request.form.get("q"))
    return(render_template("DBS_prediction.html",r=90.2 + (-50.6*q)))

@app.route("/makersuite",methods=["GET","POST"])
def makersuite():
    return(render_template("makersuite.html"))

@app.route("/makersuite_1", methods=["GET", "POST"])
def makersuite_1():
    try:
        q = "Can you help me prepare my tax return?"
        r = palm.chat(**model, messages=q)
        print(f"API Response: {r}")
        response_text = getattr(r, 'last', 'No response available')
        return render_template("makersuite_1_reply.html", r=response_text)
    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred while processing your request 1. Please try again later.", 500

@app.route("/makersuite_gen", methods=["GET", "POST"])
def makersuite_gen():
    try:
        q = request.form.get("q")
        r = palm.chat(**model, messages=q)
        print(f"API Response: {r}")
        response_text = getattr(r, 'last', 'No response available')
        return render_template("makersuite_gen_reply.html", r=response_text)
    except Exception as e:
        print(f"Error occurred: {e}")
        return "An error occurred while processing your request 2. Please try again later.", 500

if __name__ == "__main__":
    app.run(debug=True)
