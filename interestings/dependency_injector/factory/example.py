import dependency_injector.providers as providers

from interestings.dependency_injector.factory.games import Chess, Checkers, Ludo

game_factory = providers.FactoryAggregate(chess=providers.Factory(Chess),
                                          checkers=providers.Factory(Checkers),
                                          ludo=providers.Factory(Ludo))

if __name__ == '__main__':
    game_type = 'chess'
    player1 = 'yangkai'
    player2 = 'limei'

    selected_game = game_factory(game_type, player1, player2)
    selected_game.play()
    ludo = game_factory.ludo('niubi', 'shabi')
    ludo.play()

    # $ python example.py chess John Jane
    # John and Jane are playing chess
    #
    # $ python example.py checkers John Jane
    # John and Jane are playing checkers
    #
    # $ python example.py ludo John Jane
    # John and Jane are playing ludo
