from flask import Flask,render_template,request
import google.generativeai as palm
import os

api = os.getenv("MAKERSUITE_API_TOKEN")
model = {"model":"models/chat-bison-001"}
palm.configure(api_key=api)

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    return(render_template("main.html",r=q))

@app.route("/makersuite",methods=["GET","POST"])
def makersuite():
    return(render_template("makersuite.html"))

@app.route("/makersuite_1",methods=["GET","POST"])
def makersuite_1():
    q = "Can you help me prepare my tax return?"
    r = palm.chat(**model, messages=q)
    return(render_template("makersuite_1_reply.html",r=r.last))

@app.route("/makersuite_gen",methods=["GET","POST"])
def makersuite_gen():
    q = request.form.get("q")
    r = palm.chat(**model, messages=q)
    return(render_template("makersuite_gen_reply.html",r=r.last))

if __name__ == "__main__":
    app.run()
