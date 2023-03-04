from django import template

register = template.Library()

OBSCENE_WORDS = [
    "Здесь будет список нецензурных слов"
]


@register.filter(name='censor')
def censor(text: str):
    if type(text) is not str:
        raise ValueError('censor filter only accepts str values')

    for word in OBSCENE_WORDS:
        text = text.replace(word, f'{word[0]}{"*"*(len(word)-1)}')
        word = word.title()
        text = text.replace(word, f'{word[0]}{"*"*(len(word)-1)}')
    return text
