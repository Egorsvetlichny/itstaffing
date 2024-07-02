# Тесты представлений.

from django.test import TestCase
import unittest
from unittest.mock import patch
from django.test import RequestFactory
from django.urls import reverse
from staff.views import HomePageView


class HomePageViewTest(TestCase):
    def setUp(self):
        """Создает тестовый клиент перед каждым тестом."""
        self.factory = RequestFactory()

    def test_view_url_exists_at_desired_location(self):
        """Test that the url exists at the desired location."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """Test that the url is accessible by name."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Test that the view uses the correct template."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'staff/index.html')

    def test_view_returns_correct_content(self):
        """Test that the view returns the correct content."""
        request = self.factory.get('/')
        response = HomePageView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Главная страница')
        self.assertContains(response, 'Содержимое главной страницы')

    def test_view_returns_404_for_nonexistent_url(self):
        """Test that the view returns a 404 for a nonexistent url."""
        response = self.client.get('/nonexistent-url/')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
