import spacy
from django.shortcuts import render, redirect
from .forms import ResumeUploadForm
from .models import Resume

def extract_resume_data(resume_file):
    # Load the English language model
    nlp = spacy.load('en_core_web_sm')

    # Parse the resume text using spaCy
    doc = nlp(resume_file)

    # Extract the name, email, phone number, education, and experience from the resume
    name = None
    email = None
    phone_number = None
    education = None
    experience = None
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            name = ent.text
        elif ent.label_ == 'EMAIL':
            email = ent.text
        elif ent.label_ == 'PHONE':
            phone_number = ent.text
        elif ent.text.startswith('Education') or ent.text.startswith('EDUCATION'):
            education = ent.text
        elif ent.text.startswith('Experience') or ent.text.startswith('EXPERIENCE'):
            experience = ent.text

    return name, email, phone_number, education, experience

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume_file = request.FILES['resume_file'].read().decode('utf-8')
            name, email, phone_number, education, experience = extract_resume_data(resume_file)
            resume = Resume(name=name, email=email, phone_number=phone_number, education=education, experience=experience)
            resume.save()
            return redirect('resume_data', pk=resume.pk)
    else:
        form = ResumeUploadForm()
    return render(request, 'upload_resume.html', {'form': form})
