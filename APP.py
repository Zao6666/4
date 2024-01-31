from flask import Flask,request,render_template
import json
import time
import requests

headers={
    "Authorization" : "Token 787f515cb0624813736c11e7fefec66473394f02",
    "Content-Type" : "application/json"
}

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        data = json.dumps(
            {
                "version" : "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",    
                "input" : {"prompt":q}
            }
        )
        r = requests.post('https://api.replicate.com/v1/predictions',data=data,headers=headers)
        time.sleep(20)
        r = r.json()["urls"]["get"]
        r = requests.post(r,headers=headers).json()["output"]
        return(render_template("index.html",r=r[0]))
    else:
        return(render_template("index.html",r="Waiting for your entry"))

if __name__ == "__main__":
    app.run()
