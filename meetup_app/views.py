from django.shortcuts import render, redirect
from .models import Group
from .forms import GroupForm
from django.contrib.auth.decorators import login_required


# Helper methods


def _get_group(group_id):
    return Group.objects.get(id=group_id)

# Function views


@login_required
def show_groups(request):
    groups = Group.objects.all()
    return render(request, 'meetup_app/groups_list.html', {'groups': groups})


@login_required
def show_group(request, group_id):
    group = _get_group(group_id)
    context = {'group': group}
    return render(request, 'meetup_app/group_detail.html', context)


@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            new_group = form.save()
            return redirect('show_group', group_id=new_group.id)
    else:
        form = GroupForm()
        context = {'form': form, 'type_of_request': 'New'}
    return render(request, 'meetup_app/group_form.html', context)


@login_required
def edit_group(request, group_id):
    group = _get_group(group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            edited_group = form.save()
            return redirect('show_group', group_id=edited_group.id)
    else:
        form = GroupForm(instance=group)
        context = {'form': form, 'type_of_request': 'Edit'}
    return render(request, 'meetup_app/group_form.html', context)


@login_required
def delete_group(request, group_id):
    group = _get_group(group_id)
    group.delete()
    return redirect('show_groups')
