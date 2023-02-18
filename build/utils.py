# импорт реобходимых зависимостей
import random
from build.basic_word import BasicWord


def load_random_word(data_):
    """
    функция определяет случайное слово из словаря,
    создает экземпляр класса "BasicWord"
    :param data_: список слов с внешнего ресурса
    :return: созданный экземпляр класса "BasicWord"
    """
    random.shuffle(data_)
    word_list = None
    for item in data_:
        word = item['word']
        sub_words = item['sub_words']
        word_list = BasicWord(word, sub_words)

    return word_list


def greetings(player, basic_words):
    """
    вспомогательная функция, выводит в консоль приветственное сообщение
    :param player: имя игрока
    :param basic_words: экземпляр класса "BasicWord"
    :return: сообщение в консоль
    """
    if len(player) == 0:
        player = 'Unknown player'
    return f'Привет, {player}!''\n' \
           f'Составьте {basic_words.count_sub_words()} слов из слова {basic_words.original_word}''\n'\
           f'Слова должны быть не короче 3 букв''\n' \
           f'Чтобы закончить игру, угадайте все слова или напишите "stop"''\n' \
           f'Поехали, ваше первое слово?'



