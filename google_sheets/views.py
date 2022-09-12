from django.shortcuts import render
from django.views.generic import TemplateView
from task123.sheets import Sheets
from google_sheets.models import GoogleSheets
from datetime import datetime


class Home(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        sheets = Sheets()
        GoogleSheets.objects.all().delete()
        for data in sheets.get_data():
            GoogleSheets.objects.create(number=data[0], order_number=data[1],
                                        price=data[2], date=datetime.strptime(data[3], '%d.%m.%Y'), price_rubles=data[4])
        return render(request, self.template_name, context={'sheets': GoogleSheets.objects.all()})
