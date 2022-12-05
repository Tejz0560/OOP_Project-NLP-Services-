#install
import paralleldots


class API:

    def __init__(self) -> None:
        paralleldots.set_api_key("bOZS78qxwSvTFlAAHxY3aGDiJJNCShfTJWK7pmogHBE")

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner(self,text):
        response = paralleldots.ner(text)
        return response

    def emotion(self,text):
        response = paralleldots.emotion(text)
        return response
