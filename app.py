from flask import flask,request,redirect,url_form,render_template
app = Flask(__name__)
@app.router("/")
def  index()
    return