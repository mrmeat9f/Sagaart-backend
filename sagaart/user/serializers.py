from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import (SocialNets, Education, Subscribe,
                     ShoppingList, User, Catalog)


class SocialNetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNets
        fields = ['id', 'name_nets', 'account']


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'ed_type', 'ed_level', 'ed_name_institute']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['id']


class ShoppingListSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Catalog.objects.all())

    class Meta:
        model = ShoppingList
        fields = ['id', 'product']


class UserSerializer(serializers.ModelSerializer):
    social_nets = SocialNetsSerializer(many=True, read_only=True)
    education = EducationSerializer(many=True, read_only=True)
    nick_name = serializers.RegexField(
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
