from django.core.management.base import BaseCommand
from subprocess import call


class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        call(["python", "manage.py", "loaddata", "fixtures/initial-data.json"])

        self.stdout.write('\n[+] done.')
