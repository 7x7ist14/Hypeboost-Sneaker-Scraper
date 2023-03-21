import json
import requests
from bs4 import BeautifulSoup


def hypeboost_product_url(SKU):
    url = "https://hypeboost.com/en/search/shop?keyword=" + SKU
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    for a in soup.find_all('a', href=True):
        print("Product URL:", a['href'])
    url2 = a['href']
    return url2


def hypeboost_prices(SKU):
    url = hypeboost_product_url(SKU)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    sizes = soup.find_all('div', class_='size')
    output = ""

    for size in sizes:
        label = size.find('div', class_='label').text.strip()
        if 'data-price' in size.attrs:
            price = size['data-price']
            price = price.replace('\xa0', '')
            price = price.replace(' ', '')
            price = price.replace('€', '') + '€'
        else:
            price = 'OOS!'
        output += label.replace(' ', '') + ': ' + price + "\n"
    print("Scraped Payout Prices!")
    return output
#print(hypeboost_prices("DV3742-021"))

def hypeboost_product_title(SKU):
  hypeboost_product_url_r = hypeboost_product_url(SKU)
  headers = {
      "cookie": "country=eyJpdiI6ImlCRDJaRExPQkZYNTNlMmM0OWFEQVE9PSIsInZhbHVlIjoiTFRaRW01UW5wNUY2RjZnQzViWGlPYWRtYVRmbmxxMXpoRjNzODlZZUdIZmNLWjZSTFp0Q3htbTFuYUF4ZGkwVSIsIm1hYyI6IjQ0MzBlZTdkZmNhYjVhYmJhMDAzNDhlNjQ3MGU5NzQ1YThkOTk0ZDRkNzYxZGQzYzg0ODI0ZWYzZWZhODBlZGYiLCJ0YWciOiIifQ%253D%253D; currency=eyJpdiI6ImFlbkxaNHJyOHdUZlJFRlJ2dGlna0E9PSIsInZhbHVlIjoieEx2OE01VHhzOGZ1eFdsM09IVDFIZmR6R1hieHpDRDZScWoweVhqTDZjUzY2a3FFUmhQZGdPV2piaFN3OTViTCIsIm1hYyI6IjgzMTY0NDExNzljYjM1MzFmZmM5ZTBhOGY0MjU3ZWViMjA2NjBjYmUwMjg0MDFkMmUyYmJiNTVjYTUxZTk5MjMiLCJ0YWciOiIifQ%253D%253D",
      "Content-Type": "application/json"
  }
  response = requests.request("GET", hypeboost_product_url_r, headers=headers)
  soup = BeautifulSoup(response.content, 'html.parser')
  title = soup.find('h1')
  title_text = title.get_text()
  print('Scraped Product title!')
  return title_text

def stockx_url(SKU):
  url = "https://stockx.com/api/browse?_search=" + SKU

  headers = {
          'accept': 'application/json',
          'accept-encoding': 'utf-8',
          'accept-language': 'en-DE',
          'app-platform': 'Iron',
          'referer': 'https://stockx.com/en-DE',
          'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
          'x-requested-with': 'XMLHttpRequest'
      }

  request1 = requests.get(url=url, headers=headers)

  product_id = json.loads(request1.text)
  product_id_final = product_id['Products'][0]['id']

  ID = product_id_final
  url_stockX = "https://stockx.com/" + ID
  print("Scraped StockX URL: " + url_stockX)
  return url_stockX

def restocks_url(SKU):
  base_url = 'https://restocks.net/de/shop/search?q='
  request_url = base_url + SKU + '&page=1&filters[0][range][price][gte]=1'

  r = requests.get(request_url)

  json_restocks = json.loads(r.text)
  product_url = json_restocks["data"][0]['slug']
  print('Scraped Restocks URL: ' + product_url)
  return product_url


def product_picture(SKU):
  hypeboost_product_url_output = hypeboost_product_url(SKU)
  headers = {
      "cookie": "country=eyJpdiI6ImlCRDJaRExPQkZYNTNlMmM0OWFEQVE9PSIsInZhbHVlIjoiTFRaRW01UW5wNUY2RjZnQzViWGlPYWRtYVRmbmxxMXpoRjNzODlZZUdIZmNLWjZSTFp0Q3htbTFuYUF4ZGkwVSIsIm1hYyI6IjQ0MzBlZTdkZmNhYjVhYmJhMDAzNDhlNjQ3MGU5NzQ1YThkOTk0ZDRkNzYxZGQzYzg0ODI0ZWYzZWZhODBlZGYiLCJ0YWciOiIifQ%253D%253D; currency=eyJpdiI6ImFlbkxaNHJyOHdUZlJFRlJ2dGlna0E9PSIsInZhbHVlIjoieEx2OE01VHhzOGZ1eFdsM09IVDFIZmR6R1hieHpDRDZScWoweVhqTDZjUzY2a3FFUmhQZGdPV2piaFN3OTViTCIsIm1hYyI6IjgzMTY0NDExNzljYjM1MzFmZmM5ZTBhOGY0MjU3ZWViMjA2NjBjYmUwMjg0MDFkMmUyYmJiNTVjYTUxZTk5MjMiLCJ0YWciOiIifQ%253D%253D",
      "Content-Type": "application/json"
  }
  response = requests.request("GET", hypeboost_product_url_output, headers=headers)
  soup = BeautifulSoup(response.content, 'html.parser')

  pictures = soup.find("div", class_ = "item")
  image = pictures.find_all('img')[0].get('src')

  print('Scraped image!')
  return image


def product_goat(SKU):
  url = "https://ac.cnstrc.com/search/" + SKU
  querystring = {"c":"ciojs-client-2.29.12","key":"key_XT7bjdbvjgECO5d8","i":"f8b0a5f2-bc6b-4626-b980-74bbc3b45edf","s":"1","num_results_per_page":"25","_dt":"1678011980760"}

  payload = ""
  headers = {
      "authority": "ac.cnstrc.com",
      "accept": "*/*",
      "accept-language": "en-DE,en;q=0.9",
      "origin": "https://www.goat.com",
      "sec-ch-ua": "^\^Chromium^^;v=^\^110^^, ^\^Not",
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": "^\^Windows^^",
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "cross-site",
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
  }

  response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
  output = json.loads(response.text)
  output_slug = output['response']['results'][0]['data']['slug']
  product_url = "https://www.goat.com/sneakers/" + output_slug
  print("Scraped GOAT product URL!")
  return product_url
