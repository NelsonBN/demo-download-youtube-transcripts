import os
from youtube_transcript_api import YouTubeTranscriptApi


def download_transcript(id, language):
    return YouTubeTranscriptApi.get_transcript(
        video_id = id,
        languages = [language])


def extract_text(transcript):
    return '\n'.join([line['text'] for line in transcript])


def save_in_file(text, file_path):
    folder = os.path.dirname(file_path)
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


# video_id = 'zZgcoWJPYAY'
# language = 'en'

video_id = input('Enter the video id: ')
language = input('Enter the language: ')


transcript = download_transcript(video_id, language)
transcript = extract_text(transcript)
save_in_file(transcript, './.out/transcript.txt')
print(transcript)
