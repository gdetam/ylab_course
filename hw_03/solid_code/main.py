from heroes import ChackNorris, Superman

from news import NewsPaper, TV

from places import Kostroma, Tokyo

from save_place import SavePlace


if __name__ == '__main__':
    s = SavePlace(Superman(), Kostroma(), NewsPaper())
    s.save_the_place()
    print('-' * 20)
    s = SavePlace(ChackNorris(), Tokyo(), TV())
    s.save_the_place()
