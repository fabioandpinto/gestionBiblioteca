from datetime import date

from django.shortcuts import render
from django.views.generic import FormView

# Create your views here.
from .models import Prestamo
from .forms import PrestamoForm


class NuevoPrestamo(FormView):
    template_name = 'prestamo/nuevo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):
        Prestamo.object.create(
            lector=form.cleaned_data['lector'],
            book=form.cleaned_data['book'],
            date_require=date.today(),
            returned=False
        )
        return super().form_valid(form)
