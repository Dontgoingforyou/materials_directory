from rest_framework import serializers
from materials.models import Material, Category


class MaterialSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Material, используемый для представления и обработки данных материалов """

    class Meta:
        model = Material
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """ Сериализатор для модели Category, используемый для представления и обработки данных категорий """

    class Meta:
        model = Category
        fields = '__all__'