from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Employe, Affectation, Poste

@login_required
def employee_list(request):
    employees = Employe.objects.all()
    affectations = Affectation.objects.select_related('id_poste').all()
    emp_poste = {}
    for a in affectations:
        emp_poste[a.id_employe] = a.id_poste.libelle_poste
    employee_list_data = []
    for emp in employees:
        poste = emp_poste.get(emp.id_employe, 'Not assigned')
        employee_list_data.append({
            'employee': emp,
            'poste': poste,
        })
    context = {
        'employee_list': employee_list_data,
    }
    return render(request, 'hr/list.html', context)
