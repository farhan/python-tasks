from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from myurlshortner.forms import UrlForm
from myurlshortner.logic import url_key_db_utils
from myurlshortner.logic import constants
from myurlshortner.logic import utils
from myurlshortner.models import UrlKey


def redirect(request):
    key = utils.clean_key(request.path)
    url_key = UrlKey.objects.filter(key_name=key).first()
    if url_key is None or url_key.assigned_url is None:
        return HttpResponse('Key <b>' + key + '</b> is not assigned to any url.')
    else:
        return HttpResponseRedirect(url_key.assigned_url)


def index(request):
    if request.POST.get('btn_shorten'):
        form = UrlForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            url = data['url']
            key = url_key_db_utils.get_best_key(url)
            key.is_assigned = True
            key.assigned_timestamp = timezone.now()
            key.assigned_url = str(url)
            key.save()
            shorten_url = constants.DOMAIN_NAME + key.key_name
            return render(request, 'index.html', {'form': form, 'shorten_url': shorten_url})
    else:
        form = UrlForm()
    return render(request, 'index.html', {'form': form})
