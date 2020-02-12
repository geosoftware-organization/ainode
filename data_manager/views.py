import csv

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Country
# from .forms import UploadFileForm

# # Create your views here.


# @permission_required('admin.can_add_log_entry')
# def country_upload(request):
#     if request == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             # handle_uploaded_file(request.FILES['file'])
#             messages.info(request, 'File was successfuly uploaded into the Database!')
#         else:
#             messages.error(request, 'File was NOT uploaded!')

#     return request
#         # csv_file = 'test,csv'

#         # if not csv_file.endswith('.csv'):
#         #     messages.error(request, 'This is not a csv file!')

#         # data_set = csv_file.read().decode('UTF-8')
