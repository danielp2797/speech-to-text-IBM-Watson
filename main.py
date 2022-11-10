from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from src.secrets.authentication import get_authentication
from src.text_to_speech.ibm_text_to_speech_client import convert_audio_to_text
import sys

CREDENTIALS_FILE = 'config/credentials/credentials.json'

if __name__ == '__main__':

    URL, API_KEY = get_authentication(CREDENTIALS_FILE)
    service = SpeechToTextV1(authenticator=IAMAuthenticator(API_KEY))
    service.set_service_url(URL)
    audio_file = sys.argv[1]

    result = convert_audio_to_text(service, audio_file)
    print(result)