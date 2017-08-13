from django.shortcuts import redirect, render, reverse

from .forms import PatientForm, PlanForm


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
            # return redirect('view_plans', args=[patientid])
            request.method = 'GET'
            print(request)
            return view_plans(request, patientid)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PatientForm()

    return render(request, 'plancheck/index.html', {'form': form})


def view_plans(request, patientid):
    print('here')

    # ---- Set up some dummy plans
    plans = []
    for plan in patientid:
        plans.append(plan)

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlanForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            selectedplan = form.cleaned_data['selectedplan']

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return redirect('view_plans', args=[patientid])

            # ---- This is daft and doesn't work
            request.method = 'GET'
            print(request)
            return index(request)

    # if a GET (or any other method) we'll create a blank form
    else:

        form = PlanForm()

        # ---- Not sure why this is needed, should prob used init function in PlanForm
        form.fields['selectedplan'].choices = []


        choices = []
        for idx in range(len(plans)):
            form.fields['selectedplan'].choices.append((idx, plans[idx]))


    return render(request, 'plancheck/view_plans.html', {'form': form, 'patientid': patientid, }, )
