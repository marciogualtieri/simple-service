from sqlmodel import select, exists

from api import models


def test_create_user(client, db_session):
    response = client.post("/users", json={"email": "test@test.com", "password": "12345"})
    assert response.status_code == 201

    user = response.json()
    assert user == {"email": "test@test.com", "id": 1}

    with db_session() as session:
        assert session.exec(select(models.User).where(models.User.id == user["id"])).first() is not None


def test_get_user(client, db_session):
    with db_session() as session:
        
        test_user = models.User(email="test@test.com", hashed_password="12345")
        session.add(test_user)
        session.commit()

        response = client.get(f"/users/{test_user.id}")
        assert response.status_code == 200

        session.refresh(test_user)

        expected_user = {"email": "test@test.com", "id": test_user.id}

        assert response.json() == expected_user
