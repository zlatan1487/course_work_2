
class BasicWord:
    """
    Класс для определения исходного слова и подслов,
    которые можно составить из исх.слова
    """

    def __init__(self, original_word, valid_sub_words):
        """
        инициализируем атрибуты, исходное слово и набор допустимых подслов
        """
        self.original_word = original_word
        self.valid_sub_words = valid_sub_words

    def checking_entered_word(self, word):
        """
        метод возвращает булевое значение
        в зависимости от имеющего слова в списке подслов

        :param word:
        :return: возвращает True, если оно есть
        """
        return word in self.valid_sub_words

    def count_sub_words(self):
        """
        метод возвращает количество подслов (вернет int)
        """
        return len(self.valid_sub_words)


