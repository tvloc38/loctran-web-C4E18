from flask import Flask, render_template
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

@app.route('/search/<int:gender>')
def search(gender):
    all_service = Service.objects(gender=gender)
    return render_template('search.html', all_service= all_service)

@app.route('/customer')
def customer():
    all_customer = Customer.objects(gender=1,contacted=False)
    if len(all_customer) <= 10:
        result_customer = all_customer
    else:
        result_customer = all_customer[0:9]
    return render_template('customer.html',result_customer=result_customer)

if __name__ == '__main__':
  app.run(debug=True)