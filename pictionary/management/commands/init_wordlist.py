import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from pictionary.models import WordModel


class Command(BaseCommand):
    help = 'Initializes the Pictionary wordlist'

    def handle(self, *args, **options):
        WordModel.objects.all().delete()
        word_list_json_file = os.path.join(settings.BASE_DIR, 'pictionary', 'wordlist.json')
        with open(word_list_json_file, 'r') as this_file:
            json_string = this_file.read()
        word_list_data = json.loads(json_string)
        word_array = word_list_data['words']
        existing_words = []
        for word in word_array:
            if word in existing_words:
                continue
            existing_words.append(word)
            w = WordModel(word=word)
            w.save()
