from flask import *
import mlab
from models.service import Service
from models.customer import Customer
from models.user import User
from models.order import Order
from datetime import datetime
from gmail import *

app = Flask(__name__)
app.secret_key = "secret key"

#0. Create connection
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/search/<int:gender>')
# def search(gender):

#     all_service = Service.objects(gender=gender, yob__lte= 2018-20)
#     return render_template('search.html', all_service= all_service)

@app.route('/search')
def search():
    all_service = Service.objects()
    return render_template('search.html', all_service= all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
    if "signin" in session:
        one_service = Service.objects.get(id=service_id)
        if service_id is None:
            return "Not found"
        else:
            return render_template('detail.html', service=one_service)
    else:
        session['service_id'] = service_id
        return redirect(url_for('signin'))

@app.route('/customer')
def customer():
    all_customer = Customer.objects(gender=1,contacted=False)
    if len(all_customer) <= 10:
        result_customer = all_customer
    else:
        result_customer = all_customer[0:10]
    return render_template('customer.html',result_customer=result_customer)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service=all_service)

@app.route('/admin/delete/<service_id>')
def admin_delete(service_id):
    service_delete = Service.objects.get(id=service_id)
    if service_delete is None:
        return "Service not found"
    else:
        service_delete.delete()
        return redirect('/admin', code=302)

@app.route('/admin/update/<service_id>', methods=['GET', 'POST'])
def admin_update(service_id):
    service_update = Service.objects.get(id=service_id)
    if request.method == 'GET':
        if service_update is None:
            return "Service not found"
        else:
            return render_template('update.html', service=service_update)
    elif request.method == 'POST':
        form = request.form 
        name = form['name']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        phone = form['phone']
        address = form['address']
        # status = form['status']
        description = form['description']
        # measure = form['measure']

        service_update.update(
            set__name = name,
            set__yob = yob,
            set__gender = gender,
            set__height = int(height),
            set__phone = phone,
            set__address = address,
            # set__status = status,
            set__description = description,
            # set__measure = measure
        )
        service_update.reload()
        return redirect('/admin', code=302)

@app.route('/admin/add', methods=["GET", "POST"])
def admin_add():
    if request.method == "GET":
        return render_template('new_service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        address = form['address']
        phone = form['phone']
        height = form['height']
        gender = form['gender']


        new_service = Service(
            name=name,
            yob=yob,
            address=address,
            phone=phone,
            height=int(height),
            gender=gender
        )

        new_service.save()
        # print("Saved")
        return redirect('/admin', code=302)

@app.route('/admin/order')
def admin_order():
    all_order = Order.objects()
    return render_template('admin_order.html', all_order=all_order)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        form = request.form
        fullname = form['fullname']
        email = form['email']
        username = form['username']
        password = form['password']

        new_user = User(
            fullname = fullname,
            email = email,
            username = username,
            password = password
        ) 
        new_user.save()
        return redirect('/', code=302)

@app.route('/signin', methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template("signin.html")
    elif request.method == "POST":
        form = request.form 
        username = form['username']
        password = form['password']
        
        one_user = User.objects.get(username=username)
        if one_user is None:
            return "Tai khoan khong ton tai"
        else:
            if one_user['password'] == password :
                session['signin'] = True
                user_id = str(one_user['id'])
                session['user_id'] = user_id
                return redirect(url_for('detail',service_id=session['service_id']))
            else:
                return "dang nhap khong thanh cong"

@app.route('/signout')
def signout():
    del session['signin']
    return redirect(url_for('index'))

@app.route('/order/<service_id>')
def order(service_id):
    new_order = Order(
        service_id = service_id,
        user_id = session['user_id'],
        time_order = datetime.now().strftime("%I:%M %p"),
        is_accepted = False 
    )
    new_order.save()
    return "Da gui yeu cau"

@app.route('/order/accept/<order_id>')
def order_accept(order_id):
    one_order = Order.objects.get(id=order_id)
    if one_order is None:
        return "Khong ton tai"
    else:
        one_order.update(
            set__is_accepted = True
        )
        one_order.reload()
        gmail = GMail('LocTran<loctran.mict@gmail.com>','Mict12345')
        content="Yêu cầu của bạn đã được xử lý, chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất. Cảm ơn bạn đã sử dụng dịch vụ của ‘Mùa Đông Không Lạnh"
        msg = Message('Hello',to=one_order.user_id.email,html=content)
        gmail.send(msg)
        return redirect(url_for('admin_order'))

if __name__ == '__main__':
  app.run(debug=True)