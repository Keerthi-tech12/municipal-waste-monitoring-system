from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create default users'

    def handle(self, *args, **kwargs):

        users = [
            ('admin', 'raja1505', True, True),
            ('commissioner', 'comm1505', False, False),
            ('keerthiga', 'keerthi1210', False, False),
            ('operator', 'oper1505', False, False),
            ('zoneofficer', 'zone1505', False, False),
        ]

        for username, password, is_staff, is_superuser in users:

            if not User.objects.filter(username=username).exists():

                user = User.objects.create_user(
                    username=username,
                    password=password
                )

                user.is_staff = is_staff
                user.is_superuser = is_superuser
                user.save()

                self.stdout.write(
                    self.style.SUCCESS(f'Created user: {username}')
                )