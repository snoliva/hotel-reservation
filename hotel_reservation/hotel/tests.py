from django.test import TestCase
from django.urls import reverse
from .models import Room
from .views import AddRoomView


class RoomModelTestCase(TestCase):
    def setUp(self):
        self.room = Room.objects.create(room_number='101', room_type='Individual')

    def test_room_creation(self):
        self.assertEqual(Room.objects.count(), 1)

    def test_room_str(self):
        self.assertEqual(str(self.room), '101 - Individual')


class AddRoomViewTestCase(TestCase):
    def test_add_room_view(self):
        response = self.client.get(reverse('hotel:add_room'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hotel/add_room.html')

    def test_add_room_success(self):
        response = self.client.post(reverse('hotel:add_room'), {'room_number': '102', 'room_type': 'Doble'})
        self.assertEqual(response.status_code, 302)  # 302: Redirect after successful form submission
        self.assertEqual(Room.objects.count(), 1)  # Make sure a room has been created

    def test_add_room_duplicate_number(self):
        Room.objects.create(room_number='102', room_type='Individual')
        response = self.client.post(reverse('hotel:add_room'), {'room_number': '102', 'room_type': 'Doble'})
        self.assertEqual(response.status_code, 200)  # Stay on the same page
        self.assertFormError(response, 'form', 'room_number', '¡Este número de habitación ya está registrado!')


# Agrega más pruebas según sea necesario para otras vistas y funcionalidades relacionadas con las habitaciones.
