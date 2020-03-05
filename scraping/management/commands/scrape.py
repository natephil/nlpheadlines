from newscatcher import Newscatcher
from datetime import datetime

from django.core.management.base import BaseCommand

from scraping.models import Headline

class Command(BaseCommand):
    help = "collect headlines"
        
    # define logic of command
    def handle(self, *args, **options):
        
        # define news website
        nytimes = Newscatcher('nytimes.com')
    
        # get headlines
        news = nytimes.news
        
        # grab all headlines
        for n in news:
            title = n.title
            published_date = n.published
            # published_date = datetime.strptime(n.published, "%a, %d %b %Y %I:%M:%S %z").strftime("%Y-%m-%d")

            # check if url in db
            try:
                # save in db
                Headline.objects.create(
                    title=title,
                    published_date=published_date
                )
                print('%s added' % (title))
            except:
                print('%s already exists' % (title,))

        self.stdout.write( '\n\nHeadlines Collected!' )