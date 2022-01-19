from django.core.management.base import BaseCommand, CommandError
from questions.models import Question, Answer

import random

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=0)
        parser.add_argument('--questions', type=int, default=0)


    def handle(self, *args, **options):
        self.create_answers()
        
    def create_answers(self):
        questions = Question.objects.all()
        random_index_of_questions = [random.randint(0, 100000) for i in range(0,10000)]
        answers_to_create=[Answer(text=f"This is forth answer for {random_index_of_questions[i]} question", question=questions[random_index_of_questions[i]]) for i in range(0,10000)]
        Answer.objects.bulk_create(answers_to_create)
