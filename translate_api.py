import six
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account
import configsx


def translate_text(target, text):
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    creds = service_account.Credentials.from_service_account_file(filename=configsx.API_translate_json_secret_path)
    translate_client = translate.Client(credentials=creds)

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")
    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)
    return result

if __name__ == '__main__':
    test_1 = translate_text('en', 'Salutare, ce mai faci?')
    print(test_1)