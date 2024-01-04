import requests


with requests.Session() as session:
    print(session.cookies.get_dict())  # {}

    headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    # Add more headers as needed
}

    response = session.get('http://google.com', headers=headers, cookies = {'CONSENT' : 'YES+'} )

    # {'AEC': 'Ad49MVGzf2rt5u6ObCPLjVzjrRqRMuYhCFG3iH7Ui8-banKZJ3dpZ_4wCA'}
    print(session.cookies.get_dict())