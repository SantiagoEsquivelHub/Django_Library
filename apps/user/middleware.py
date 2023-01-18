import datetime
from datetime import timedelta
from apps.author.models import *


class ReservationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print("request: ", request)
        response = self.get_response(request)
        # print("response: ", response)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated:
            # print("logged")
            current_date = datetime.date.today()
            
            reservations = Reservation.objects.filter(state = True, user = request.user)

            for reservation in reservations:
                expiration_date = reservation.creation_date + timedelta(days = 7)
                # print("current_date: ", current_date)
                # print("expiration_date: ", expiration_date)
                
                if current_date > expiration_date:
                    reservation.state = False
                    reservation.save()
