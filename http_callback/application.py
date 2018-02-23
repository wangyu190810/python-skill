from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def index():
    return "NO callback"


@app.route("/index")
def first_index():
    print(dir(request))
    return str(request.user_agent)


if __name__ =="__main__":
    app.run(debug=True)
    #app.debug()
