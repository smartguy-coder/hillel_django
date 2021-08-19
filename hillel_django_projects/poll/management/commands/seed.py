import datetime

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker

from poll.models import Question


# имя файла является название команды
class Command(BaseCommand):

    # Description of the command will be placed in parameter 'help'
    help = 'Add new question(s) to the system'

    # We parse all arguments in this method
    def add_arguments(self, parser):
        parser.add_argument('-l', '--len', type=int, default=10)

    # We put a logic of the command here
    def handle(self, *args, **options):
        # Initialize Faker as object
        faker = Faker()

        # We use self.stdout.write instead of print to make visual inference of the process
        self.stdout.write('Start generating Questions')
        for _ in range(options['len']):
            self.stdout.write('Generating Question {}'.format(_ + 1))
            question = Question()
            # Faker generates text for the questions. We may also give a list of designed
            # questions to the Faker as parameter
            question.question_text = faker.text(max_nb_chars=50)[:-1] + "?"
            question.pub_date = timezone.now()
            question.save()
        self.stdout.write('End generating Questions')