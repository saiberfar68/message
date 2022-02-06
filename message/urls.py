from django.conf.urls import url
from . import views
from rest_framework.views import APIView

urlpatterns = [
    url('get_message', views.GetMessageAPIView.as_view(), name='get_message'),
    url('send_message', views.SendMessageAPIView.as_view(), name='send_message'),
    url('update_message', views.UpdateMessageAPIView.as_view(), name='update_message'),
    url('delete_message', views.DeleteMessageAPIView.as_view(), name='delete_message'),

]