from rest_framework import serializers
from posts.models import Comment, Group, Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description', 'id')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'post', 'created')
        read_only_fields = ('post',)
