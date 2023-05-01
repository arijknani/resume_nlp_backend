from django.http import JsonResponse
from .models import Resume

def get_resume_data(request, resume_id):
    try:
        resume = Resume.objects.get(id=resume_id)
        data = {
            "name": resume.name,
            "email": resume.email,
            "phone_number": resume.phone_number,
            "education": resume.education,
            "experience": resume.experience
        }
        return JsonResponse(data)
    except Resume.DoesNotExist:
        return JsonResponse({"error": "Resume data not found."})
