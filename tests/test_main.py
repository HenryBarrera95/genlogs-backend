from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_health_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_carriers_nyc_dc():
    response = client.get(
        "/carriers", params={"from_city": "New York", "to_city": "Washington DC"}
    )
    assert response.status_code == 200
    carriers = response.json()["carriers"]
    assert carriers[0]["name"] == "Knight-Swift Transport Services"


def test_carriers_sf_la():
    response = client.get(
        "/carriers", params={"from_city": "San Francisco", "to_city": "Los Angeles"}
    )
    assert response.status_code == 200
    carriers = response.json()["carriers"]
    assert carriers[0]["name"] == "XPO Logistics"


def test_carriers_other():
    response = client.get(
        "/carriers", params={"from_city": "Bogota", "to_city": "Lima"}
    )
    assert response.status_code == 200
    carriers = response.json()["carriers"]
    assert carriers[0]["name"] == "UPS Inc."


def test_carriers_missing_params():
    response = client.get("/carriers")
    assert response.status_code == 400
    assert response.json()["detail"] == "from_city and to_city are required"
