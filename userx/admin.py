# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from userx.models import Extention

class ExtentionInline(admin.StackedInline):
    model = Extention
    can_delete = False
    classes = ('grp-collapse grp-open',)
    inline_classes = ('grp-collapse grp-open',)

class UserAdmin(UserAdmin):
	list_display = ('username', 'email', 'first_name', 'last_name','inn', 'account')
	inlines = (ExtentionInline, )
	def inn(self, obj):
		return obj.userdata.inn
	def account(self, obj):
		return obj.userdata.account
	inn.short_description = u'ИНН'
	account.short_description = u'Счёт'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)