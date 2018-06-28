from flask import *
import mlab
from models.service import Service
from models.customer import Customer

app = Flask(__name__)

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
    one_service = Service.objects.get(id=service_id)
    if service_id is None:
        return "Not found"
    else:
        return render_template('detail.html', service=one_service)

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
        measure = form['measure']

        service_update.update(
            set__name = name,
            set__yob = yob,
            set__gender = gender,
            set__height = height,
            set__phone = phone,
            set__address = address,
            # set__status = status,
            set__description = description,
            set__measure = measure
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
        gender = form['gender']


        new_service = Service(
            name=name,
            yob=yob,
            address=address,
            phone=phone,
            gender=gender
        )

        new_service.save()
        # print("Saved")
        return redirect('/admin', code=302)

if __name__ == '__main__':
  app.run(debug=True)