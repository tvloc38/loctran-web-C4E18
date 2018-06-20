from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def about():
    return render_template('about.html')

@app.route('/school')
def school():
    return redirect('http://techkids.vn', code=302)

@app.route('/bmi/<int:w>/<int:h>')
def bmi(w, h):
    h_m = float(h/100)
    bmi = float(w/(h**2))

    if bmi < 16:
        condition = "Severely underweight"
    elif bmi < 18.5:
        condition = "Underweight"
    elif bmi < 25:
        condition = "Normal"
    elif bmi <= 30:
        condition = "Overweight"
    else:
        condition = "Obese"
    # return "bmi = {0} => {1}".format(bmi,condition)  #Without render_template
    return render_template('bmi.html', bmi=bmi, condition=condition)  #With render_template

@app.route('/user/<username>')
def user(username):
    users = {
	    "quy" :{
			"name" : "Dinh Cong Quy",   
			"age" : 20
        },
        "tuananh" :{
			"name" : "Huynh Tuan Anh",
			"age" : 22
        }
    }

    return render_template('user.html', users=users, username=username)



if __name__ == '__main__':
  app.run(debug=True)
 