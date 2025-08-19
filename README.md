# Pageant Vision API

## Local Development Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the API:

For staging environment (with auto-reload):
```bash
APP_ENV=staging uvicorn main:app --reload
```

For production environment:
```bash
APP_ENV=prod uvicorn main:app
```

The API will be available at http://localhost:8000

API Documentation available at:
- http://localhost:8000/docs
- http://localhost:8000/redoc

## Environment Configuration

The API supports different environments through `.env` files:
- `.env.prod` - Production settings
- `.env.staging` - Staging settings with debug mode enabled

Environment variables can be overridden by setting them before running the application:
```bash
export APP_ENV=staging
export DEBUG=true
```