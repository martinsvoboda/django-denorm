from django.core.management.base import BaseCommand
from denorm import fields

class Command(BaseCommand):

    def handle(self, **kwargs):
        print "This management command is deprecated."
        print "Please consult the documentation for a command reference."
