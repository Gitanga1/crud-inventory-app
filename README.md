# 📦 Inventory Management System

A full-stack CRUD web application for local small and medium enterprises (SMEs) to manage products, track stock levels, and export data.

## 🚀 Live Demo

**[https://crud-inventory-app.onrender.com](https://crud-inventory-app.onrender.com)**

## 📋 Features

| Feature | Description |
|---------|-------------|
| **Create** | Add new products with name, price, and quantity |
| **Read** | View all products in a sortable table |
| **Update** | Edit product details inline |
| **Delete** | Remove products (password protected) |
| **Search** | Filter products by name in real-time |
| **Low Stock Alert** | Visual warning when quantity < 5 |
| **Export CSV** | Download product data as spreadsheet |
| **Cloud Database** | Persistent storage with Supabase PostgreSQL |

## 🛠️ Technology Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.14, Flask 3.0.0 |
| Database | PostgreSQL (Supabase) / SQLite (local) |
| ORM | SQLAlchemy |
| Frontend | HTML5, CSS3, Jinja2 templating |
| Deployment | Render.com |
| Version Control | Git, GitHub |

## 🏗️ Project Structure
crud-inventory-app/
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend UI template
├── instance/ # Local SQLite database (not on GitHub)
└── docs/ # Documentation


## 💻 Local Development

### Prerequisites
- Python 3.14 or higher
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Gitanga1/crud-inventory-app.git
cd crud-inventory-app

# Create virtual environment
python -m venv venvv
source venvv/bin/activate  # On Windows: venvv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

Environment Variables (for production)
Variable	Description
DATABASE_URL	PostgreSQL connection string (Supabase)
PORT	Server port (default: 5000)
🔐 Default Admin Password
Delete operations require password: admin123

📤 Export Format
CSV files include:

Product Name

Price (Ksh)

Quantity

🌐 Deployment
The app is deployed on Render.com with:

Free tier web service

Supabase PostgreSQL for persistent storage

Automatic HTTPS

Continuous deployment from GitHub

👩‍💻 Author
Grace Gitanga

GitHub: @Gitanga1

Email: gitangagrace@gmail.com

📄 License
This project is open source and available under the MIT License.

🎯 Future Enhancements
User authentication (login system)

Product categories

Image uploads

Sales/checkout feature

Barcode generation

PDF receipt printing

Mobile responsive redesign