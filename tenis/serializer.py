from rest_framework import serializers
from .models import Brand, Shoe
from django.conf import settings

class ShoeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required=False)
    class Meta:
        model = Shoe
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        shoe = super().create(validated_data)
        if image:
            shoe.image_url = self.save_image(shoe, image)
            shoe.save()
        return shoe

    def save_image(self, shoe, image):
        from django.core.files.storage import default_storage 
        from django.core.files.base import ContentFile
        import os

        path = default_storage.save(os.path.join('images', str(shoe.id) + '_' + image.
        name), ContentFile(image.read())) 
        return settings.MEDIA_URL + path

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'