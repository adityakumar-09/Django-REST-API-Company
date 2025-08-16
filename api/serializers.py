''' serializers.py in the Django REST Framework (DRF) is to convert complex data types, like Django model instances and querysets, 
into native Python data types that can be easily rendered into JSON, XML, or other content types. '''

from rest_framework import serializers
from api.models import Company

#create serualizer here
class CompanySerializer(serializers.HyperlinkedModelSerializer): #defines a serializer in the Django REST Framework (DRF) named CompanySerializer
    company_id=serializers.ReadOnlyField()
    class Meta: # This is an inner class used to configure the serializer. It's a standard Django pattern for providing metadata about a class.
        model=Company #This line tells the serializer which Django model it should be associated with. In this case, it's the Company model. The serializer will automatically inspect this model to determine the fields it needs to serialize and deserialize.
        fields="__all__" #This is a shortcut to include every field from the Company model in the serializer. The serializer will automatically generate corresponding fields for all of the model's fields, including any relationships.

