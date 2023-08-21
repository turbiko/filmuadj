from django.shortcuts import render, get_object_or_404
from .models import Announcement

def announcement(request, pk):
    context = {}
    zakup_item = get_object_or_404(Announcement, pk=pk)
    context['announcement'] = zakup_item
    context['item_exist'] = True if zakup_item else False
    print("Announcement: ", pk)
    return render(request, 'announcement/zakupitem.html', context)


def announcements(request):
    context = {}
    announcements = Announcement.objects.all()
    print("Announcements: ", len(announcements), announcements)
    context['announcements'] = announcements
    return render(request, 'announcement/announcements.html', context)