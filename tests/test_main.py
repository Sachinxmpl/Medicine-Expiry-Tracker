import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.database import Base, get_db
import os

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql://test_user:test_password@postgres_test:5432/test_medicine_db")

test_engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="function")
def test_client():
    Base.metadata.create_all(bind=test_engine)
    client = TestClient(app)
    yield client
    Base.metadata.drop_all(bind=test_engine)

@pytest.mark.asyncio
async def test_create_medicine(test_client):
    response = test_client.post(
        "/medicines/",
        json={"name": "Paracetamol", "expiry_date": "2025-12-31", "quantity": 10}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Paracetamol"
    assert data["quantity"] == 10

@pytest.mark.asyncio
async def test_read_medicines_expiry_check(test_client):
    test_client.post(
        "/medicines/",
        json={"name": "Aspirin", "expiry_date": "2025-05-20", "quantity": 5}
    )
    response = test_client.get("/medicines/")
    assert response.status_code == 200
    medicines = response.json()
    assert len(medicines) == 1
    assert medicines[0]["name"] == "Aspirin"