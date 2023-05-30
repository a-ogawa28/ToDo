from django.shortcuts import redirect, render
from django.db.models import Q, Count
from django.views import generic
from django.urls import reverse_lazy
from .models import Todo, Reply
from .forms import TodoForm, TodoUpdateForm, TodoSearchForm, ReplyForm2


class Top(generic.TemplateView):
    model = Todo
    template_name = 'todo/index.html'


class TodoList(generic.ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TodoSearchForm(self.request.GET or None)
        context['todo_count'] = Todo.objects.all().count()
        return context

    def get_queryset(self):
        queryset = Todo.objects.order_by('-updated_at', 'category', 'deadline')
        q_keyword = self.request.GET.get('keyword')
        if q_keyword:
            queryset = queryset.filter(
                Q(title__icontains=q_keyword) | Q(content__icontains=q_keyword)
                | Q(reply__comment__icontains=q_keyword)
            ).distinct()
        return queryset


class TodoDetail(generic.DetailView):
    model = Todo
    template_name = 'todo/todo_detail.html'


class TodoCreate(generic.CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/todo_create.html'
    success_url = reverse_lazy('todo:todo_status')


class TodoUpdate(generic.UpdateView):
    model = Todo
    form_class = TodoUpdateForm
    template_name = 'todo/todo_update.html'
    success_url = reverse_lazy('todo:todo_status')


class TodoDelete(generic.DeleteView):
    model = Todo
    template_name = 'todo/todo_delete.html'
    success_url = reverse_lazy('todo:todo_status')


class TodoStatus(generic.TemplateView):
    model = Todo
    template_name = 'todo/todo_status.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['waiting_list']  = Todo.objects.filter(status__status_name='Waiting').order_by('deadline', 'category', '-updated_at')
        context['waiting_count'] = Todo.objects.filter(status__status_name='Waiting').count()
        context['working_list']  = Todo.objects.filter(status__status_name='Working').order_by('deadline', 'category', '-updated_at')
        context['working_count'] = Todo.objects.filter(status__status_name='Working').count()
        context['done_list']     = Todo.objects.filter(status__status_name='Done').order_by('deadline', 'category', '-updated_at')
        context['done_count']    = Todo.objects.filter(status__status_name='Done').count()
        context['todo_count']    = Todo.objects.all().count()
        return context


class ReplyCreate(generic.CreateView):
    model = Reply
    form_class = ReplyForm2
    template_name = 'todo/reply_create.html'
    success_url = reverse_lazy('todo:todo_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo'] = Todo.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        todo = Todo.objects.get(pk=self.kwargs['pk'])
        reply = form.save(commit=False)
        reply.target = todo
        reply.save()
        return redirect('todo:todo_list')
