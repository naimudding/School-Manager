from django.db import models

# Create your models here.
CLASSES = (('Nurani Qayda', 'Nurani Qayda'),
			('Nazra', 'Nazra'), 
			('Hifz', 'Hifz'), 
			('Farsi', 'Farsi'), 
			('Alimiyat', 'Alimiyat')
		)

STATUS = (('Active', 'Active'),
            ('Graduated', 'Graduated'), 
            ('Absconded', 'Absconded'), 
            ('Transferred', 'Transferred')
        )
RELATIONS = (('Father', 'Father'),
            ('Mother', 'Mother'), 
            ('CareTaker', 'CareTaker')
        )

class Students(models.Model):
    sr_no = models.CharField(max_length=100, unique=True)
    old_sr_no = models.CharField(max_length=100, unique=True,null=True,blank=True)
    fullname = models.CharField(max_length = 30)
    guardian_relation = models.CharField(max_length=20, choices = RELATIONS, default = "Father")
    guardian_name = models.CharField(max_length=50)
    father_biz = models.CharField(max_length=30,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    caste = models.CharField(max_length = 30, null=True,blank=True)
    date_of_birth = models.DateField()
    father_mobile = models.CharField(max_length = 20, null=True,blank=True)
    date_of_joining = models.DateField(null=True,blank=True)
    class_name = models.CharField(max_length = 25, choices = CLASSES)
    status = models.CharField(max_length = 25, choices = STATUS, default = "Active", null=True, blank=True)
    city = models.CharField(max_length = 30)
    pincode = models.CharField(max_length = 30, null=True,blank=True)
    aadhar = models.FileField(upload_to = "students_docs/aadhars", null=True,blank=True)
    picture = models.ImageField(upload_to = "students_docs/pictures", null=True,blank=True)

class StudentTerminate(models.Model):
    student = models.OneToOneField(Students, on_delete=models.CASCADE)
    date_of_leaving = models.DateField()
    reason_of_leaving = models.TextField(null=True,blank=True)
    is_tc_issued = models.CharField(max_length = 25, choices = (("Yes", "Yes"),("No", "No")),null=True,blank=True)

class StudentPreviousStudy(models.Model):
    student = models.OneToOneField(Students, on_delete=models.CASCADE)
    prev_study = models.CharField(max_length = 30, null=True,blank=True)
    prev_marks = models.CharField(max_length = 30, null=True,blank=True)
    pre_date_of_leaving = models.DateField(null=True,blank=True)
    prev_reason_of_leaving = models.TextField(null=True,blank=True)
    is_prev_tc_issued = models.CharField(max_length = 25, choices = (("Yes", "Yes"),("No", "No")),null=True,blank=True)

class StudentDocuments(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    document_name = models.CharField(max_length = 20)
    document_path = models.FileField(upload_to = "students_docs/")
    class Meta:
        unique_together = ("student", "document_name")