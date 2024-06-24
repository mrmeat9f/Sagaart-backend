from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from .models import User


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'nick_name',
            'phone',
            'icon',
            'gender',
            'biography',
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
