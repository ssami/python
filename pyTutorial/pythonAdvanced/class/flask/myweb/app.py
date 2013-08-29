from flask import Flask, request, render_template
from fabric import tasks 
from fabric.api import run, settings

HOST = "ec2-107-21-80-136.compute-1.amazonaws.com"
USER = "student4"
PASS = "letmein"

app = Flask(__name__)

def run_command(**kwargs):
    print kwargs
    user = kwargs.get('name')[0]                           # we use a "get" to safely return None or the object (no need to check for "in")
    password = kwargs.get('password')[0]
    command = kwargs.get('command')[0]
    with settings(host_string=HOST,
                  user=user,
                  password=password):
        output = run(command)
    return output

@app.route('/test', methods=["POST"])
def test(): 
    context = {}
    
    # return "Hello world test!"
#     template = []
#     template.append("Your request method is: %s <br>" % request.method)
#     template.append("You sent me the following form: ")
#     for name, value in request.form.items():            # if you had put just "i" or "name" instead of name, value, you would get a tuple 
#         template.append("%s %s " % (name, value))       # tuple-ize these values before printing them!
    
    context['output'] = run_command(**request.form).splitlines() 
    context['command'] = request.form['command']
    return render_template("output.html", **context)



@app.route('/', methods=["GET"])
def home():
    context = {}
    context['header'] = 'HAXZORZ'
    
    return render_template("index.html", **context)




if __name__ == "__main__":
    app.debug = True
    app.run()