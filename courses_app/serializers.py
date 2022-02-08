from rest_framework import serializers
from rest_framework.utils import field_mapping

from courses_app import models



class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'name','email', 'password') # NOTE show fields 
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    # NOTE override django create for this serializer
    def create(self, validated_data):
        """create and return user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
        )

        return user



class CourseSerializer(serializers.ModelSerializer):
    """Serialize Course object"""

    class Meta:
        model = models.Course
        fields = ('id', 'name','details','language','price','category_id','updated_at','created_at') # NOTE show fields 

class CategorySerializer(serializers.ModelSerializer):
    """Serialize Category object"""

    class Meta:
        model = models.Category
        fields = ('id', 'name') # NOTE show fields 


class ArticleSerializer(serializers.ModelSerializer):
    """Serialize Article object"""

    class Meta:
        model = models.Article
        fields = ('id', 'title', 'body') # NOTE show fields 

class PartnerSerializer(serializers.ModelSerializer):
    """Serialize Partner object"""

    class Meta:
        model = models.Partner
        fields = ('id', 'name', 'logo') # NOTE show fields 



# class ProfileFeedItemSerializer(serializers.ModelSerializer):
#     """Serialize ProfileFeedItems"""


#     class Meta:
#         model = models.ProfileFeedItem
#         fields = ('id','user_profile','status_text','created_on')
#         # id and created_on are read-only by default
#         # we make user_profile read only because we will use it for auth

#         extra_kwargs = {
#             'user_profile': {
#                 'read_only': True
#             }
#         }
        
