from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/")
def hello_world() : 
    return render_template('hello.html')

@app.route("/hello", methods = ['GET', 'POST'])
# by default its get only, there are other methods like delete
def hello_world_name() : 
    if request.method == 'GET' :
        return render_template('get_details.html')

    elif request.method == 'POST' : 
        userName = request.form['userName']
        return render_template('display.html', display_name = userName)
    else : 
        print('error check')

if __name__ == '__main__' : 
    # port 5000 by default
    app.debug = True
    # for production it should be false 
    app.run()