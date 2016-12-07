# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Extention( models.Model):
	user = models.OneToOneField(User, related_name='userdata')
	inn = models.CharField(u'ИНН',  max_length = 255)
	account = models.DecimalField(u'Счёт', default=0.00, decimal_places = 2, max_digits=32, help_text = u'руб.')
	def __unicode__(self):
		return self.user.username
	class Meta:
		verbose_name = u''
		verbose_name_plural = u'данные пользователя'

