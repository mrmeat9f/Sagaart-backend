
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
            'address',
            'social_network',
            'avg_price'
            )
        )


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User.USERNAME_FIELD,
            'password',
        )

    def validate(self, obj):
        invalid_usernames = ['me', 'set_password',
                             'subscriptions', 'subscribe']
        if self.initial_data.get('username') in invalid_usernames:
            raise serializers.ValidationError(
                {'username': 'Вы не можете использовать этот username.'}
            )
        return obj


class SetPasswordSerializer(serializers.Serializer):
    """[POST] Изменение пароля пользователя."""
    current_password = serializers.CharField()
    new_password = serializers.CharField()

    def validate(self, obj):
        try:
            validate_password(obj['new_password'])
        except django_exceptions.ValidationError as e:
            raise serializers.ValidationError(
                {'new_password': list(e.messages)}
            )
        return super().validate(obj)

    def update(self, instance, validated_data):
        if not instance.check_password(validated_data['current_password']):
            raise serializers.ValidationError(
                {'current_password': 'Неправильный пароль.'}
            )
        if (validated_data['current_password']
           == validated_data['new_password']):
            raise serializers.ValidationError(
                {'new_password': 'Новый пароль должен отличаться от текущего.'}
            )
        instance.set_password(validated_data['new_password'])
        instance.save()
        return validated_data
