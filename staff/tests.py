from django.test import TestCase, Client
import unittest


class HomePageViewTest(TestCase):
    # def setUp(self):
    #     """Создает тестовый клиент перед каждым тестом."""
    #     self.client = self.itstaffing.test_client()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
