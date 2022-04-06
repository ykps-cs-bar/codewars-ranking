import argparse
import sqlite3 as sql
from random import choice

from scrap import get_user_score


DB_NAME = 'codewars_tracking.db'
RAND_LIST = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]


def get_score(iden):
    score_data = get_user_score(iden)

    if not score_data['valid']:
        code = score_data['code']
        print(f'Error Code: {code}')
        exit()

    return score_data['score']


def init_db(cur):
    cur.execute(
        'CREATE TABLE Players '
        '(ID text PRIMARY KEY, Name text, Start int, Curr int) WITHOUT ROWID'
    )


def add(cur, iden, name):
    score = get_score(iden)
    cur.execute(
        'INSERT INTO Players '
        '(ID, Name, Start, Curr) '
        f"VALUES('{iden}', '{name}', {score}, {score})"
    )
    print(f'Player "{iden}" has been registered with display name "{name}"')
    print(f'Starting score: {score}')


def reset(cur, iden):
    score = get_score(iden)
    cur.execute(
        'UPDATE Players '
        f'SET Start = {score}, Curr = {score} '
        f"WHERE ID = '{iden}'"
    )
    print(f'Player "{iden}"\'s progress in this competition has be reset.')
    print(f'New starting score: {score}')


def remove(cur, iden):
    cur.execute(f"DELETE FROM Players WHERE ID = '{iden}'")
    print(f'Player "{iden}" has been removed.')


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

    ids = [i[0] for i in cur.execute('SELECT ID FROM Players').fetchall()]

    for i in ids:
        reset(cur, i)


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
