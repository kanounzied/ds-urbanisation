from flask import Flask

from db import Employee

app = Flask(__name__)
app.config['DEBUG'] = True
SESSION_TYPE = 'mongodb'
app.config.from_object(__name__)


@app.route("/users", methods=['GET'])
def users():
    emp = Employee.find({})
    data = list([])
    for doc in emp:
        data.append(doc["name"])
    return data

@app.route("/user/<id>", methods=['POST'])
def adduser(id):
    Employee.insert_one({

    })


if __name__ == '__main__':
    app.run(host='0.0.0.0')
