unique_word = set()


def counter():
    phrase = input('Digite uma frase:')
    words = phrase.lower().split()

    for word in words:
        word = word.strip('.,!?;:')
        unique_word.add(word)


counter()
print(f"Quantidade de palavras unicas: {len(unique_word)}")