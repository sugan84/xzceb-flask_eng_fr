"""
Translator Module
"""

#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-11-11',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(eng_text):
    """
    Convert english to french
    """
    if eng_text != '':
        translation = language_translator.translate(text=eng_text, model_id='en-fr').\
            get_result()
        return translation['translations'][0]['translation']


def frenchToEnglish(fr_text):
    """
    Convert french to english
    """
    if fr_text != '':
        translation = language_translator.translate(text=fr_text, model_id='fr-en').\
            get_result()
        return translation['translations'][0]['translation']
