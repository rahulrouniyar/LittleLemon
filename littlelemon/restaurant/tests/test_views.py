from django.test import TestCase

from django.test import Client

from restaurant.models import MenuItem

from restaurant.serializers import MenuItemSerializer
from django.urls import reverse


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menuItem1 = MenuItem.objects.create(
            title="IceCream", price=80, inventory=100
        )
        self.menyItem2 = MenuItem.objects.create(
            title="Coffee", price=20, inventory=150
        )

    def test_getall(self):
        response = self.client.get(reverse("menu-list"))
        serialized_item = MenuItemSerializer(
            [self.menuItem1, self.menyItem2], many=True
        ).data

        self.assertEqual(response.data, serialized_item)
