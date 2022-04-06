import argparse
import sqlite3 as sql


DB_NAME = 'codewars_tracking.db'


def init_db():
    with sql.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute('CREATE TABLE players (id text, name text, score int)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Tools for manipulating the Codewars tracking process.'
    )

    subparsers = parser.add_subparsers(required=True, dest='action')

    init_parser = subparsers.add_parser('init', help='initializes a player')
    add_parser = subparsers.add_parser('add', help='adds a player')
    set_parser = subparsers.add_parser(
        'reset', help='resets the score of a player'
    )
    remove_parser = subparsers.add_parser('remove', help='removes a player')
    reset_parser = subparsers.add_parser(
        'resetAll',
        help='resets all player\'s score'
    )

    id_params = {
        'dest': 'id',
        'type': str,
        'help': 'the player\'s Codewars ID'
    }

    add_parser.add_argument(**id_params)
    add_parser.add_argument(
        'name',
        type=str,
        help='the player\'s display name'
    )

    set_parser.add_argument(**id_params)
    remove_parser.add_argument(**id_params)

    args = parser.parse_args()


