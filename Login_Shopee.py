import requests
import hashlib


def encrypt_password(password):
    password = hashlib.md5(password.encode()).hexdigest()
    password = hashlib.sha256(password.encode()).hexdigest()
    return password


def login_shopee():
    payload = {
        'password_hash': encrypt_password("545724HaHa"),
        'username': 'hung7698',
        'vcode': ''
    }
    url = "https://banhang.shopee.vn/api/v2/login"
    with requests.Session() as s:
        p = s.post(url, data=payload)
        if p.status_code == requests.codes.ok:
            r = s.get('https://shopee.vn/cart')
            print(r.text)
        else:
            payload['vcode'] = input("Nhập mã: ")
            p = s.post(url, data=payload)
            print(p.text)
        x = s.get("https://shopee.vn/api/v2/user/profile/get/")
        print(x.content)


if __name__ == '__main__':
    login_shopee()

    # https://shopee.vn/api/v2/search_items/?by=relevancy&keyword=qu%E1%BA%A7n&limit=50&newest=0&official_mall=1&order=desc&page_type=search&version=2
