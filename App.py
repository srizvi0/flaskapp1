from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/welcome<name>')
def Welcome(name):
    return "Welcome to the page " + name

@app.route('/result', methods=["GET"])
def result():
    if request.method == "GET":
        result = str(request.args.get("result"))
        return f"Result = {result}"
@app.route('/default', methods=["POST", "GET"])
def default(): 
    if request.method == "POST":
        NumberA_str = request.form.get("NumberA")
        NumberB_str = request.form.get("NumberB")
        Oper = request.form.get("Operator")
        print("NumberA_str:", NumberA_str)
        print("NumberB_str:", NumberB_str)
        print("Oper:", Oper)
        if NumberA_str and NumberB_str and Oper is not None:
            NumberA = int(NumberA_str)
            NumberB = int(NumberB_str)
            if Oper == '+':   
                Result = NumberA + NumberB
            elif Oper == "-":
                Result = NumberA - NumberB
            elif Oper == "*":
                Result = NumberA * NumberB
            elif Oper == "/":
                if NumberB == 0:
                    return 'Invalid Denominator'
                Result = NumberA / NumberB
            else:
                return "Invalid input"                        
            redirect_url1 = redirect(f"http://127.0.0.1:5000/result?result={Result}") 
            return redirect_url1                        
        else: 
            return "One or more form fields are empty"
    else:
        return render_template('app.html')

if __name__ == '__main__':
    app.run(debug=True)
