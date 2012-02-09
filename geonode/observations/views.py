# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4

#Copyright (C) 2012  FaultedEarth
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/agpl.html>.

from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_response_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import simplejson
from django.db import connection, transaction

from geonode.observations import models
from geonode.observations.forms import Observation
from geonode.observations.utils import create_faultsource


#views for the observation form
def obsform(request):
    if request.method == 'POST':
        form = Observation(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("obsform_form.html",
                      {'form': form,
                       'success' : 'Your observation was saved'},
                context_instance=RequestContext(request))
    else:
        form = Observation()
    return render_to_response('obsform_form.html', {'form': form},
                              context_instance=RequestContext(request))

def traces(request):

    response = HttpResponse()
    if request.method == 'PUT':

        json_data = request.raw_post_data

        fault_section = models.FaultSection.objects.create()

        for trace in simplejson.loads(json_data):
            if isinstance(trace, dict):
                fault_section.sec_name = trace['name']
            else:
                trace = models.Trace.objects.get(pk=trace.split('.')[1])
                trace.fault_section.add(fault_section)

        fault_section.save()


    return response

def faultsection(request):
    response = HttpResponse()
    if request.method == 'PUT':

        json_data = request.raw_post_data

        fault = models.Fault.objects.create()

        for fault_section in simplejson.loads(json_data):
            if isinstance(fault_section, dict):
                fault.fault_name = fault_section['name']
            else:
                fault_section = models.FaultSection.objects.get(
                        pk=fault_section)
                fault_section.fault.add(fault)

        fault.save()

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM set_fault_simplegeom(%s)", [fault.pk])
    transaction.commit_unless_managed()

    return response

def foldsection(request):
    response = HttpResponse()
    if request.method == 'PUT':

        json_data = request.raw_post_data

        fold = models.Fold.objects.create()

        for fold_section in simplejson.loads(json_data):
            if isinstance(fold_section, dict):
                fold.fold_name = fold_section['name']
            else:
                fold_section = models.FoldSection.objects.get(
                        pk=fold_section)
                fold_section.fold.add(fold)

        fold.save()

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM set_fold_simplegeom(%s)", [fold.pk])
    transaction.commit_unless_managed()

    return response
    
def foldtraces(request):

    response = HttpResponse()
    if request.method == 'PUT':

        json_data = request.raw_post_data

        fold_section = models.FoldSection.objects.create()

        for foldtrace in simplejson.loads(json_data):
            if isinstance(foldtrace, dict):
                fold_section.sec_name = foldtrace['name']
            else:
                foldtrace = models.FoldTrace.objects.get(pk=foldtrace.split('.')[1])
                foldtrace.fold_section.add(fold_section)

        fold_section.save()


    return response

def faultsource(request):
    if request.method == 'PUT':

        json_data = simplejson.loads(request.raw_post_data)
        name = json_data['name']
        fault_id = json_data['fault_id'].split('.')[-1]
        fault = models.Fault.objects.get(pk=fault_id)
        create_faultsource(fault, name)

    return HttpResponse('ok')
    
def export(request):
    if request.method == 'PUT':
        
        json_data = simplejson.loads(request.raw_post_data)
        
    return HttpResponse('ok')

def new(request, summary_id):
    o = models.Observations(summary_id=summary_id)
    o.save()

    return HttpResponseRedirect(
            '/observations/obsform/edit/%s/summary_id/%s' %
            (o.id, o.summary_id))


def edit(request, observation_id, summary_id):
    """
    The view that returns the Id filed from the fault summary table.
    """

    if request.method == 'POST':
        if observation_id and summary_id:
            o = get_object_or_404(models.Observations, pk=observation_id)
            o.summary_id = summary_id
            form = Observation(request.POST,instance=o)
        else:
            form = Observation(request.POST)
        if form.is_valid():
            form.save()
            return render_to_response("obsform_form.html",
                      {'form': form,
                       'success' : 'Your observation was saved'},
                context_instance=RequestContext(request))
    else:
        o = get_object_or_404(models.Observations, pk=observation_id)
        o.summary_id = summary_id

        form = Observation(instance=o)

    return render_to_response('obsform_form.html', {'form' : form},
                              context_instance=RequestContext(request))
