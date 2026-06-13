from tests.conftest import SAMPLE_DATA


class TestListResources:
    def test_returns_200(self, client):
        response = client.get("/api/v1/resources/")
        assert response.status_code == 200

    def test_returns_all_records(self, client):
        response = client.get("/api/v1/resources/")
        data = response.json()
        assert len(data) == len(SAMPLE_DATA)

    def test_resource_has_required_fields(self, client):
        response = client.get("/api/v1/resources/")
        resource = response.json()[0]
        assert "title" in resource
        assert "type" in resource
        assert "category" in resource
        assert "notes" in resource
        assert "link" in resource

    def test_returns_correct_titles(self, client):
        response = client.get("/api/v1/resources/")
        titles = {r["title"] for r in response.json()}
        expected = {row["title"] for row in SAMPLE_DATA}
        assert titles == expected


class TestRandomByCategory:
    def test_returns_200(self, client):
        response = client.get("/api/v1/resources/random")
        assert response.status_code == 200

    def test_returns_one_per_category(self, client):
        response = client.get("/api/v1/resources/random")
        data = response.json()
        categories = [item["category"] for item in data]
        # No duplicates — one result per category
        assert len(categories) == len(set(categories))

    def test_covers_all_categories(self, client):
        response = client.get("/api/v1/resources/random")
        returned_categories = {item["category"] for item in response.json()}
        expected_categories = {row["category"] for row in SAMPLE_DATA}
        assert returned_categories == expected_categories

    def test_each_item_has_resource(self, client):
        response = client.get("/api/v1/resources/random")
        for item in response.json():
            assert "category" in item
            assert "resource" in item
            resource = item["resource"]
            assert "title" in resource
            assert "category" in resource

    def test_resource_belongs_to_category(self, client):
        response = client.get("/api/v1/resources/random")
        for item in response.json():
            assert item["resource"]["category"] == item["category"]


class TestHealthCheck:
    def test_health_returns_ok(self, client):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
