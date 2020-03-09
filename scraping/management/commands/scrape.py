from newscatcher import Newscatcher
from datetime import datetime
from time import mktime

from django.core.management.base import BaseCommand

from scraping.models import Headline

# define news website
nytimes = Newscatcher('nytimes.com')
usa_today = Newscatcher('usatoday.com')
la_times = Newscatcher('latimes.com')
guardian = Newscatcher('theguardian.com')
wash_post = Newscatcher('washingtonpost.com')
daily_mail = Newscatcher('dailymail.co.uk')
NBC = Newscatcher('nbcnews.com')
fox = Newscatcher('foxnews.com')
huff_post = Newscatcher('huffpost.com')
google_news = Newscatcher('news.google.com')
wired = Newscatcher('wired.com')

news_list = [usa_today, la_times, guardian, wash_post, daily_mail, NBC, fox, huff_post, google_news, nytimes, wired]

class Command(BaseCommand):
    help = "collect headlines"

    # define logic of command
    def handle(self, *args, **options):

        for n in news_list:
            news = n.news
            source = n.website
            for i in news:
                title = i.title
                # published_date = i.published
                published_date = datetime.fromtimestamp(mktime(i.published_parsed))

        # get headlines
        # news = nytimes.news

        # grab all headlines
        # for n in news:
            # source = news.website
            # title = n.title
            # published_date = n.published
            # published_date = datetime.fromtimestamp(mktime(i.published_parsed))

                # check if url in db
                exists = False
                try:
                    exists = Headline.objects.get(
                        source=source,
                        title=title,
                        published_date=published_date
                    )
                except:
                    pass
                # store data in db
                if exists == False:
                    try:
                        # save in db
                        Headline.objects.create(
                            source=source,
                            title=title,
                            published_date=published_date
                        )
                        print('%s added' % (title))
                    except:
                        print('%s Error storing in database' % (title,))

        self.stdout.write( '\n\nFinished Collecting Headlines!' )