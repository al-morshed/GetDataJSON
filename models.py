from django.db import models
from django.contrib.auth.models import User
from .models import *
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext as _


# Create your models here.
class License_Type(models.Model):
    type = models.CharField(verbose_name=_('Type Name'), max_length=50, null='True')

    class Meta:
        verbose_name = _('Type')
        verbose_name_plural = _('Types')

    def __str__(self):
        return self.type


class Partner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    RouterSerial = models.CharField(verbose_name=_('Router Serial Number'), max_length=50, primary_key=True,
                                    unique=True)
    LicenseKey = models.CharField(verbose_name=_('License kay '), max_length=50, null=True, blank=True)
    # Appversion = models.IntegerField(verbose_name=_('Program Version'), null='True')
    Appversion = models.DecimalField(verbose_name=_('Program Version'), max_digits=20, decimal_places=2)
    phone = models.CharField(verbose_name=_('phone'), max_length=50, null='True', blank=True,
                             # unique=True
                             )
    address = models.CharField(verbose_name=_('Address'), max_length=50, null='True', blank=True)
    license_type = models.CharField(max_length=50, verbose_name=_('Type of license'),
                                    choices=(
                                        ('trial', 'Trial'),
                                        ('free', 'Free'),
                                        ('licensed', 'Licensed'),
                                    ),
                                    default='trial')
    RouterDisabled = models.BooleanField(default=False, verbose_name="تعطيل هذه النسخة حتى لو كانت مرخصة")
    Reload = models.BooleanField(default=True, verbose_name=_('Reload info from server'),
                                 help_text='اذا تم سحب الرخصة لابد للبرنامج اعادة حفظ البيانات')
    active = models.BooleanField(default=True)
    dateOfJoin = models.DateTimeField(default=timezone.now, verbose_name=_('Date Join'))
    done_date = models.DateTimeField(verbose_name=_('Date Of Accepted License'), blank=True, null=True)
    last_login_date = models.DateTimeField(verbose_name=_('Date Of Last Login'), blank=True, null=True)
    state = models.CharField(max_length=50, verbose_name=_('Status'),
                             choices=(
                                 ('pending', 'pending'),
                                 ('active', 'activate'),
                                 ('deactive', 'deactivate'),
                                 ('close', 'Closed'),
                             ),
                             default=("pending"))
    Advertisement = models.ForeignKey('customer.Advertisement', on_delete=models.CASCADE,
                                      related_name=_('Advertisement'), null=True, blank=True)
    log = models.IntegerField(verbose_name=_('Log or Session connection Count Number'), null='True', blank=True)
    OpenMainCount = models.IntegerField(verbose_name=_('Main Menu Count Number'), null='True', blank=True)
    OpenNeighborCount = models.IntegerField(verbose_name=_('Neighbor Count Number'), null='True', blank=True)
    OpenActiveCount = models.IntegerField(verbose_name=_('Active Count Number'), null='True', blank=True)
    OpenHostCount = models.IntegerField(verbose_name=_('Host Count Number'), null='True', blank=True)
    OpenAddUserCount = models.IntegerField(verbose_name=_('Add User Activity Count Number'), null='True', blank=True)
    OpenAddUsersCount = models.IntegerField(verbose_name=_('Add Users Activity Count Number'), null='True', blank=True)
    OpenUsermanCount = models.IntegerField(verbose_name=_('Open Userman Activity Count Number'), null='True',
                                           blank=True)
    OpenHotspotCount = models.IntegerField(verbose_name=_('Open HotSpot Activity Count Number'), null='True',
                                           blank=True)

    Max_Neighbor_date = models.DateTimeField(verbose_name=_('Date Of Maximum Neighbor'), blank=True, null=True)
    last_pdf_date = models.DateTimeField(verbose_name=_('Date Of Last Print pdf'), blank=True, null=True)
    OpenActiveMax = models.IntegerField(verbose_name=_('Active Maximum Number'), null='True', blank=True)
    OpenNeighborPast = models.IntegerField(verbose_name=_('Neighbor Count Number Past'), null='True', blank=True)

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    def __str__(self):
        return self.RouterSerial

    def Advertisements(self):
        return self.Advertisement.text


class Post(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.name


from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# class DriverUs(AbstractUser):
#     name = models.CharField(max_length=250, default='Name')
#     def __str__(self):
#         return self.username
