from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class CustomSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        queryset = self.get_queryset()
        try:
            return queryset.get(**{self.slug_field: data})
        except ObjectDoesNotExist:
            return queryset.create(**{self.slug_field: data})
        except (TypeError, ValueError):
            self.fail('invalid')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('__all__')


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('id', 'pub_date', 'author')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('id', 'author', 'created')


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username', read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    validators = [
        UniqueTogetherValidator(
            queryset=Follow.objects.all(),
            fields=['user', 'following']
        )
    ]

    def validate_following(self, following):
        user = self.context['request'].user
        if user != following:
            return following
        raise serializers.ValidationError(
            'Нельзя подписываться на самого себя'
        )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        read_only_fields = ('id',)
