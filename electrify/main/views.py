# Create your views here.
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings

from main.models import UserProfile, AccountNumber

from main.forms import CustomerForm

import uuid, csv

def home(request):
  """
    Landing page
  """

  data = {}

  if request.method == "GET":
    # just getting the first landing page, fill form if they were filling things out
    form = CustomerForm()
  else:
    # posting the form 
    """
    form = CustomerForm(request.POST)
    if form.is_valid():
      # save form
      email = form.cleaned_data["email"]
      zip_code = form.cleaned_data["zip_code"]
      account_number = form.cleaned_data["account_number"]
      if User.objects.filter(email=email).exists():
        # just use existing profile

        user = User.objects.get(email=email)
        # profile should exist
        prof = UserProfile.objects.get(user=user)
        
        # get the account number or create it
        account, created = AccountNumber.objects.get_or_create(account_number=account_number)
        # add account number to the profile 
        prof.account_numbers.add(account)
      else:
        # create a user
        first, last = email.split("@")
        user = User(username=str(uuid.uuid1())[:30], first_name=first, last_name=last, email=email)
        user.save()

        # create a user profile
        prof = UserProfile(user=user, zip_code=zip_code)
        prof.save()

        # create the account number
        account, created = AccountNumber.get_or_create(account_number=account_number)
        # assign the account number to user profile
        prof.account_numbers.add(account)
      """
    return HttpResponseRedirect(reverse("dashboard"))

  data["form"] = form

  return render_to_response("main/home.html", data, context_instance=RequestContext(request))

def about(request):

  data = {}

  return render_to_response("main/about.html", data, context_instance=RequestContext(request))

def dashboard(request):
  """
    Show users customized dashboard
  """

  data = {}

  MEDIA_ROOT = settings.MEDIA_ROOT

  f = open(MEDIA_ROOT+'PTC_AllOffers_2012-05-05.csv', 'r')

  csv_reader = csv.DictReader(f)

  data["provider_info"] = [] 

  total_kw_hrs = 881

  for row in csv_reader:
    provider_data = {}
    if row["TduCompanyName"] == "ONCOR ELECTRIC DELIVERY COMPANY" and row["TermValue"] in ["0", "1"]:
      provider_data["RepCompany"] = row["RepCompany"]
      provider_data["Product"] = row["Product"]
      provider_data["Kwh"] = float(row["kwh1000"])*total_kw_hrs
      provider_data["AvgPrice"] = float(row["kwh1000"])
      provider_data["Renewable"] = row["Renewable"]
      provider_data["RateType"] = row["RateType"]
      provider_data["TermValue"] = row["TermValue"]
      provider_data["CancelType"] = row["CancelType"]
      provider_data["TermsURL"] = row["TermsURL"]
      provider_data["FactsURL"] = row["FactsURL"]
      data["provider_info"].append(provider_data)
  return render_to_response("main/dashboard.html", data, context_instance=RequestContext(request))
