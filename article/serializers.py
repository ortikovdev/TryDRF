from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Article
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Article
        # fields = ['id', 'author', 'title', 'image', 'content', 'created_date']
        fields = '__all__'

    def validate(self, attrs):
        print(attrs)
        title = attrs.get('title')
        content = attrs.get('content')
        exps = {}
        if not title[0].isupper():
            exps['title'] = []
            exps['title'].append('Title must start with uppercase')
        if not content[0].isupper():
            exps['content'] = 'Content must be uppercase'
        if self.Meta.model.objects.filter(title=title).exists():
            exps['title'] = []
            exps['title'].append(["Title already exists"])
        if exps:
            raise ValidationError(exps)
        return attrs

    def create(self, validated_data):
        user_id = self.context.get('user_id')
        print(validated_data)
        validated_data['author_id'] = user_id
        print(validated_data)
        return super().create(validated_data)


class ArticlePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        # fields = ['id', 'author', 'title', 'image', 'content', 'created_date']
        fields = '__all__'
