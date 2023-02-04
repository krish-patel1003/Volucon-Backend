from rest_framework import serializers
from .models import VolunteerProfile, Skills

class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = '__all__'

class VolunteerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = VolunteerProfile
        fields = '__all__'
    
    def create(self, validated_data):
        print("validated_data:", validated_data)
        skills = []
        for s in validated_data["skills"]:
            skills.append(s.id)
        print(skills)
        volunteer = VolunteerProfile.objects.create(
            user=validated_data.get("user"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            age=validated_data.get("age"),
            gender=validated_data.get("gender"),
            city=validated_data.get("city"),
            state=validated_data.get("state"),
            phone=validated_data.get("phone"),
            contact_email=validated_data.get("contact_email"),
            linkedin=validated_data.get("linkedin"),
            twitter=validated_data.get("twitter"),
            instagram=validated_data.get("instagram"),
            experience=validated_data.get("experience"),
            preferences=validated_data.get("preferences"),
        )

        volunteer.save()
        for s in validated_data["skills"]:
            skills.append(s.id)
            volunteer.skills.add(s)
        print(skills)

        return volunteer


    # def update(self, instance, validated_data):
        
    

