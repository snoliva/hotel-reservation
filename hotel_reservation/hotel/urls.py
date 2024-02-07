from django.urls import path
from .views import MakeReservationView, AvailabilityView, AddRoomView, IndexView, RoomDeleteView, RoomUpdateView, RoomDetailView

app_name = 'hotel'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('make_reservation/', MakeReservationView.as_view(), name='make_reservation'),
    path('availability/', AvailabilityView.as_view(), name='availability'),
    path('add_room/', AddRoomView.as_view(), name='add_room'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('room/<int:pk>/update/', RoomUpdateView.as_view(), name='room_update'),
    path('room/<int:pk>/delete/', RoomDeleteView.as_view(), name='room_delete'),
]
