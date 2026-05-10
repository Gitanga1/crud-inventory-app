# Technical Documentation

## Architecture Overview
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ Browser │────▶│ Render │────▶│ Supabase │
│ (Client) │◀────│ (Flask) │◀────│ (PostgreSQL)│
└─────────────┘ └─────────────┘ └─────────────┘


## Database Schema

### Product Table

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | Integer | PRIMARY KEY | Auto-incrementing ID |
| name | String(100) | NOT NULL | Product name |
| price | Float | NOT NULL | Price in Ksh |
| quantity | Integer | DEFAULT 0 | Stock count |

## API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/` | View all products | No |
| POST | `/add` | Create new product | No |
| POST | `/update/<id>` | Update product | No |
| GET | `/delete/<id>` | Delete product | Yes (password) |
| GET | `/search?q=` | Search products | No |
| GET | `/export` | Download CSV | No |

## Environment Variables

| Variable | Required | Default | Production Value |
|----------|----------|---------|------------------|
| `DATABASE_URL` | Yes | None | Supabase PostgreSQL URI |
| `PORT` | No | 5000 | 10000 (Render) |

## Local Development Setup

```bash
# Clone and setup
git clone https://github.com/Gitanga1/crud-inventory-app.git
cd crud-inventory-app
python -m venv venvv
source venvv/bin/activate  # Windows: venvv\Scripts\activate
pip install -r requirements.txt

# Run locally
python app.py

Deployment to Render
Push code to GitHub

Connect repository to Render

Set environment variables

Deploy with gunicorn app:app

Database Migration (SQLite → PostgreSQL)
The app automatically detects DATABASE_URL environment variable:

If present → connects to PostgreSQL (Supabase)

If absent → uses local SQLite file

Security Notes
Delete operations require ?password=admin123 parameter

Password is hardcoded - change in production

Database credentials stored as environment variables

SSL enforced on Supabase connections

Performance Considerations
Free tier limits: 1 CPU, 512MB RAM

Cold starts: 30-50 seconds after inactivity

Database connection: Supabase free tier (max 200 connections)

Testing
bash
# Test database connection
python -c "from app import db; db.create_all(); print('OK')"

# Test local server
python app.py
# Visit http://localhost:5000

Contributing
Fork the repository

Create feature branch

Commit changes

Push to branch

Open Pull Request