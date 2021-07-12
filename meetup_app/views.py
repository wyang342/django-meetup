from django.shortcuts import render, redirect
from .models import Group, Event
from .forms import GroupForm, EventForm
from django.contrib.auth.decorators import login_required


# Helper methods


def _get_group(group_id):
    return Group.objects.get(id=group_id)


def _get_event(event_id):
    return Event.objects.get(id=event_id)

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

    if request.user != group.owner:
        return redirect('show_group', group_id=group.id)

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

    if request.user != group.owner:
        return redirect('show_group', group_id=group.id)

    group.delete()
    return redirect('show_groups')


@login_required
def show_events(request, group_id):
    group = _get_group(group_id)
    events = group.events.all()

    context = {'group': group, 'events': events}
    return render(request, 'meetup_app/events_list.html', context)


@login_required
def show_event(request, group_id, event_id):
    group = _get_group(group_id)
    event = _get_event(event_id)

    context = {'group': group, 'event': event}
    return render(request, 'meetup_app/event_detail.html', context)


@login_required
def create_event(request, group_id):
    group = _get_group(group_id)

    context = {}
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            new_event = form.save(commit=False)
            new_event.group = group
            new_event.save()
            return redirect('show_event', group_id=group.id, event_id=new_event.id)
    else:
        form = EventForm()
        context = {'form': form, 'type_of_request': 'New'}
    return render(request, 'meetup_app/event_form.html', context)


@login_required
def edit_event():
    pass


@login_required
def delete_event():
    pass
