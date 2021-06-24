from rest_framework.serializers import (
	ModelSerializer,
)
from customer.models import Partner ,Post


class ListSerializer(ModelSerializer):
	class Meta:
		model =Partner
		fields = [
			'user',
			'LicenseKey',
			'RouterSerial',
			'active',
		]

class postSerializer(ModelSerializer):
	class Meta:
		model =Post
		fields = [
			'name',
			'text',
		]


class AddSerializer(ModelSerializer):
	class Meta:
		model = Partner
		fields = [
			'RouterSerial',
			# 'LicenseKey',
			# 'active',
			'Appversion',
			# 'license_type',
			# 'RouterDisabled',
			# 'Reload',
			# 'dateOfJoin',
			# 'last_login_date',
			# 'state',
			# 'Advertisement',
			# 'log',

		]
	def create(self, validated_data):
			RouterSerial = validated_data.get('RouterSerial')
			Appversion = validated_data.get('Appversion')
			return Partner.objects.create(RouterSerial=RouterSerial, Appversion=Appversion)

from rest_framework import generics

class ShowSerializer(ModelSerializer):
	class Meta:
		model = Partner
		fields = [
			'RouterSerial',
			'LicenseKey',
			'active',
			'Appversion',

			'license_type',
			'RouterDisabled',
			'Reload',
			'dateOfJoin',
			'last_login_date',
			'state',
			'Advertisement',
			'log',
		]
	def nassar(self):
		return self.RouterSerial

class DeleteSerializer(ModelSerializer):
	class Meta:
		model = Partner

from rest_framework import serializers
class userSerializer(ModelSerializer):
	class Meta:
		model=Partner
		fielde='__all__'

# class postSerializer(ModelSerializer):
# 	class Meta:
# 		model = Post
# 		fields = [
# 		  'name',
# 		  'text',
# 		  ]