from django.shortcuts import render, get_object_or_404
from django.forms import modelformset_factory
from django.http import Http404,HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from .forms import *
from .models import *
from django.urls import reverse
from django.template.loader import get_template
from django.views.generic import View
from .utils import render_to_pdf #created in step 4
# Create your views here.
from django.contrib import messages

def key_details(request):
    pass

    return render(request, 'key.html', {})

def manage(request):
    form = ManageForm(request.POST or None, request.FILES or None)
    queslist = Dynamicques.objects.all()

    if form.is_valid():
        instance = form.save(commit=False)
        form.save()
        return HttpResponseRedirect('/key/ques')
    context={
        "form":form,     "queslist":queslist,  
    }
    return render(request, 'manage_ques.html', context)

def que_delete(request,id):
    template = 'manage_ques.html'
    question= get_object_or_404(Dynamicques, id=id)
    # if request.method=='POST':
    #     form= ManageForm(request.POST, instance=question)
    question.delete()
    messages.success(request, "Successfully deleted")
    return HttpResponseRedirect('/key/ques')
    # else:
    #     form = ManageForm(instance=question)
    # context = {"form": form , "question":question}
    # return render(request, template , context)

def que_update(request,id):
    template = 'manage_ques.html'
    question= get_object_or_404(Dynamicques, id=id)
    if request.method=='POST':
        form= ManageForm(request.POST, instance=question)
        form.save()
        return HttpResponseRedirect('/key/ques')
    else:
        form = ManageForm(instance=question)
    context = {"form": form , "question":question}
    return render(request, template , context)
   
def Add_keyword(request):
    form = KeywordForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save()
        keys = Dynamicques.objects.all()
        for key in keys:
            title= key.question.replace("<key>",instance.add_keyword)
            que1_instance = Detail.objects.create(title=title,keyword = instance)
            # que2_instance = Detail.objects.create(title='why we use '+instance.add_keyword+' ?',keyword = instance)
        return HttpResponseRedirect('/key/')
    context={
        "form":form,       
    }
    return render(request, 'Trainee_add_keyword.html', context)

def Keyword_list(request):
    form = KeywordListForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form_instance = form.save(commit=False)
            form.save()
            keyword_id = form_instance.id
        return HttpResponseRedirect(reverse('keyword_que_list', args=(keyword_id,)))
    Key = Keyword.objects.all()
    context={
        "form":form,
        "Key":Key,     
    }
    return render(request, 'keyword_list.html', context)

def keyword_que_list(request, keyword_id):
    instance = get_object_or_404(Keyword,id=keyword_id)
    form= UpdateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form_instance = form.save(commit=False)
            form.save()
            # detail_id = form_instance.id
    ExampleFormset = modelformset_factory(Detail,fields=("title","description"),extra=1, max_num=1)
    my_queryset = Detail.objects.filter(keyword__id=keyword_id)
    if request.method == 'POST':
        formset = ExampleFormset(request.POST or None)
        print("\n"*5)
        print("before valid")
        if formset.is_valid():
            print("\n"*5)
            print("inside valid")
            formset_instance=formset.save(commit=False)
            for obj in formset.deleted_objects:
                obj.delete()
            # presentation = Presentation.objects.get(id=presentation_id)
            for form in formset:   
                print("\n"*5)
                print("inside form")
                form_instance = form.save(commit=False)
                # form_instance.presentation = presentation
                # # form_instance.title = "New Title"
                # # form_instance.description = "New Desc"
                form_instance.save()


        return HttpResponseRedirect(reverse('key:de',args=(keyword_id,)))
    formset = ExampleFormset(queryset=my_queryset)
    # context= {'form': form}
    context = {'formset':formset,'form':form,'instance':instance}
    return render(request,'first.html',context)

def main(request):
    form= DetailForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form_instance = form.save(commit=False)
            form.save()
            presentation_id = form_instance.id
        return HttpResponseRedirect(reverse('key:detailview',args=(presentation_id,)))
    list = Presentation.objects.all()
    context = {'form':form,'presentation':list}

    return render(request,'new.html',context)

def detailview(request,presentation_id):
    form= UpdateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form_instance = form.save(commit=False)
            form.save()
            # detail_id = form_instance.id
    ExampleFormset = modelformset_factory(Detail,fields=("title","description"),extra=1, max_num=1)
    my_queryset = Detail.objects.filter(presentation__id=presentation_id)
    if request.method == 'POST':
        formset = ExampleFormset(request.POST or None)
        print("\n"*5)
        print("before valid")
        if formset.is_valid():
            print("\n"*5)
            print("inside valid")
            formset_instance=formset.save(commit=False)
            for obj in formset.deleted_objects:
                obj.delete()
            presentation = Presentation.objects.get(id=presentation_id)
            for form in formset:   
                print("\n"*5)
                print("inside form")
                form_instance = form.save(commit=False)
                form_instance.presentation = presentation
                # form_instance.title = "New Title"
                # form_instance.description = "New Desc"
                form_instance.save()


        return HttpResponseRedirect(reverse('key:deck',args=(presentation_id,)))
    formset = ExampleFormset(queryset=my_queryset)
    # context= {'form': form}
    context = {'formset':formset,'form':form}
    return render(request,'first.html',context)


def deck(request,presentation_id):
    titles = Detail.objects.filter(presentation__id=presentation_id)
    context = {'titles':titles}
    return render(request,'second.html',context)

def de(request,keyword_id):
    titles = Detail.objects.filter(keyword__id=keyword_id)
    context = {'titles':titles}
    return render(request,'fourth.html',context)

class GeneratePdf(View):
    def get(self, request, presentation_id , *args, **kwargs):
        template = get_template('invoice.html')
        titles = Detail.objects.filter(presentation__id=presentation_id)
        context ={'titles':titles}
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Second%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

class KeyPdf(View):
    def get(self, request, keyword_id , *args, **kwargs):
        template = get_template('invoice1.html')
        titles = Detail.objects.filter(keyword__id=keyword_id)
        context ={'titles':titles}
        html = template.render(context)
        pdf = render_to_pdf('invoice1.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Second%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
