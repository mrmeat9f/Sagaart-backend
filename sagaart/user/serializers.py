from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.RegexField(
        regex=r'^[\w.@+-]+\Z',
        required=True,
        max_length=150,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True,
        max_length=254,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'nick_name',
            'biograthy',
            'year_of_birth',
            'place_of_birth',
            'residence_city',
            'education', 
            'art_education', 
            'teaching_experience',
            'personal_style',
            'solo_shows', 
            'solo_shows_gallery',
            'group_shows', 
            'group_shows_gallery',
            'group_shows_artist',
            'collected_private',
            'collected_major',
            'winner',
            'social_network',
            'avg_price'
            )
