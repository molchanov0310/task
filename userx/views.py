# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from models import *
import math

def home_page(request):
	users = User.objects.filter(is_staff=False)
	return render_to_response('index.html', {'users':users, }, RequestContext(request))

def ajax_transfer(request):
	if request.method == 'POST':
		import json
		result = {}
		result['status'] = 0

		try:
			summa = float(request.POST.get('sum',''))
		except ValueError, e:
			result['status'] = 1
			result['message'] = 'Неверно введена сумма!'
			return HttpResponse(json.dumps(result), content_type = "application/json")

		inn = request.POST.get('inn','')
		recipients = User.objects.filter(userdata__inn=inn)
		if  not recipients:
			result['status'] = 1
			result['message'] = 'Нет пользователей с данным ИНН!'
			return HttpResponse(json.dumps(result), content_type = "application/json")

		username = request.POST.get('username','')
		try:
			user = User.objects.get(username=username)
			user_money = float(user.userdata.account)
		except:
			result['status'] = 1
			result['message'] = 'Операция не была проведена! Попробуйте ещё раз.'
			return HttpResponse(json.dumps(result), content_type = "application/json")

		if user.userdata.inn == inn:
			result['status'] = 1
			result['message'] = 'Невозможно провести операцию! Введённый ИНН совпадает с ИНН пользователя.'
			return HttpResponse(json.dumps(result), content_type = "application/json")
		if user_money<summa:
			result['status'] = 1
			result['message'] = 'На счету недостаточно средств!'
			return HttpResponse(json.dumps(result), content_type = "application/json")

		rcount = 0
		for recipient in recipients:
			try:
				float(recipient.userdata.account)
				rcount += 1
			except:
				result['status'] = 1
				result['message'] = 'Операция не была проведена! Попробуйте ещё раз.'
				return HttpResponse(json.dumps(result), content_type = "application/json")

		send_money = summa / rcount 
		send_money = math.trunc(send_money*100)/100.0
		summa = rcount*send_money
		for recipient in recipients:
			rmoney = float(recipient.userdata.account) + send_money
			recipient.userdata.account = rmoney
			recipient.userdata.save()

		user.userdata.account = user_money - summa
		user.userdata.save()
		result['count'] = rcount
		result['send_money'] = send_money
		return HttpResponse(json.dumps(result), content_type = "application/json")
	else:
		return HttpResponseRedirect('/')