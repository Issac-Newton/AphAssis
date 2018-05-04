# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#from urllib import request 
#from urllib import response
import json
import random
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from upload.models import Ques, guide
from django.http import HttpResponse, JsonResponse
# Create your views here.

number = int(0)
questions = list(Ques.objects.all())
length = len(questions)
question = questions[number]

def show(request):
	return render(request,'show/showImg.html')


def index(request):
	return render(request,'show/index.html')

@csrf_exempt
def get_next(request):
	global number	
	global questions
	global length
	global question
		
	if number < length:
		question = questions[number]	
	ques = str(question.question)
	imageA = str(question.imageA)
	DesA = str(question.DesA)
	imageB = str(question.imageB)
	DesB = str(question.DesB)
	imageC = str(question.imageC)
	DesC = str(question.DesC)
	imageD = str(question.imageD)
	DesD = str(question.DesD)
	voice = str(question.voice)
	if number < length:
		number += 1
	else:
		ques = ""
	return JsonResponse({"namee":ques,
						 "imageA":imageA,
						 "DesA":DesA,
						 "imageB":imageB,
						 "DesB":DesB,
						 "imageC":imageC,
						 "DesC":DesC,
						 "imageD":imageD,
						 "DesD":DesD,
						 "voice":voice
							})


@csrf_exempt
def error_answer(request):
	right = request.POST.get('right',None)
	wrong = request.POST.get('wrong',None)	
	Guider = list(guide.objects.filter(right_answer=right,wrong_answer=wrong))
	
	if len(Guider) > 0:
		tip = random.sample(Guider,1)
		result = tip[0].tips
		return JsonResponse({"guide":result})
	else:
		tip = ""
		return JsonResponse({"guide":tip})
	

