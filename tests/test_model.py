from flask_testing import TestCase
from app import create_app

from app.models.tweet import Tweet

class TestModel(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def test_instance_variables_class_tweets(self):
        first_tweet = "Mon premier tweet. Ourraaaa :)!"
        tweet = Tweet(first_tweet)

        #on verifie qu'on a le meme contenu passer en parametre
        self.assertEqual(tweet.text, first_tweet)

        #on verifie la date de création, un tweet a toujours une date de création
        self.assertIsNotNone(tweet.created_at)

        # Vérifier que l'id du tweet n'est pas encore attribué lors de la création d'un tweet en mémoire.
        self.assertIsNone(tweet.id)
