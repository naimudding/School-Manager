from django.shortcuts import render, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentsForm, StudentTerminateForm, StudentPreviousStudyForm, StudentDocumentsForm
from django.forms.formsets import formset_factory
from django.contrib import messages
from .models import Students, StudentPreviousStudy, StudentDocuments
from django.forms.models import model_to_dict
import pdb
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/user/login/')
def std_home_view(request):
	context = {"tab": "students"}
	return render(request, 'students/student_main.html', context)

@login_required(login_url='/user/login/')
def std_list_view(request):
	context = {"tab": "students"}
	return render(request, 'students/students_list.html', context)

@login_required(login_url='/user/login/')
def add_std_view(request):
	context = {"tab": "students"}
	FormSet = formset_factory(StudentDocumentsForm)
	student_form = StudentsForm()
	prev_study_form = StudentPreviousStudyForm()
	if request.method == "GET":
		context["formset"] = FormSet()
		context["student_form"] = student_form
		context["prev_study_form"] = prev_study_form
		return render(request, 'students/add_student.html', context)
	elif request.method == "POST":
		student_form = StudentsForm(request.POST, request.FILES)
		prev_study_form = StudentPreviousStudyForm(request.POST)
		formset = FormSet(request.POST, request.FILES)
		if student_form.is_valid() and prev_study_form.is_valid() and formset.is_valid():
			student = student_form.save()
			prev_study = prev_study_form.save(commit=False)
			prev_study.student = student
			prev_study.save()
			for form in formset:
				if form.cleaned_data.get("document_name") and form.cleaned_data.get("document_path"):
					doc = form.save(commit=False)
					doc.student = student
					try:
						doc.save()
					except IntegrityError:
						messages.error(request, 'Document name {} already exists.'.format(form.cleaned_data.get("document_name")))
						context["formset"] = formset
						return render(request, 'students/documents.html', context)
			messages.success(request, 'Student Added Successfully.')
			return redirect('students:list_student')
		else:
			for err in student_form.errors:
				messages.error(request, "{} is required, duplicate or invalid".format(err.replace("_"," ").capitalize()))
			for err in prev_study_form.errors:
				messages.error(request, "{} is required, duplicate or invalid".format(err.replace("_"," ").capitalize()))
			for errors in formset.errors:
				for err in errors:
					messages.error(request, "{} is required, duplicate or invalid".format(err.replace("_"," ").capitalize()))
			context["formset"] = formset
			context["student_form"] = student_form
			context["prev_study_form"] = prev_study_form
			return render(request, 'students/add_student.html', context)

@login_required(login_url='/user/login/')
def std_profile_view(request, student_id):
	context = {"tab": "students"}
	student = Students.objects.get(id=student_id)
	try:
		prev_study = StudentPreviousStudy.objects.get(student=student)
	except:
		prev_study= None
	if request.method == "GET":
		student_form = StudentsForm(instance=student)
		prev_study_form = StudentPreviousStudyForm(instance=prev_study)
		# pdb.set_trace()
		context["student_form"] = student_form
		context["prev_study_form"] = prev_study_form
		return render(request, 'students/std_profile.html', context)
	elif request.method == "POST":
		student_form = StudentsForm(request.POST, instance=student)
		prev_study_form = StudentPreviousStudyForm(request.POST, instance=prev_study)
		if student_form.is_valid() and prev_study_form.is_valid():
			student = student_form.save()
			prev_study = prev_study_form.save(commit=False)
			prev_study.student = student
			prev_study.save()
			messages.success(request, 'Student Data Edited Successfully.')
			return redirect('students:list_student')
		else:
			for err in student_form.errors:
				messages.error(request, "{} is required, duplicate or invalid".format(err.replace("_"," ").capitalize()))
			for err in prev_study_form.errors:
				messages.error(request, "{} is required, duplicate or invalid".format(err.replace("_"," ").capitalize()))
			context["student_form"] = student_form
			context["prev_study_form"] = prev_study_form
			return render(request, 'students/std_profile.html', context)

@login_required(login_url='/user/login/')
def std_doc_view(request, student_id):
	context = {"tab": "students"}
	student = Students.objects.get(id=student_id)
	student_docs = StudentDocuments.objects.filter(student=student)
	FormSet = formset_factory(StudentDocumentsForm)
	student_form = StudentsForm()
	context["student"] = student
	context["student_docs"] = student_docs
	if request.method == "GET":
		context["formset"] = FormSet()
		return render(request, 'students/documents.html', context)
	elif request.method == "POST":
		if request.FILES.get("aadhar"):
			student.aadhar = request.FILES.get("aadhar")
		if request.FILES.get("picture"):
			student.picture = request.FILES.get("picture")
		student.save()
		formset = FormSet(request.POST, request.FILES)
		if formset.is_valid():
			for form in formset:
				if form.cleaned_data.get("document_name") and form.cleaned_data.get("document_path"):
					doc = form.save(commit=False)
					doc.student = student
					try:
						doc.save()
					except IntegrityError:
						messages.error(request, 'Document name {} already exists.'.format(form.cleaned_data.get("document_name")))
						context["formset"] = formset
						return render(request, 'students/documents.html', context)
			messages.success(request, 'Documents saved Successfully.')
			return redirect('students:list_student')
		else:
			for form in formset:
				for err in form.errors:
					messages.error(request, "{} is required or duplicate or invalid".format(err.replace("_"," ").capitalize()))
			context["formset"] = formset
			return render(request, 'students/documents.html', context)

@login_required(login_url='/user/login/')
def std_terminate_view(request, student_id):
	context = {"tab": "students"}
	terminate_form = StudentTerminateForm()
	student = Students.objects.get(id=student_id)
	if request.method == "GET":
		context["terminate_form"] = terminate_form
		return render(request, 'students/termination_form.html', context)
	elif request.method == "POST":
		status = request.POST.dict()["status"]
		terminate_form = StudentTerminateForm(request.POST)
		if terminate_form.is_valid():
			if status:
				student.status = status
				student.save()
			term = terminate_form.save(commit=False)
			term.student = student
			term.save()
			messages.success(request, 'Termination form saved Successfully.')
			return redirect('students:list_student')
		else:
			for err in terminate_form.errors:
				messages.error(request, "{} is required, duplicate or invalid".format(err.replace("_"," ").capitalize()))
			
			context["terminate_form"] = terminate_form
			return render(request, 'students/termination_form.html', context)

