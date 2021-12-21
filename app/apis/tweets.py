from flask_restx import Namespace, Resource

api = Namespace("tweets", description="Tous ce qui concerne les tweets")


@api.route("/hello")
class TweetResource(Resource):
    def get(self):
        return "Goodbye. See you next time."