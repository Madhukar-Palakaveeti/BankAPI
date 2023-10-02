from rest_framework import serializers
from api.models import Banks, Branches, EasyView


class BankViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banks
        fields = ('id', 'name',)

class BankBranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EasyView
        fields = ('ifsc','bank_name','branch','address','city','district','state','bank_id')     
        
        
        