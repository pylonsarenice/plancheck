from django.shortcuts import redirect, render, reverse

from .forms import PatientForm

def index(request):
    # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = PatientForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                patientid = form.cleaned_data['patientid']

                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                #return redirect('view_plans', args=[patientid])
                return view_plans(request, patientid)

        # if a GET (or any other method) we'll create a blank form
        else:
            form = PatientForm()

        return render(request, 'plancheck/index.html', {'form': form})

def view_plans(request, patientid):

    return render(request, 'plancheck/view_plans.html', {'patientid': patientid})