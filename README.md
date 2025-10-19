# 🧾 Egyptian National ID Validator API

A Django REST Framework (DRF) project that validates Egyptian National ID numbers and extracts useful details such as date of birth, gender, and province.  
Supports both **Token Authentication** (for users) and **API Key Authentication** (for external apps or anonymous usage). All validations are based on information by
https://en.wikipedia.org/wiki/Egyptian_National_Identity_Card#National_Number 

---

## Features

- Validate Egyptian National ID numbers.
- Extract:
  - Birth date (and check validity / future dates)
  - Province (from digits 8–9)
  - Gender (from serial digits)
  - Same day births
- Authentication:
  - `TokenAuthentication` for registered users.
  - `APIKeyAuthentication` for anonymous apps.
- Rate limiting using DRF throttling (`100/hour` for users, `10/hour` for anonymous).
- Clean serializer-based validation.

## How to Run the Applicaiton

- **Download Python:** [https://www.python.org/downloads/](https://www.python.org/downloads/)
- **Create virtual environment:** `python -m venv venv`
- **Run virtual environment:** `./venv/Scripts/activate`
- **Install project dependencies:** `pip install -r requirements.txt`
- **Create superuser for admin page:** `python manage.py createsuperuser`
- **Migrate models and DRF:** `python manage.py migrate`
- **Run server:** `python manage.py runserver`
- **Open admin page:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
- **Log in with superuser**
- **Add Token** for user to use **Token Authentication** (users)
- **Add API Key** for client to use **API-key Authentication** (anons)

## CheckID API

- **Use Postman to test the API:** [https://www.postman.com/downloads/](https://www.postman.com/downloads/)
- **Create a new POST request:** `http://127.0.0.1:8000/IDValidator/CheckID/`
- **Add the request body (JSON):**
  ```json
  {
      "national_id": "##############"
  }
- Put in Headers -> Key : Authorization , Value : Api-Key <API-Key generated> (to use the API-key authentication) LIMIT 10/Hour
- Put in Headers -> Key : Authorization , Value : Token <Token generated> (to use the Token authentication) LIMIT 100/Hour
- Choose which Auth you want to use to send the API
- You can adjust the rate limiter in settings.py under 'DEFAULT_THROTTLE_RATES'

## Decisions

- Used DRF’s built-in throttling and applied it globally since there’s only one public API endpoint.
- Used Token Authentication for registered users for better tracking and security.
- Used validate_id utility for cleaner architecture and reusability.
- Made easy to follow errors throughtout the validation process
