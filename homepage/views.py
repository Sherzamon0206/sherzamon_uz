import mimetypes
import os.path
from django.http import  HttpResponse,Http404
from django.conf import settings

from django.shortcuts import render
from .models import Developer,My_work,About,File
import json
from django.http import JsonResponse, HttpResponse


def Home(request):
	developer = Developer.objects.first()
	my_work=My_work.objects.all()
	about=About.objects.first()

	context={
		'developer':developer,
		'my_work':my_work,
		'about':about,
		'file':File.objects.last()

	}
	return render(request, 'index.html', context)


# def download_file(request):
# 	print("Salom")
# 	if request.method == 'POST':
# 		data = json.loads(request.body)
# 		print(data)
# 		fl_path ="About.resume"
# 		filename="resume.pdf"
# 		fl=open(fl_path,"r")
# 		mime_type, _ = mimetypes.guess_type(fl_path)
# 		response = HttpResponse(fl, content_type=mime_type)
# 		response['Content-Disposition'] = "attachment; filename=%s" % filename
#
#
#
#
#
# 		return JsonResponse({'data': response})
#


def download(request,path):
	file_path=os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path,"rb") as fh:
			response=HttpResponse(fh.read(),content_type="application/resume")
			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
			return  response


