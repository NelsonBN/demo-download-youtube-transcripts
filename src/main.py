import os
from youtube_transcript_api import YouTubeTranscriptApi
from easygoogletranslate import EasyGoogleTranslate


def download_transcript(id, language):
    return YouTubeTranscriptApi.get_transcript(
        video_id = id,
        languages = [language])


def extract_text(transcript):
    return '\n'.join([line['text'] for line in transcript])


def translate_text(source, target, text):
    return EasyGoogleTranslate(
        source_language = source,
        target_language = target
    ).translate(text)


def save_in_file(text, file_path):
    folder = os.path.dirname(file_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


# video_id = 'zZgcoWJPYAY'
# source_language = 'en'
# target_language = 'pt'


video_id = input('Enter the video id: ')
source_language = input('Enter the source language: ')
target_language = input('Enter the target language: ')


transcript = download_transcript(video_id, source_language)
transcript = extract_text(transcript)
save_in_file(transcript, f'./.out/transcript-{source_language}.txt')
print('Transcript:')
print(transcript)


translation = translate_text(source_language, target_language, transcript)
save_in_file(translation, f'./.out/transcript-{target_language}.txt')
print('Translation:')
print(translation)
