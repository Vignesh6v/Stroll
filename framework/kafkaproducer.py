import json
from kafka import SimpleProducer, KafkaClient
from flask import Flask, request, jsonify, session, render_template,session
app = Flask(__name__)


@app.route('/api/login', methods=['POST'])
def login():
    req = request.json
    print req
    _uname = req['username']
    _pass = req['password']
    status = False
    try:
        print _uname, _pass
        '''
        if _uname and _pass :
            # check user and password are correct in ES
            if ok:
                status = True
                return jsonify({'message':'Login Successfull','code':'200','result': status, 'user': req})
            else:
                status = True
                return jsonify({'message':'Enter Valid Username/Password','code':'201','result': status})
        else:
            status = True
            return jsonify({'message':'User not registered or Invalid Username/Password','code':'201','result': status})
        '''
        return jsonify({'message':'Login Successfull','code':'200','result': True, 'user': _uname})
    except Exception, e:
        print "ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1])
        return False


@app.route("/api/logout")
def logout():
    return jsonify({"result": "success"})


@app.route('/api/signup',methods = ['POST'])
def signup():
    req = request.json
    username = req['username']
    email = req['email']
    password = req['password']
    lastname = req['lastname']
    firstname = req['firstname']

    '''check if the username exist or the email id exist
       if not create the user

    '''
    val = 201
    posts = {}
    if val == 201:
    	posts['status'] = "Success"
    	posts['message'] = "Inserted"
    else:
    	posts['status'] = "Failed"
    	posts['message'] = "User Name already taken"
    return jsonify(posts)

if __name__ == "__main__":
    app.debug = True
    app.run()
