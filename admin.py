from dataclasses import field
import datetime
from django.contrib import admin

from .forms import PartnerForm
from .models import Partner,Post,Advertisement
# Register your models here.


admin.site.register(Post)

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    save_on_top = True

from django.utils.html import format_html

from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'state', 'license_type', 'RouterSerial', 'dateOfJoin', 'Advertisement', 'Appversion', 'last_login_date', 'count', 'active')
    readonly_fields = ('dateOfJoin', 'done_date', 'last_login_date', 'log',)
    save_on_top = True
    search_fields = ('RouterSerial', 'dateOfJoin', 'Advertisement__text', 'Appversion', 'last_login_date',)
    list_filter = ('user', 'state', 'license_type', 'Appversion')
    sortable_by = ('user', 'dateOfJoin', 'state', 'license_type', 'RouterSerial', 'dateOfJoin', 'Advertisement', 'last_login_date', 'log', 'active','Appversion')
    actions = ('set_user_active', 'set_user_dis_active',)
    list_display_links = ('user', 'state', 'license_type', 'dateOfJoin', 'Advertisement', 'Appversion', 'last_login_date', 'count',)
    exclude = ('user',)
    # form = PartnerForm
    list_per_page = 15
    def count(self,obj):
        if obj.log:
            color_code = '447e9b'
        else:
            color_code = 'FF0000'
        html = '<span style="color: #{}">{} </span>'.format(color_code, obj.log)
        return format_html(html)

    def RouterSerialFun(self,obj):
        if obj.RouterSerial:
            color_code = '4E7e9b'
        else:
            color_code = 'FF0000'
        html = '<span style="color: #{}">{} </span>'.format(color_code, obj.RouterSerial)
        return format_html(html)

    def get_queryset(self, request):
        qs = super(PartnerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        # if request.user.username != request.user:
        album_ct = ContentType.objects.get_for_model(Partner)
        log_entries = LogEntry.objects.filter(
            content_type=album_ct,
            user=request.user,
            action_flag=ADDITION
        )
        user_album_ids = [a.object_id for a in log_entries]
        print(user_album_ids)
        if qs.filter(LicenseKey=None):
            return qs.filter(user=None)|qs.filter(user=request.user) # as qs.filter(user=None)&&qs.filter(user=request.user)
        return qs.filter(user=request.user)

    def get_readonly_fields(self,request,obj = None):
        if obj and obj.pk:
            return ('RouterSerial','active','dateOfJoin', 'done_date', 'last_login_date', 'log','Reload')
        return super().get_readonly_fields(request,obj)

    def set_user_active(self, request, queryset):
        count = queryset.update(active=True)
        self.message_user(request, '{} USER have been actived successfuly .'.format(count))
    set_user_active.short_description = 'Mark Selected is Active App '
    def set_user_dis_active(self, request, queryset):
        count = queryset.update(active=False)
        self.message_user(request, '{} USER have been disactived successfuly .'.format(count))
    set_user_dis_active.short_description = 'Mark Selected is DeActive App '

    def save_model(self,request,obj,form,change):
        if 'LicenseKey' in form.changed_data:
            # print(request.user + " change LicenseKey " +str(obj.RouterSerial))
            obj.user=request.user
            if(obj.LicenseKey):
                obj.done_date= datetime.date.today()
                obj.Reload=False
                obj.license_type='licensed'
                obj.state='active'
            if not obj.LicenseKey:
                obj.Reload=True
                obj.license_type='trial'
                obj.state = 'close'
                obj.user=None
        super().save_model(request, obj, form, change)
    # def export
    #     if request.method == 'GET':
