#!/usr/bin/env python3

from http.client import HTTPConnection
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
#         print('start tag: ', tag, attrs)

        for data in attrs:
            if 'href' in data:
                self.hrefs.append(data)

    def handle_endtag(self, tag):
        pass
#         print('end tag: ', tag)

    def hanjle_data(self, data):

        pass
#         print('data: ', data)

    def get_hrefs(self):
        return self.hrefs



def main():
    answer_data = []


    url = 'www.asahi-net.or.jp'
    path = '/~kc7k-nd/onlispjhtml/'
    http_client = HTTPConnection(url)
#     print(http_client)

    http_client.request('GET', path)
    response = http_client.getresponse()
    response_html = response.readall().decode('UTF-8')
#     print(response_html)


    parser = MyHTMLParser()
    parser.feed(response_html)
#     parser = HTMLParser(strict=True)
#     parser.feed(response_html)
    hrefs = parser.get_hrefs()
    for h in hrefs:
#         print(h)
#         find_word(h[1], url, 'mappend')
        ret = find_word(path + h[1], url, 'mappend')
        for r in ret:
#             print(r)
            if r:
#                 for a in r:
                print(r)
#         print(ret)
#     print('path: ', path + hrefs[2][1], ', url: ', url)

    print()


class WordSearchHTMLParser(HTMLParser):
    def __init__(self, word):
        self.__search_word = word
        HTMLParser.__init__(self)
        self.__data = []

    def handle_data(self, data):
#         print(data)
        if self.__search_word in data:
#             print(data)
            self.__data.append(data)

    def get_data(self):
        return self.__data


def find_word(path, url, word):

    http_client = HTTPConnection(url)

    http_client.request('GET', path)

    response_html_text = http_client.getresponse().readall().decode('UTF-8')
#     print(response_html_text)

    wordparser = WordSearchHTMLParser(word)
    data = [path]
    wordparser.feed(response_html_text)
    data.append(wordparser.get_data())
#     WordSearchHTMLParser(word).get_data())
    return data

if __name__ == '__main__':
    main()

