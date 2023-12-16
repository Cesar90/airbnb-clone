from typing import Any
from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = "This command tells me testing"
    print("hello")

    def add_arguments(self, parser: CommandParser) -> None:
        # return super().add_arguments(parser)
        # python manage.py testing --times
        parser.add_argument("--times",help="How many times do you want to tell you that I am testing?")

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            # print("I am testing")
            self.stdout.write(self.style.SUCCESS("I am testing"))