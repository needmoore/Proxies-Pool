from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler
from loguru import logger

BASEURL = 'http://www.66ip.cn/{page}.html'


class SixIp(BaseCrawler):
    urls = [BASEURL.format(page=page) for page in range(9)]

    @logger.catch()
    def parse(self, html):
        doc = pq(html)
        trs = doc('#main > div > div:nth-child(1) > table ').items()
        for tr in trs:
            host = tr.find('td:nth-child(1)').text()
            # port = int(tr.find('td:nth-child(2)').text())
            port = int(tr.find('td:nth-child(2)').text())
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = SixIp()
    for proxy in crawler.crawl():
        print(proxy)
