# from django.contrib import admin
# from .models import Passenger, Ticket, Train

# @admin.register(Passenger)
# class PassengerAdmin(admin.ModelAdmin):
#     list_display = ('user',)  # Add additional fields if needed

# @admin.register(Ticket)
# class TicketAdmin(admin.ModelAdmin):
#     list_display = ('pnr', 'passenger', 'train', 'journey_date', 'source', 'destination', 'ticket_number', 'status', 'booking_date')

# @admin.register(Train)
# class TrainAdmin(admin.ModelAdmin):
#     list_display = ('train_number', 'train_name', 'source', 'destination', 'journey_date', 'seats_available')
from django.contrib import admin
from .models import Passenger, Train, Ticket

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('train_number', 'train_name', 'source', 'destination')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('pnr', 'passenger', 'train', 'ticket_number', 'status')

