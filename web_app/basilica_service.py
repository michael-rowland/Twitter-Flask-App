import basilica
import os
from dotenv import load_dotenv
from web_app.twitter_service import twitter_api


load_dotenv()
API_KEY = os.getenv('BASILICA_API_KEY') 

connection = basilica.Connection(API_KEY)

if __name__ == "__main__":
    twitter_api_client = twitter_api()
    statuses = twitter_api_client.user_timeline(
            'aarongleeman', 
            tweet_mode="extended", 
            count=50, 
            exclude_replies=True, 
            include_rts=False)

    statuses_full_text = [status.full_text for status in statuses]
    embeddings = connection.embed_sentences(
            statuses_full_text,
            model='twitter')
    embeddings_list = [embedding for embedding in embeddings]
    print(len(embeddings_list))
#     for embedding in embeddings:
#             print(dir(embedding))
