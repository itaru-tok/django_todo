from django.shortcuts import render, redirect
from .models import TodoItem

def todo_view(request):
    todo_items = TodoItem.objects.all().order_by('-created_at')
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        new_item = TodoItem(content=request.POST['content'])
        new_item.save()
        return redirect('/')
    return render(request, 'todo/todo_list.html', {'todo_items': todo_items})
