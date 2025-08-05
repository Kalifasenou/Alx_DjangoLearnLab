#Step 4: Create Custom Serializers
from rest_framework import serializers
from .models import Author, Book
import datetime

# a BookSerializer that serializes all fields of the Book model.
class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all()
    )
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Validation : l’année ne peut pas être dans le futur
    def validate_publication_year(self, value):
        if value > datetime.date.today().year:
            raise serializers.ValidationError("L'année de publication ne peut pas être dans le futur.")
        return value


# an AuthorSerializer that includes
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name']


