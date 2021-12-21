from flask_restx import Namespace, Resource, fields
from app.db import tweet_repository
from flask import json

api = Namespace("tweets", description="Tous ce qui concerne les tweets")

model = api.model("Model", {
    "id": fields.Integer,
    "text": fields.String,
    "created_at": fields.DateTime
})

class TweetDao(object):
    def __init__(self, id, text, created_at):
        self.id = id
        self.text = text
        self.created_at = created_at

@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
class TweetResource(Resource):
    @api.marshal_with(model)
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404)
        else:
            return TweetDao(id=tweet.id, text=tweet.text, created_at=tweet.created_at)