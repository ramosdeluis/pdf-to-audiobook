from audio import convert
from pdf import read_pdf


def make_audiobook(pdf_name, language, domain):
    pdf_text = read_pdf(pdf_name)
    print('Converting... Please, wait.')
    convert(
        text=pdf_text,
        filename=f'{pdf_name}_audiobook',
        language=language,
        domain=domain
    )
    print('Done, your audiobook is completed!')


if __name__ == '__main__':
    make_audiobook(
        pdf_name='Historias-Que-Acabam-Aqui',
        language='pt',
        domain='com.br'
    )
