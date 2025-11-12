import unittest
import json
from app import app


class TestKCLAPI(unittest.TestCase):

    def setUp(self):
        # configure test client
        app.testing = True
        self.client = app.test_client()

    def test_health_endpoint(self):
        """Health check should return 200 OK"""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b"OK", resp.data)

    def test_index_json(self):
        """Root endpoint should return JSON with service info"""
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertIn("service", data)
        self.assertIn("status", data)
        self.assertEqual(data["service"], "kcl-api-project")

    def test_echo(self):
        """Echo endpoint should return same JSON payload"""
        payload = {"test": "hello"}
        resp = self.client.post("/echo", json=payload)
        self.assertEqual(resp.status_code, 200)
        data = json.loads(resp.data)
        self.assertEqual(data.get("echo"), payload)

    def test_unknown_route(self):
        """Unknown routes should return 404"""
        resp = self.client.get("/doesnotexist")
        self.assertEqual(resp.status_code, 404)

    # Example of a skipped test — typical in dev
    @unittest.skip("integration test for /auth not implemented yet")
    def test_auth_token(self):
        """Placeholder for future auth test"""
        pass


if __name__ == "__main__":
    unittest.main()
