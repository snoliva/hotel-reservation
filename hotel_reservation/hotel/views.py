from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, DeleteView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from .models import Room, Reservation
from .forms import ReservationForm

class IndexView(ListView):
    model = Room
    template_name = 'index.html'
    context_object_name = 'rooms'

class MakeReservationView(FormView):
    template_name = 'hotel/make_reservation.html'
    form_class = ReservationForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class AvailabilityView(FormView):
    template_name = 'hotel/availability.html'

    def get(self, request, *args, **kwargs):
        room_id = request.GET.get('room_id')
        check_in_date = request.GET.get('check_in_date')
        check_out_date = request.GET.get('check_out_date')
        if room_id and check_in_date and check_out_date:
            room = Room.objects.get(pk=room_id)
            available_dates = []
            for reservation in room.reservation_set.all():
                if reservation.check_in_date <= check_in_date and reservation.check_out_date >= check_out_date:
                    available_dates.append(reservation)
            return render(request, self.template_name, {'available_dates': available_dates})
        else:
            return render(request, self.template_name)

class AddRoomView(CreateView):
    model = Room
    fields = ['room_number', 'room_type']
    template_name = 'hotel/add_room.html'
    success_url = reverse_lazy('hotel:index')  # Ajusta 'index' al nombre de tu página principal

    def form_valid(self, form):
        room_number = form.cleaned_data['room_number']
        if Room.objects.filter(room_number=room_number).exists():
            form.add_error('room_number', '¡Este número de habitación ya está registrado!')
            return self.form_invalid(form)
        return super().form_valid(form)


class RoomDetailView(DetailView):
    model = Room
    template_name = 'hotel/room_detail.html'

class RoomUpdateView(UpdateView):
    model = Room
    fields = ['room_type']
    template_name = 'hotel/room_update.html'
    success_url = reverse_lazy('hotel:index')  # Ajusta 'index' al nombre de tu página principal

class RoomDeleteView(DeleteView):
    model = Room
    success_url = reverse_lazy('hotel:index')  # Ajusta 'index' al nombre de tu página principal