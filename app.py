from flask import Flask,make_response,request

app = Flask(__name__)

@app.route("/home")
def home():
    name = request.cookies.get('name')
    resp = make_response({"name":name})
    return resp

@app.route("/set_cookie",methods=["POST"])
def set_cookie():
    data = request.json
    resp = make_response({"message":"Cookies has been set"})
    resp.set_cookie("name",data["name"])
    return resp

@app.route("/set_cookie/<name>",methods=["GET"])
def set_cookie_dynamic(name):
    resp = make_response({"message":"Cookies has been set"})
    resp.set_cookie("name",name)
    return resp


if __name__ == "__main__":
    app.run(port=8080,debug=True)