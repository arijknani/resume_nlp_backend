from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ResumeForm
from .models import Resume
import spacy

nlp = spacy.load('en_core_web_sm')

def index(request):
    return render(request, 'index.html')

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            return redirect('resume_data', resume_id=resume.id)
    else:
        form = ResumeForm()
    return render(request, 'upload.html', {'form': form})

def process_resume(request):
    if request.method == 'GET' and request.is_ajax():
        resume_id = request.GET.get('resume_id', None)
        if resume_id:
            resume = Resume.objects.get(id=resume_id)
            doc = nlp(resume.resume_text)
            data = {
                'name': None,
                'email': None,
                'phone': None,
            }
            for ent in doc.ents:
                if ent.label_ == 'PERSON':
                    data['name'] = ent.text
                elif ent.label_ == 'EMAIL':
                    data['email'] = ent.text
                elif ent.label_ == 'PHONE':
                    data['phone'] = ent.text
            resume.name = data['name']
            resume.email = data['email']
            resume.phone = data['phone']
            resume.save()
            return JsonResponse(data)
    return HttpResponseBadRequest()

def get_resume_data(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    return render(request, 'resume.html', {'resume': resume})
