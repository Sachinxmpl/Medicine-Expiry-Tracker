# Medicine Expiry Tracker

A simple FastAPI application to track medicine expiry dates and notify users when medicines are nearing expiration.

## Features

- Add, view, and delete medicines with name, expiry date, and quantity.
- Automatic expiry checks (within 30 days, logged to console).
- PostgreSQL database for storage (via Docker Compose).
- Dockerized for easy deployment.

## Prerequisites

- Python 3.10+
- Docker and Docker Compose
- Git

## Setup Instructions

### Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/medicine-tracker.git
   cd medicine-tracker
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env`:

   ```bash
   cp .env.example .env
   ```

5. Run the application:

   ```bash
   uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
   ```

6. Access the API at `http://localhost:8000/docs`.

### Docker Setup

1. Build and run the Docker container:

   ```bash
   docker build -t medicine-tracker .
   docker run -p 8000:8000 --env-file .env medicine-tracker
   ```

2. Access the API at `http://localhost:8000/docs`.

### Docker Compose Setup

1. Ensure `.env` exists (copy from `.env.example` if needed):

   ```bash
   cp .env.example .env
   ```

2. Start the services:

   ```bash
   docker-compose up -d
   ```

3. Access the API at `http://localhost:8000/docs`.

4. Stop the services:

   ```bash
   docker-compose down
   ```

   To reset the database, include volumes:

   ```bash
   docker-compose down -v
   ```

## Running Tests

```bash
pytest tests/
```

## API Endpoints

- `POST /medicines/`: Add a new medicine.
- `GET /medicines/`: List all medicines (checks for expiring medicines).
- `GET /medicines/{id}`: Get a specific medicine.
- `DELETE /medicines/{id}`: Delete a medicine.

## Configuration

- `DATABASE_URL`: PostgreSQL database URL (default: `postgresql://user:password@postgres:5432/medicine_db`).
- `NOTIFICATION_DAYS`: Days before expiry to trigger notifications (default: 30).

## Development

- **Pre-commit hooks**: Run `pre-commit install` to enable linting and formatting.
- **Git branching**:
  - `main`: Stable branch.
  - `feature/*`: New features.
  - `bugfix/*`: Bug fixes.



## .
- The expiry notification is currently logged to the console for simplicity.
- PostgreSQL is used via Docker Compose for persistent storage.