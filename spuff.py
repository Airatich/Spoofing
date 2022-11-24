import requests
from bs4 import BeautifulSoup
from random import choice
import logging

logging.basicConfig(format='%(message)s', level=logging.INFO)


def get_html(url, useragent=None, proxy=None):
    print("Получаем html страницы")
    r = requests.get(url, headers=useragent, proxies=proxy)
    return r.text


def get_ip(html):
    print('New proxy and ua')
    soup = BeautifulSoup(html, 'lxml')
    ip = soup.find("span", class_="ip").text.strip()
    ua = soup.find("span", class_="ip").find_next_sibling("span").text.strip()

    start_param_ip = '<=== IP Received: {}'
    start_param_ua = '<=== UA Received: {}'
    logging.info(start_param_ip.format(ip))
    logging.info(start_param_ua.format(ua))
    # print(ip)
    # print(ua)



def main():
    url = "http://sitespy.ru/my-ip"
    user_agents = open("SeoLik_Список_desktop_user_agent.txt").read().split("\n")
    proxies = open("proxy.txt").read().split("\n")

    for i in range(10):
        p = choice(proxies)
        u = choice(user_agents)
        # proxy = {'http': "http://" + p}
        proxy = {'http': "http://" + p}
        useragent = {"User-Agent": u}
        start_param_ip = '===> IP Connection: {}'
        start_param_ua = '===> UA Connection: {}'
        logging.info(start_param_ip.format(proxy))
        logging.info(start_param_ua.format(u))

        html = get_html(url, useragent, proxy)
        if html:
            print("код страницы получен")
        get_ip(html)

main()
