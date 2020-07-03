import csv
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse
 from django.views import View
 from .models import Bank, Branch
 from .serializers import BranchSerializer
 from django.core.files.storage import FileSystemStorage

 import codecs
 import io
 class ImportView(View):
     def get(self, request):
         return render(request, 'import.html')
 @@ -20,7 +17,7 @@ def post(self, request):
         decoded_file = csv_file.read().decode('utf-8').splitlines()
         reader = csv.DictReader(decoded_file)
         count = 0
         ifsc_list = list(Branch.objects.values_list('ifsc', flat=True))
         # ifsc_list = list(Branch.objects.values_list('ifsc', flat=True))
         for row in reader:
             bank_name = row.get('bank_name')
             ifsc = row.get('ifsc')
 @@ -50,14 +47,12 @@ def post(self, request):
             if created:
                 print("row created{}".format(branch_defaults))

             print("No of Rows imported - {} - {} ".format(count, branch_defaults))
             # print("No of Rows imported - {} - {} ".format(count, branch_defaults))

             count += 1
         context = {
             'count': count}
         messages.success(request, "{} rows imported.".format(count))

         return render(request, 'import.html',context)
         return render(request, 'import.html')


 class DetailView(View):
    def get(self, request, ifsc):
        branch = Branch.objects.filter(ifsc__iexact=ifsc).first()
        serializer = BranchSerializer(branch)
        return JsonResponse(serializer.data, safe=False)
class ListView(View):
    def get(self, request, city, bank):
        branch_qset = Branch.objects.filter(
            city__iexact=city, bank__name__icontains=bank)
        serializer = BranchSerializer(branch_qset, many=True)
        return JsonResponse(serializer.data, safe=False)
