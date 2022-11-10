import json
from time import time


def convert_audio_to_text(service, audio_file_input: str):

    audio_file_output = 'conversion/text/'+f'{str(int(time()))}_transcription.json'
    with open(audio_file_input, 'rb') as audio_file:
        audio_recognition_response = json.loads(
            json.dumps(
                service.recognize(
                    audio=audio_file,
                    content_type='application/octet-stream').get_result(), indent=2))

    transcriptions = audio_recognition_response.get('results')[0]

    if transcriptions['final']:
        with open(audio_file_output, 'w+') as outfile:
            json.dump(transcriptions, outfile)

        return transcriptions['alternatives'][0]['transcript']
    else:
        return 0

