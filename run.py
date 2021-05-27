from torrequest import TorRequest
import requests
import warnings

password = input("Enter your unhashed password for tor : ")
site = input("Enter your Site Address : ")
views = int(input("Enter The number of Viewers : "))
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77  Safari/537.36"
}
warnings.filterwarnings('ignore', message='Unverified HTTPS request')
response = requests.get('http://ipecho.net/plain')
print("My Original IP Address:", response.text)


def run():
    tr = TorRequest(password=password)
    tr.reset_identity()  # Reset Tor
    response = tr.get('http://ipecho.net/plain')
    rep = tr.get(site, headers=headers, verify=False)
    print("["+str(i)+"]" + " Blog View Added With IP:" + str(response.text))
    print(rep.status_code)


if __name__ == '__main__':
    for i in range(views):
        run()
