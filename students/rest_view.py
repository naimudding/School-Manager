from django.http import HttpResponse, JsonResponse
from .models import Students
from .serializers import StudentListSerializer
from rest_framework.decorators import api_view
from django.db.models import Q
from math import ceil

@api_view(['GET'])
def students_list(request):
	input_data = request.GET.dict()
	print(input_data)
	search_query = input_data["search_query"].strip()
	class_filter = input_data["class_filter"]
	status_filter = input_data["active_filter"]
	item_per_page = int(input_data["item_per_page"])
	page_number = int(input_data["page_number"])
	if search_query:
		if class_filter:
			if status_filter:
				queryset = Students.objects.filter(
					Q(fullname__contains=search_query) | Q(sr_no__contains=search_query)
					).filter(class_name=class_filter).filter(status=status_filter)	
			else:
				queryset = Students.objects.filter(
					Q(fullname__contains=search_query) | Q(sr_no__contains=search_query)
					).filter(class_name=class_filter)
		else:
			if status_filter:
				queryset = Students.objects.filter(
					Q(fullname__contains=search_query) | Q(sr_no__contains=search_query)
					).filter(status=status_filter)
			else:
				queryset = Students.objects.filter(
					Q(fullname__contains=search_query) | Q(sr_no__contains=search_query)
					)
	else:
		if class_filter:
			if status_filter:
				queryset = Students.objects.filter(class_name=class_filter).filter(status=status_filter)
			else:
				queryset = Students.objects.filter(class_name=class_filter)
		else:
			if status_filter:
				queryset = Students.objects.filter(status=status_filter)
			else:
				queryset = Students.objects.all()

	total_students = len(queryset)
	total_page_number = ceil(total_students / item_per_page)

	start_index = (page_number-1)*item_per_page if (page_number-1)*item_per_page >= 1 else 0
	end_index = page_number*item_per_page if page_number*item_per_page < len(queryset) else len(queryset)

	students = queryset[start_index:end_index]
	serializer = StudentListSerializer(students, many=True)
	metadata = {"total_count":total_students, "page_number":page_number, "total_page":total_page_number}
	return JsonResponse(data={"data":serializer.data, "metadata":metadata}, status=200, safe=False)
