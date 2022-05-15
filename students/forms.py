from django import forms
from .models import Students, StudentTerminate, StudentPreviousStudy, StudentDocuments

class StudentsForm(forms.ModelForm):
	class Meta:
		model = Students
		fields = "__all__"

class StudentTerminateForm(forms.ModelForm):
	class Meta:
		model = StudentTerminate
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(StudentTerminateForm, self).__init__(*args, **kwargs)
		self.fields['student'].required = False

class StudentPreviousStudyForm(forms.ModelForm):
	class Meta:
		model = StudentPreviousStudy
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(StudentPreviousStudyForm, self).__init__(*args, **kwargs)
		self.fields['student'].required = False

class StudentDocumentsForm(forms.ModelForm):
	class Meta:
		model = StudentDocuments
		fields = "__all__"
	def __init__(self, *args, **kwargs):
		super(StudentDocumentsForm, self).__init__(*args, **kwargs)
		self.fields['student'].required = False