from django.test import Client, TestCase
from django.urls import reverse
from .models import Owner, Car


class CarsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.owner = Owner.objects.create(name='John Doe', has_cars=False)
        self.car = Car.objects.create(color='yellow', model='hatch', owner=self.owner)

    def test_owner_list(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('owner_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.owner.name)

    def test_owner_create(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('owner_create'))
        self.assertEqual(response.status_code, 200)

        data = {'name': 'Jane Doe'}
        response = self.client.post(reverse('owner_create'), data)
        self.assertRedirects(response, reverse('owner_list'))
        self.assertTrue(Owner.objects.filter(name='Jane Doe').exists())

    def test_owner_edit(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('owner_edit', args=[self.owner.id]))
        self.assertEqual(response.status_code, 200)

        data = {'name': 'John Doe Updated'}
        response = self.client.post(reverse('owner_edit', args=[self.owner.id]), data)
        self.assertRedirects(response, reverse('owner_list'))
        self.owner.refresh_from_db()
        self.assertEqual(self.owner.name, 'John Doe Updated')

    def test_owner_delete(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('owner_delete', args=[self.owner.id]))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('owner_delete', args=[self.owner.id]))
        self.assertRedirects(response, reverse('owner_list'))
        self.assertFalse(Owner.objects.filter(id=self.owner.id).exists())

    def test_car_list(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('car_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.car.color)
        self.assertContains(response, self.car.model)
        self.assertContains(response, self.owner.name)

    def test_car_create(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('car_create'))
        self.assertEqual(response.status_code, 200)

        data = {
            'color': 'blue',
            'model': 'sedan',
            'owner': self.owner.id
        }
        response = self.client.post(reverse('car_create'), data)
        self.assertRedirects(response, reverse('car_list'))
        self.assertTrue(Car.objects.filter(color='blue', model='sedan', owner=self.owner).exists())

    def test_car_edit(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('car_edit', args=[self.car.id]))
        self.assertEqual(response.status_code, 200)

        data = {
            'color': 'gray',
            'model': 'convertible',
            'owner': self.owner.id
        }
        response = self.client.post(reverse('car_edit', args=[self.car.id]), data)
        self.assertRedirects(response, reverse('car_list'))
        self.car.refresh_from_db()
        self.assertEqual(self.car.color, 'gray')
        self.assertEqual(self.car.model, 'convertible')

    def test_car_delete(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('car_delete', args=[self.car.id]))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('car_delete', args=[self.car.id]))
        self.assertRedirects(response, reverse('car_list'))
        self.assertFalse(Car.objects.filter(id=self.car.id).exists())

    def test_car_create(self):
    self.client.login(username='testuser', password='testpass')
    response = self.client.get(reverse('car_create'))
    self.assertEqual(response.status_code, 200)

    data = {
        'color': 'blue',
        'model': 'sedan',
        'owner': self.owner.id
    }
    response = self.client.post(reverse('car_create'), data)
    self.assertRedirects(response, reverse('car_list'))
    self.assertTrue(Car.objects.filter(color='azul', model='sedan', owner=self.owner).exists())

def test_car_edit(self):
    self.client.login(username='testuser', password='testpass')
    response = self.client.get(reverse('car_edit', args=[self.car.id]))
    self.assertEqual(response.status_code, 200)

    data = {
        'color': 'gray',
        'model': 'convertible',
        'owner': self.owner.id
    }
    response = self.client.post(reverse('car_edit', args=[self.car.id]), data)
    self.assertRedirects(response, reverse('car_list'))
    self.car.refresh_from_db()
    self.assertEqual(self.car.color, 'gray')
    self.assertEqual(self.car.model, 'convertible')

def test_car_delete(self):
    self.client.login(username='testuser', password='testpass')
    response = self.client.get(reverse('car_delete', args=[self.car.id]))
    self.assertEqual(response.status_code, 200)

    response = self.client.post(reverse('car_delete', args=[self.car.id]))
    self.assertRedirects(response, reverse('car_list'))
    self.assertFalse(Car.objects.filter(id=self.car.id).exists())