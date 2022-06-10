import requests

MY_TOKEN = "5936eb83b91c1b682620510f32ec757656f358c3"


def request_word(word):
    header = {
        "Authorization": f"Token {MY_TOKEN}"
    }
    url = f"https://owlbot.info/api/v4/dictionary/{word}"
    print(url)
    response = requests.get(url=url, headers=header)
    response.raise_for_status()
    data = response.json()
    return data
