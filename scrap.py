from requests import get


URL = 'https://www.codewars.com/api/v1/users/{}'


def get_user_score(user_id):
    resp = get(URL.format(user_id))

    if resp.status_code == 200:
        return {
            'valid': True,
            'score': resp.json()['ranks']['overall']['score']
        }

    return {'valid': False, 'code': resp.status_code}
