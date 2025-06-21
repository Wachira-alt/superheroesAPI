# Superheroes API

A Flask RESTful API for managing heroes, their powers, and their strength levels using a many-to-many relationship with validations and a clean modular structure.

---

## Features

- List all heroes and their super names
- Retrieve a single hero with all powers and strength levels
- List all powers
- Update a power's description
- Create a new HeroPower with validation
- Error handling with proper HTTP status codes
- Modular project structure (models, resources, config, etc.)
- Database migrations with Flask-Migrate
- Serialization with `sqlalchemy-serializer`

---

## Technologies Used

- Python 3.8+
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Migrate
- SQLAlchemy Serializer
- SQLite (default database)

---

## Project Structure

superheroesAPI/
├── models/
│   ├── hero.py
│   ├── power.py
│   └── hero_power.py
├── resources/
│   ├── hero_resource.py
│   ├── power_resource.py
│   └── hero_power_resource.py
├── app.py
├── run.py
├── seed.py
├── config.py
├── extensions.py
├── .env
├── .gitignore
└── README.md

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/superheroesAPI.git
cd superheroesAPI
