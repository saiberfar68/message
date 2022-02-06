from rest_framework import serializers

class SendMessageSerializer(serializers.Serializer):
    message = serializers.CharField(required=True, allow_null=False, max_length=256)
    sender = serializers.IntegerField(required=True, allow_null=False)
    reciver = serializers.IntegerField(required=True, allow_null=False)

class GetMessageSerializer(serializers.Serializer):
    message = serializers.CharField(required=True, allow_null=False, max_length=256)
    create_at = serializers.DateTimeField(required=True, allow_null=False)
    sender = serializers.IntegerField(required=True, allow_null=False)
    reciver = serializers.IntegerField(required=True, allow_null=False)

class UpdateMessageSerializer(serializers.Serializer):
    message_id = serializers.IntegerField(required=True, allow_null=False)
    message = serializers.CharField(required=True, allow_null=False, max_length=256)

class DeleteMessageSerializer(serializers.Serializer):
    message_id = serializers.IntegerField(required=True, allow_null=False)