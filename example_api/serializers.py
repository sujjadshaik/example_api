from rest_framework import serializers
from . import models
class HelloSerailizers(serializers.Serializer):
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validate_data):
        user = models.UserProfile(
            email=validate_data['email'],
            name=validate_data['email']
        )
        user.set_password(validate_data['password'])
        user.save()
        return user
class ProfileFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfilesFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}



