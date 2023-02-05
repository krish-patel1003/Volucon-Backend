from profiles.models import VolunteerProfile
from profiles.views import VolunteerProfileDetail

def get_info(request):
    print(request.user)
    v = VolunteerProfile.objects.get(user=request.user)
    print(v)
    print(v.skills.all())
    skills = []
    for s in v.skills.all():
        skills.append(s.skill_name)

    data = {
        "age": v.age,
        "gender": v.gender,
        "city": v.city,
        "state": v.state,
        "experience": v.experience,
        "preferences": v.preferences,
        "skills": skills
    }
    return data