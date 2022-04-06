import argparse
import sqlite3 as sql
from random import choice


DB_NAME = 'codewars_tracking.db'
RAND_LIST = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]


def init_db(cur):
    cur.execute(
        'CREATE TABLE IF NOT EXISTS players '
        '(id text, name text, start int, curr int)'
    )


def add(cur, iden, name):
    print(f'Player "{iden}" has been registered with display name "{name}"')


def reset(cur, id):
    print(f'Player "{id}"\'s progress in this competition has be reset.')


def remove(cur, id):
    print(f'Player "{id}" has been removed.')


def reset_all(cur):
    # cuz making ppl type random stuff is fun
    random = ''.join(choice(RAND_LIST) for i in range(8))
    ans = input(
        'This will restart the competition tracking by syncing '
        'everyone\'s starting score to their current score.\nAre you sure?\n'
        f'Enter "{random}" to confirm: '
    )

    if ans != random:
        print('Confirmation message does not match. Aborting.')
        return

    print('bam')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Tools for manipulating the Codewars tracking process.'
    )

    subparsers = parser.add_subparsers(required=True, dest='action')

    init_parser = subparsers.add_parser('init', help='initializes a player')
    reset_parser = subparsers.add_parser(
        'resetAll',
        help='resets all player\'s score'
    )

    add_parser = subparsers.add_parser('add', help='adds a player')
    set_parser = subparsers.add_parser(
        'reset', help='resets the score of a player'
    )
    remove_parser = subparsers.add_parser('remove', help='removes a player')

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

    with sql.connect(DB_NAME) as con:
        cur = con.cursor()

        if args.action == 'init':
            init_db(cur)
        elif args.action == 'add':
            add(cur, args.id, args.name)
        elif args.action == 'reset':
            reset(cur, args.id)
        elif args.action == 'remove':
            remove(cur, args.id)
        elif args.action == 'resetAll':
            reset_all(cur)
