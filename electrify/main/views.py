# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
  """
    Landing page
  """

  data = {}

  return render_to_response("main/home.html", data, context_instance=RequestContext(request))

def about(request):

  data = {}

  return render_to_response("main/about.html", data, context_instance=RequestContext(request))

def dashboard(request):
  """
    Show users customized dashboard
  """

  data = {}

  return render_to_response("main/dashboard.html", data, context_instance=RequestContext(request))
