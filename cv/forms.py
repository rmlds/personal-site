from django import forms

from .models import Skill, Education, Achievement, Course

class SkillForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ('title',)

class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = ('title', 'date', 'description',)

class AchievementForm(forms.ModelForm):

    class Meta:
        model = Achievement
        fields = ('title', 'date',)

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('title',)
