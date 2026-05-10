from flask import Flask, render_template, request, redirect, url_for, Response
from flask_sqlalchemy import SQLAlchemy
import os
import csv
import io

app = Flask(__name__, template_folder='templates')

# --- SUPABASE POSTGRESQL CONNECTION ---
DATABASE_URL = os.environ.get('DATABASE_URL', '')

if not DATABASE_URL:
    # Fallback for local testing - REPLACE WITH YOUR ACTUAL CONNECTION STRING
    DATABASE_URL = 'postgresql://postgres.pksuygxytkjqfxfazyzl:YOUR_ACTUAL_PASSWORD@aws-1-eu-central-1.pooler.supabase.com:5432/postgres'
    print("⚠️ WARNING: Using hardcoded database URL. Set DATABASE_URL in production!")

if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_pre_ping': True,
    'pool_recycle': 300,
}

db = SQLAlchemy(app)

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
    print("✅ Database connected to Supabase PostgreSQL!")
    count = Product.query.count()
    print(f"📊 Current product count: {count}")

def get_low_stock_count():
    return Product.query.filter(Product.quantity < 5).count()

@app.route('/')
def index():
    products = Product.query.all()
    low_stock_count = get_low_stock_count()
    print(f"📊 Loaded {len(products)} products from Supabase")
    return render_template('index.html', products=products, low_stock_count=low_stock_count)

@app.route('/add', methods=['POST'])
def add_product():
    name = request.form['name']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    new_product = Product(name=name, price=price, quantity=quantity)
    db.session.add(new_product)
    db.session.commit()
    print(f"💾 SAVED to Supabase: {name}")
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
        return "Access Denied", 401
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
    output = [['Name', 'Price (Ksh)', 'Quantity']]
    for p in products:
        output.append([p.name, p.price, p.quantity])
    
    output_file = io.StringIO()
    writer = csv.writer(output_file)
    writer.writerows(output)
    
    response = Response(output_file.getvalue(), mimetype='text/csv')
    response.headers.set('Content-Disposition', 'attachment', filename='products_export.csv')
    return response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)