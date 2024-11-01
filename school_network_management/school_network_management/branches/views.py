# branches/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Branch, ServiceProvider
from .forms import ServiceProviderForm

def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'branches/branch_list.html', {'branches': branches})

def service_provider_form(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    if request.method == 'POST':
        form = ServiceProviderForm(request.POST)
        if form.is_valid():
            service_provider = form.save(commit=False)
            service_provider.branch = branch
            service_provider.save()
            return redirect('branch_list')
    else:
        form = ServiceProviderForm()
    return render(request, 'branches/service_provider_form.html', {'form': form, 'branch': branch})
