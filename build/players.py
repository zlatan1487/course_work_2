
class Player:
    """
    Класс для хранения имя игрока и
    использованных им слов
    """

    def __init__(self, name):
        """
        инициализируем атрибуты:
        имя игрока/использованные слова (список)
        """
        self.name = name
        self.used_words = []

    def count_words_used(self):
        """
        метод возвращает количество использованных слов (возвращает int)
        """
        return len(self.used_words)

    def add_words_used(self, word):
        """
        метод добавление слова в использованные слова (ничего не возвращает)
        """
        self.used_words.append(word.strip())

    def checking_word_before(self, word):
        """
        метод проверки текущего слова,
        было ли использовано данное слово
        до этого (возвращает bool).
        """
        return word in self.used_words

    def __repr__(self):
        """
        строковый метод "__repr__" возвращает итоговое сообщение по статистики игры,
        в сообщении вызываеться метод "count_words_used" который возвращает количество правильных ответов.
        """
        print('')
        return f'Игра завершена, вы угадали {self.count_words_used()} слов'

