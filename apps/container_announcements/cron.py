from datetime import datetime

from apps.container_announcements.models import ContainerAnnouncement


def check_container_announcement_status():
    container_announcements = ContainerAnnouncement.objects.filter(status=1)
    today = datetime.today().date()
    time = datetime.today().time()
    print(today)
    for item in container_announcements:
        print(item.schedule_date_from)
        if item.schedule_date_from < today and item.schedule_time_from < time:
            item.status = 0
            item.save()
    print('success')
