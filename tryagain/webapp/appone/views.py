from django.shortcuts import render
from django.views.generic import ListView,DeleteView,UpdateView
from appone.models import Subject
from django.urls import reverse_lazy


class Show(ListView):
    model=Subject
    template_name="show.html"
    context_object_name="subjects"
    
    def get_queryset(self):
        qeryset=super().get_queryset()
        query = self.request.GET.get("search","")

        if query:
            qeryset=qeryset.filter(subject_id__icontains=query)
        return qeryset
    
