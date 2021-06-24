from django import forms


from django.contrib.auth.forms import UserCreationForm
# from customer.models import DriverUs

# class RegisterForm(UserCreationForm):
# 	class Meta:
# 		model = Pa
# 		fields = ('username', 'password1', 'password2')
from customer.models import Partner

from django.utils.translation import gettext as _
class PartnerForm(forms.ModelForm):

    class  Meta:
        model = Partner
        fields=('RouterSerial','Advertisement','phone','address','Appversion',)
        exclude=()
        labels = {
            'RouterSerial':_('السيريال حق الزبون'),
            'Advertisement':_('ضع اعلان للزبون'),
            'phone':_('رقم هاتف الزبون'),
            'address':_('عنوان الزبون'),
            'Appversion':_('اصدار برنامج الزبون'),

        }

class AddForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ('RouterSerial', 'Appversion',)
