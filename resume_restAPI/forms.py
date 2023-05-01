from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['resume_file']
        labels = {
            'resume_file': 'Resume (PDF file)'
        }

    def clean_resume_file(self):
        resume_file = self.cleaned_data.get('resume_file')
        if not resume_file.name.endswith('.pdf'):
            raise forms.ValidationError('Only PDF files are allowed.')
        return resume_file