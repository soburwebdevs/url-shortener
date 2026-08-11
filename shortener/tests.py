from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .models import Link


User = get_user_model()

class LinkTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="TestPass@123")
        self.other_user = User.objects.create_user(username="otheruser", password="TestPass@123")
        
        self.token, _ = Token.objects.get_or_create(user=self.user)
        
        self.link = Link.objects.create(
            original_url="https://example.com",
            created_by=self.user
        )
        
    def test_create_link_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        data = {"original_url": "https://netflix.com"}
        response = self.client.post(reverse('link-list'), data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["created_by"], self.user.id)
        
    def test_create_link_anonymous(self):
        data = {"original_url": "https://example.com"}
        response = self.client.post(reverse('link-list'), data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNone(response.data["created_by"])
        
    def test_link_lists_scoped_to_user(self):
        # Create a link belonging to other_user
        Link.objects.create(original_url="https://otheruser-link.com", created_by=self.other_user)
        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get(reverse('link-list'))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Only self.link (created in setUp, belongs to self.user) should be visible
        self.assertEqual(len(response.data), 1)
        
        self.assertEqual(response.data[0]['id'], self.link.id)
        
    def test_redirect_increments_click_count(self):
        self.assertEqual(self.link.click_count, 0)

        url = f'/{self.link.short_code}/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.url, self.link.original_url)

        self.link.refresh_from_db()
        self.assertEqual(self.link.click_count, 1)
        
    def test_redirect_nonexistent_code(self):
        url = f'/agasgj/'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        


