from django.core.management.base import BaseCommand, CommandError
from shortener.models import asifURL

class Command(BaseCommand):
    help = 'Refreshes all asifURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return asifURL.objects.refresh_shortcodes(items=options['items'])
