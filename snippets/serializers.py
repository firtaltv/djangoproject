from rest_framework import serializers
from .models import Snippets, LANGUAGE_CHOICES, STYLE_CHOICES
from users.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet_highlight', format='html')

    class Meta:
        model = Snippets
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'code', 'lineos', 'language', 'style', 'created']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='snippet_detail',
        read_only=True
    )

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
