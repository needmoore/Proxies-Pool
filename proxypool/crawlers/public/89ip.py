from pyquery import PyQuery as pq
from proxypool.schemas.proxy import Proxy
from proxypool.crawlers.base import BaseCrawler

# http://www.89ip.cn/index_31.html
BASEURL = 'http://www.89ip.cn/index_{page}.html'


class ENIP(BaseCrawler):
    urls = [BASEURL.format(page=page) for page in range(26)]

    def parse(self, html):
        doc = pq(html)
        trs = doc('div.layui-form > table > tbody > tr').items()

        for tr in trs:
            host = tr.find('td:nth-child(1)').text()
            port = int(tr.find('td:nth-child(2)').text())
            yield Proxy(host=host, port=port)


if __name__ == '__main__':
    crawler = ENIP()
    for proxy in crawler.crawl():
        print(proxy)
