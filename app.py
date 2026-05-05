from flask import Flask, render_template, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
import os
import csv
import io

app = Flask(__name__)

# Create data directory on C: drive if it doesn't exist
DATA_DIR = 'C:/my_crud_app_data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATA_DIR}/products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Simple password protection
ADMIN_PASSWORD = "admin123"

def check_auth():
    password = request.args.get('password') or request.form.get('password')
    return password == ADMIN_PASSWORD

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=0)

with app.app_context():
    db.create_all()

def get_low_stock_count():
    return Product.query.filter(Product.quantity < 5).count()

@app.route('/')
def index():
    products = Product.query.all()
    low_stock_count = get_low_stock_count()
    return render_template('index.html', products=products, low_stock_count=low_stock_count)

@app.route('/add', methods=['POST'])
def add_product():
    name = request.form['name']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    new_product = Product(name=name, price=price, quantity=quantity)
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_product(id):
    product = Product.query.get_or_404(id)
    product.name = request.form['name']
    product.price = float(request.form['price'])
    product.quantity = int(request.form['quantity'])
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_product(id):
    if not check_auth():
        return "Access Denied. Add ?password=admin123 to the URL", 401
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/search')
def search():
    query = request.args.get('q', '')
    if query:
        products = Product.query.filter(Product.name.contains(query)).all()
    else:
        products = Product.query.all()
    low_stock_count = get_low_stock_count()
    return render_template('index.html', products=products, low_stock_count=low_stock_count)

@app.route('/export')
def export():
    products = Product.query.all()
    output = []
    output.append(['Name', 'Price (Ksh)', 'Quantity'])
    for p in products:
        output.append([p.name, p.price, p.quantity])
    
    output_file = io.StringIO()
    writer = csv.writer(output_file)
    writer.writerows(output)
    
    response = Response(output_file.getvalue(), mimetype='text/csv')
    response.headers.set('Content-Disposition', 'attachment', filename='products_export.csv')
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)