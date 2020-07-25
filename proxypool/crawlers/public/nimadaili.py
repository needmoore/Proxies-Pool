# from proxypool.crawlers.base import BaseCrawler
# from proxypool.schemas.proxy import Proxy
# from pyquery import PyQuery as pq
#
# # http://www.nimadaili.com/gaoni/11/
# # http://www.nimadaili.com/gaoni/500/
# BASEURL = 'http://www.nimadaili.com/gaoni/{page}/'
#
#
# class Nimadaili(BaseCrawler):
#     urls = [BASEURL.format(page=page) for page in range(2001)]
#
#     def parse(self, html):
#         doc = pq(html)
#         trs = doc('body > div > div:nth-child(2) > div > table  tr').items()
#         for tr in trs:
#             host = tr.find('td:nth-child(1)').text()
#             port = int(tr.find('td:nth-child(2)').text())
#             yield Proxy(host=host, port=port)
#
#
# if __name__ == '__main__':
#     crawler = Nimadaili()
#     for proxy in crawler.crawl():
#         print(proxy)
