def read_file(name):
    with open(name, 'r') as f:
        text = f.read()
    text = text.replace('\n', ' ').replace('\xa0–', '').replace('«', '').replace('»', '').replace('.', '').replace(',', '')\
        .lower()
    words = text.split(' ')
    unique_words = []
    for word in words:
        if word not in unique_words and word != '':
            unique_words.append(word)
    return sorted(unique_words)


def save_file(name, words_list):
    with open(name, 'w', encoding='UTF-8') as f:
        f.write(f'Всего уникальных слов: {len(words_list)}' + '\n')
        for word in words_list:
            f.write(word + '\n')


name = 'data.txt'
words = read_file(name=name)
print(words)
save_file('count.txt', words)
