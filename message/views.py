from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from rest_framework import status
from . import serializers
# Create your views here.
class GetMessageAPIView(APIView):

    def get(self, request, formate=None):
        try:
            reciver_id = request.GET['reciver_id']
            print(reciver_id)
            messages = Messages.objects.filter(reciver__user_id=reciver_id)
            print(messages)
            serializer_data = serializers.GetMessageSerializer(messages, many=True)
            data = serializer_data.data

            return Response({'data': data}, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({'status': "Internal Server Error, we'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SendMessageAPIView(APIView):

        def post(self, request, format=None):
            try:
                serializer = serializers.SendMessageSerializer(data=request.data)
                print(serializer)
                if serializer.is_valid():
                    message = serializer.data.get('message')
                    sender_id = serializer.data.get('sender')
                    reciver_id = serializer.data.get('reciver')
                else:
                    return Response({'status': 'Bad Request.'}, status=status.HTTP_200_OK)
                user_sender = User.objects.get(id=sender_id)
                user_reciver = User.objects.get(id=reciver_id)
                sender = UserProfile.objects.get(user=user_sender)
                reciver = UserProfile.objects.get(user=user_reciver)

                messages = Messages()
                messages.message = message
                messages.sender = sender
                messages.reciver = reciver
                messages.save()

                return Response({'status': 'ok'}, status=status.HTTP_200_OK)

            except:
                return Response({'status': "Internal Server Error, well Check It Later"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateMessageAPIView(APIView):

    def post(self, request, format=None):
        try:
            serializer_update = serializers.UpdateMessageSerializer(data=request.data)
            if serializer_update.is_valid():
                message_id = serializer_update.data.get('message_id')
                message = serializer_update.data.get('message')
            else:
                return Response({'status': 'Bas Request.'}, status.HTTP_400_BAD_REQUEST)
            Messages.objects.filter(id=message_id).update(message=message)

            return Response({'status':'ok'}, status=status.HTTP_200_OK)

        except:
            return Response({'status': "Internal Server Error, We'll Check It Later"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteMessageAPIView(APIView):

    def post(self, request, format:None):
        try:
            serilizer_id = serializers.DeleteMessageSerializer(data=request.data)
            if serilizer_id.is_valid():
                message_id = serilizer_id.data.get('message_id')
            else: return Response({'status': 'Bad Request.'},
                                  status=status.HTTP_400_BAD_REQUEST)
            deleted = Messages.objects.filter(id=message_id).delete()
            
            return Response({'staus': "ok"},
                            status=status.HTTP_200_OK)


        except:
            return Response({'staus': "Internal Server Erroe,We'll Check It Later "},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
