from flask import Flask, render_template, request, url_for,redirect
app = Flask(__name__)

@app.route('/welcome<name>')
def Welcome (name):
    return "Welcome to the page " + name

@app.route('/result', methods = ["GET"])
def result():
    if(request.method == "GET"):
        result = str(request.args.get("result"))
        return f"Result = {result}"

@app.route('/default', methods=["POST","GET"])
def default(): 
    if (request.method=="POST"):
        Number1 = int(request.form.get("Number1"))
        Number2 = int(request.form.get("Number2"))
        Oper = (request.form.get("Operator"))
        if Number1 and Number2 and Oper is not None:
            if (Oper=='+'):   
                Result = (Number1) + (Number2)
            elif(Oper =="-"):
                Result = (Number1) - (Number2)
            elif(Oper=="*"):
                Result = (Number1)*(Number2)
            elif(Oper=="/"):
                Result = (Number1)/(Number2)
                if (Number2>Number1):
                    return 'Invalid Numerator'     
            else:
                "invalid input" 
                        
            redirect_url1 = redirect(f"http://127.0.0.1:5000/result?result={Result}") 
            return redirect_url1                        
        else: 
            return "This is a None character"          
        
    else:
        return render_template('app.html')


if __name__ == '__main__':
    app.run(debug=True)