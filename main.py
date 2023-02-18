# импорт реобходимых зависимостей
from build.utils import load_random_word, greetings
from build.players import Player
from build.requests_word import list_words


if __name__ == '__main__':

    player_name = input('Ввведите имя игрока ')

    # инициализация игрока
    player = Player(player_name.title())
    # инициализация словаря
    basic_words = load_random_word(list_words.json())

    # вызов функции с сообщением о начале игры/приветствие игрока
    print(greetings(player.name, basic_words))

    # для удобства тестирования игры (список подслов)/перед запуском раскомментировать)
    # print(basic_words.valid_sub_words)

    while set(player.used_words) != set(basic_words.valid_sub_words):
        print('')
        user_response = input('Ваш ответ...  ')

        # проверка ответа - соответствует ли ответ к возможным правильным словам из списка подслов
        checking_entered_word = basic_words.checking_entered_word(user_response)

        # проверка соответствия - на наличия верного слова в списке использованных слов
        checking_word_before = player.checking_word_before(user_response)

        if user_response == 'stop' or user_response == 'стоп':
            print(player)
            quit()
        elif 0 != len(user_response) < 3:
            print('Слишком короткое слово')
        elif checking_word_before:
            print('Уже использовано!')
        elif checking_entered_word:
            print('Верно')
            player.add_words_used(user_response)

        else:
            print('Неверно')

    # вызов строкового метода "__repl__" экземпляра класса "player" с сообщением о завершении и итогах игры
    print(player)







