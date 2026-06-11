from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import UserProfile

class Command(BaseCommand):
    help = 'Create default users'

    def handle(self, *args, **kwargs):

        users = [
    ('admin', 'raja1505', True, True, 'Commissioner'),
    ('commissioner', 'comm1505', False, False, 'Commissioner'),
    ('keerthiga', 'keerthi1210', False, False, 'Commissioner'),
    ('operator', 'oper1505', False, False, 'Data Entry Operator'),
    ('zoneofficer', 'zone1505', False, False, 'Zone Officer'),
]

for username, password, is_staff, is_superuser, role in users:

    user, created = User.objects.get_or_create(
        username=username
    )

    if created:
        user.set_password(password)

    user.is_staff = is_staff
    user.is_superuser = is_superuser
    user.save()

    UserProfile.objects.get_or_create(
        user=user,
        defaults={
            'role': role
        }
    )

    self.stdout.write(
        self.style.SUCCESS(
            f'Created/Checked user: {username}'
        )
    )