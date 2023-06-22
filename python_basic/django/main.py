# # django basic
# # urlib.request 모듈
# import urllib.request
# url = 'https://www.google.com'
#
# request = urllib.request.Request(url)
# response = urllib.request.urlopen(request)
#
# html = response.read()
# print(html)

#
# # urllib.request 모듈 실습
# import http.client
# from urllib.parse import urljoin, urlunparse
# from urllib.request import urlopen, urlretrieve
# from html.parser import HTMLParser
# from pathlib import Path
#
#
# class ImageParser(HTMLParser):
#     def __int__(self):
#         super().__init__()
#         self.result = []
#
#     def handle_starttag(self, tag, attrs):
#         if tag != 'img':
#             return
#         if not hasattr(self, 'result'):
#             self.result = []
#         for name, value in attrs:
#             if name == 'src':
#                 self.result.append(value)
#
#
# def parse_image(date):
#     parser = ImageParser()
#     parser.feed(date)
#     # set 에 담아서 중복을 제거
#     data_set = set(x for x in parser.result)
#     return data_set
#
#
# def download_image(url, data):
#     download_dir = Path('DOWNLOAD')
#     download_dir.mkdir(exist_ok=True)
#
#     parser = ImageParser()
#     parser.feed(data)
#     data_set = set(x for x in parser.result)
#     for x in sorted(data_set):
#         image_url = urljoin(url, x)
#         basename = Path(image_url).name
#         target_file = download_dir / basename
#         print(target_file)
#
#         print("Downloading...", image_url)
#         urlretrieve(image_url, target_file)
#
#
# def main():
#     url = 'https://google.com'
#     with urlopen(url) as f:
#         charset = f.headers.get_params('charset')[1][1]
#         data = f.read().decode(charset)
#
#     host = "www.google.com"
#     conn = http.client.HTTPConnection(host)
#     conn = request('GET', '')
#     resp = conn.getresponse()
#
#     charset = resp.msg.get_param('charset')
#     print('charset: ', charset)
#     data = resp.read().decode(charset)
#     conn.close()
#
#     data_set = parse_image(data)
#     print('\n>>>>> Fetch Images from', url)
#     print('\n'.join(sorted(data_set)))
#
#
# if __name__ == '__main__':
#     main()


# # http.client 모듈
# import http.client
# # 연결 설정
# conn = http.client.HTTPConnection('www.google.com')
# # 요청 보내기
# conn.request('GET', '/')
# # 응답 받기
# response = conn.getresponse()
# # 응답 출력
# print(response.read())
# # b'<!doctype html><html itemscope="" it ....


# # http.client 모듈 실습
# import http.client
# from urllib.parse import urljoin, urlunparse, urlencode
# from urllib.request import urlopen, urlretrieve
# from html.parser import HTMLParser
# from pathlib import Path
#
#
# class ImageParser(HTMLParser):
#     def __int__(self):
#         super().__init__()
#         self.result = []
#
#     def handle_starttag(self, tag, attrs):
#         if tag != 'img':
#             return
#
#         if not hasattr(self, 'result'):
#             self.result = []
#
#         for name, value in attrs:
#             if name == 'src':
#                 self.result.append(value)
#
#
# def parse_image(date):
#     parser = ImageParser()
#     parser.feed(date)
#     # set 에 담아서 중복을 제거
#     data_set = set(x for x in parser.result)
#     return data_set
#
#
# def download_image(url, data):
#     download_dir = Path('DOWNLOAD')
#     download_dir.mkdir(exist_ok=True)
#
#     parser = ImageParser()
#     parser.feed(data)
#     data_set = set(x for x in parser.result)
#
#     for x in sorted(data_set):
#         image_url = urljoin(url, x)
#         basename = Path(image_url).name
#         target_file = download_dir / basename
#         print(target_file)
#
#         print("Downloading...", image_url)
#         urlretrieve(image_url, target_file)
#
#     return data_set
#
#
# def main():
#     host = "www.google.com"
#     conn = http.client.HTTPConnection(host)
#     conn.request('GET', '')
#     resp = conn.getresponse()
#
#     charset = resp.msg.get_param('charset')
#     print('charset: ', charset)
#     data = resp.read().decode(charset)
#     conn.close()
#
#     data_set = parse_image(data)
#     print('\n>>>>> Downloading...', host)
#     url = urlunparse(('http', host, '', '', '', ''))
#     print('>>>>>', url)
#     download_image(url, data)
#
#
# if __name__ == '__main__':
#     main()


# # http.server 모듈
# from http.server import HTTPServer, BaseHTTPRequestHandler
#
# class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200, 'OK')
#         self.send_header('content-Type', 'text/plain')
#         self.end_headers()
#         self.wfile.write(b'Hellow World')
#
# server = HTTPServer(("", 8080), SimpleHTTPRequestHandler)
# # server = http.server.HTTPServer(("", 8080), SimpleHTTPRequestHandler)
# server.serve_forever()


# from wsgiref.simple_server import make_server
#
#
# def application(environ, start_response):
#     start_response_body = b"Hello,World!"
#     status = "200 OK"
#     headers = [("Content-Type", "text/plain")]
#
#     start_response(status, headers)
#     return [start_response_body]
#
#
# if __name__ == '__main__':
#     httpd = make_server("", 8000, application)
#     print("Running...")
#     httpd.serve_forever()
