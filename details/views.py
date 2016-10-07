from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from .models import Messages
import json
from .forms import ContactMe

# Create your views here.
def aboutme(request):
	return render(request,'detail/aboutme.html',{})

def contactme(request):
	form = ContactMe()
	return render(request,'detail/contactme.html',{'form':form})


def sentmail(request):
	if request.method==	'POST':
		if request.is_ajax():
			form = ContactMe(request.POST)
			name=form['name'].value()
			email_id=form['email_id'].value()
			phone_no=form['phone_no'].value()
			message=form['message'].value()
			msg=Messages.objects.create(
				name=name,
				email_id=email_id,
				phone_no=phone_no,
				message=message,
				)
			msg.save()
			response_data={'status':'success','message':'message sent'}
		else:
			response_data={'status':'error','message':'not sent'}
	else:
		response_data={'status':'error','message':'not sent'}
	return HttpResponse(json.dumps(response_data),content_type="application/json")

