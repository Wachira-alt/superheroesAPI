
# Superheroes API

A Flask RESTful API for managing heroes, their powers, and strength levels using a many-to-many relationship with validations and modular structure.

---

## Features

- List all heroes and their super names
- Retrieve a single hero with powers and strength levels
- List all powers
- Update a power's description
- Create a new HeroPower with validation
- Error handling with proper HTTP status codes
- Modular structure (models, resources, config, etc.)
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
- SQLite (default)

---

## Project Structure

```

superheroesAPI/
├── models/
│   ├── hero.py
│   ├── power.py
│   └── hero\_power.py
├── resources/
│   ├── hero\_resource.py
│   ├── power\_resource.py
│   └── hero\_power\_resource.py
├── app.py
├── run.py
├── seed.py
├── config.py
├── extensions.py
├── .env
├── .gitignore
└── README.md

````

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/superheroesAPI.git
cd superheroesAPI
````

### 2. Install Dependencies

```bash
pipenv install
```

### 3. Activate the Virtual Environment

```bash
pipenv shell
```

### 4. Set Environment Variables

Create a `.env` file with:

```env
FLASK_APP=run.py
FLASK_ENV=development
```

### 5. Run Migrations

```bash
flask db init       # only once
flask db migrate -m "initial"
flask db upgrade
```

### 6. Seed the Database

```bash
python seed.py
```

### 7. Start the Server

```bash
flask run
```

---

## API Endpoints

### GET /heroes

Returns a list of all heroes.

### GET /heroes/<id>

Returns a specific hero with powers.

### GET /powers

Returns all powers.

### GET /powers/<id>

Returns a specific power.

### PATCH /powers/<id>

Updates the description of a power. Description must be at least 20 characters.

### POST /hero\_powers

Creates a new HeroPower. Strength must be one of: `Strong`, `Weak`, `Average`.

---

## Validations

* `Power.description` must be at least 20 characters.
* `HeroPower.strength` must be `Strong`, `Weak`, or `Average`.

---

## Author

Dennis Wachira




