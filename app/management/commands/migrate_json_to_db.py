# Python imports
import json
import os

# Django imports
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

# custom imports
from app.models import Movie, Genre

def upload_data_to_db(record):
    obj, status = Movie.objects.get_or_create(
        director=record['director'],popularity=record['99popularity'],
        score=record['imdb_score'],name=record['name'])

    for genre_name in record['genre']:
        genre_obj, status = Genre.objects.get_or_create(name=genre_name.strip())
        obj.genre.add(genre_obj)
    obj.save()

class Command(BaseCommand):
    def handle(self, *args, **options):
        proj_loc = settings.BASE_DIR
        path = os.path.join(proj_loc, 'sample_data.json')
        file_obj = open(path, 'r')
        data = json.loads(file_obj.read())
        for record in data[:5]:
            upload_data_to_db(record)
        file_obj.close()
        print('migrating json to db success')

