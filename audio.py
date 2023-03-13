import gtts


def convert(text, filename, language='en', domain='us'):
    my_obj = gtts.gTTS(text=text, lang=language, tld=domain, slow=False)
    my_obj.save(f"audiobooks/{filename}.mp3")


if __name__ == '__main__':
    convert('Olá hahahahahah', "haha")
