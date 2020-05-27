from django.core.management.base import BaseCommand, CommandError
from user_activity.models import User, Activity
import time
from datetime import date


def createUser(paramName, paramTz):
    user = User(name=paramName, timezone=paramTz)
    user.save()
    return user


def createActivity(user, start, end):
    activity = Activity(user=user, start_time=start, end_time=end)
    activity.save()


class Command(BaseCommand):
    '''
    Django admin command to populate database
    can be fired with - python3 manage.py populate_db
    '''

    help = 'Command to populate DB'

    def handle(self, *args, **kwargs):
        try:
            user = createUser("Ram", "asia")
            self.stdout.write('User Created')

            createActivity(user, date(2005, 7, 27), date(2005, 8, 27))
            createActivity(user, date(2006, 7, 27), date(2006, 8, 27))
            self.stdout.write('Activity Created')

        except Exception as e:
            raise CommandError(e)
            return

        self.stdout.write(self.style.SUCCESS('Database Populated!'))
