from django.urls import path
from .views import task, send_email


urlpatterns = [
    path('task/', task),
    # path('send_email/', send_email)
]