from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)
static_DB = {"Jente":"1234","Etnej":"4321"}

@app.route("/")
def index():
    return render_template("FEP.html")

@app.route("/connectionStatus", methods=["POST"])
def connectionStatus():
    page_status = "Connected"
    return page_status

@app.route("/infoHandler", methods=["POST"])
def infoHandler():
    if request.method == "POST":
        in_SDB = False
        info_list = request.form
        name = info_list.get("name")
        password = info_list.get("password")
        DBM = info_list.get("debug")
        SDB_pass = static_DB.get(name)
        if SDB_pass == password:
            in_SDB = True
        if DBM == "true":
            form_status = f"The backend has received the data. (debug: --n.[{name}] --p.[{password}] --ISDB[{in_SDB}] --DBM[{DBM}])"
        elif DBM == "false":
            form_status = "The backend has received the data."
        else:
            form_status = "Not all settings have been set correctly."
        return_data = {"form_status":form_status,"ISDB":in_SDB}
        return return_data

if __name__ == '__main__':
    devMode = False
    if devMode:
        print("devMode is enabled")
        app.run( 
            host="codespaces-d57c39",
            port=5001, 
            debug=True,
            )
    else:
        serve(
            app,
            host="codespaces-d57c39",
            port=5001,
            )