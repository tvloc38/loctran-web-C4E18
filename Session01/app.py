from flask import Flask,render_template
app = Flask(__name__)


@app.route('/')             #route: trang con
def index():

    posts = [
        {
            "title": "Thơ 3 dòng",
            "content": "Dòng 1.Dòng 2.Dòng 3",
            "author": "Loc Tran",
            "gender": 0
        },
        
        {
            "title": "Thơ 3 dòng 1",
            "content": "Dòng 1.Dòng 2.Dòng 3",
            "author": "Loc Tran",
            "gender": 0
        },

        {
            "title": "Thơ 3 dòng 2",
            "content": "Dòng 1.Dòng 2.Dòng 3",
            "author": "Loc Tran",
            "gender": 0
        },

        {
            "title": "Thơ 3 dòng 3",
            "content": "Dòng 1.Dòng 2.Dòng 3",
            "author": "Loc Tran",
            "gender": 1
        }
    ]

    # first_post = posts[0]
    return render_template("index.html", post=posts)

@app.route('/hello')
def say_hello():
    return "<h1>Hello C4E18</h1>"

@app.route('/hi/<name>/<age>')          #parameter: <>
def say_hi(name, age):
    return "Hi {0}, you re {1} years old".format(name, age)     #return khong duoc moi so

@app.route('/sum/<int:x>/<int:y>')
def su(x, y):
    su = x + y
    return "{0} + {1} = {2}".format(x, y, su)

if __name__ == '__main__':  #khi mà file app.py được chạy trực tiếp
  app.run(debug=True)       #khởi động server
 
