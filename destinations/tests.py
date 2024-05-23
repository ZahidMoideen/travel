from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Destination

class DestinationModelTest(TestCase):
    def setUp(self):
        Destination.objects.create(
            name='Test Destination',
            country='Test Country',
            description='Test Description',
            best_time_to_visit='Test Time',
            category='Beach',
            image_url='https://example.com/test.jpg'
        )

    def test_destination_fields(self):
        destination = Destination.objects.get(name='Test Destination')
        self.assertEqual(destination.country, 'Test Country')
        self.assertEqual(destination.description, 'Test Description')
        self.assertEqual(destination.best_time_to_visit, 'Test Time')
        self.assertEqual(destination.category, 'Beach')
        self.assertEqual(destination.image_url, 'https://example.com/test.jpg')

class DestinationAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.destination_data = {
            'name': 'Test Destination',
            'country': 'Test Country',
            'description': 'Test Description',
            'best_time_to_visit': 'Test Time',
            'category': 'Beach',
            'image_url': 'https://example.com/test.jpg'
        }

    def test_create_destination(self):
        response = self.client.post('/destinations/', self.destination_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_destination_list(self):
        response = self.client.get('/destinations/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_destination_detail(self):
        destination = Destination.objects.create(**self.destination_data)
        response = self.client.get(f'/destinations/{destination.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_destination(self):
        destination = Destination.objects.create(**self.destination_data)
        updated_data = {
            'name': 'Updated Test Destination',
            'country': 'Updated Test Country',
            'description': 'Updated Test Description',
            'best_time_to_visit': 'Updated Test Time',
            'category': 'City',
            'image_url': 'https://example.com/updated_test.jpg'
        }
        response = self.client.put(f'/destinations/{destination.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_destination(self):
        destination = Destination.objects.create(**self.destination_data)
        response = self.client.delete(f'/destinations/{destination.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
