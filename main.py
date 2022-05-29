import pdfplumber
from art import text2art
from pathlib import Path
from gtts import gTTS


def pdf_to_mp3(filepath='test.pdf', language='en'):

    if Path(filepath).is_file():
        filename = input('Write new name of mp3 file: ')

        print('[+] Starting, please wait...')
        with pdfplumber.open(filepath) as pdf:
            text = [page.extract_text() for page in pdf.pages]
        text = ''.join(text)
        text = text.replace('\n', '')

        tts = gTTS(text=text, lang=language)
        tts.save(filename + '.mp3')

        print(f"[+] File '{filename}.mp3' created!")
    else:
        print('[!] File not exist, check the file path.')

    print('[+] Closing...')


def main():
    print_art = text2art('PDF-to-MP3')
    print(print_art)
    filepath = input('Write filepath: ')
    language = input('Write language(for example: "ru", "en"): ')
    print()

    pdf_to_mp3(filepath=filepath, language=language)


if __name__ == '__main__':
    main()
