#install
import paralleldots


class API:

    def __init__(self) -> None:
        paralleldots.set_api_key("bOZS78qxwSvTFlAAHxY3aGDiJJNCShfTJWK7pmogHBE")

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

