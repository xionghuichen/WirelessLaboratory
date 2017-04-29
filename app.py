INFO:root:ap is /home/burningbear/WirelessLaboratory/Application_service/
INFO:root:start server.
INFO:root:connect mysql ..
INFO:root:connect mongodb ..
INFO:root:connect mongodb successfully..
INFO:root:varcode url is http://127.0.0.1:10000/v1.0/barcode
INFO:root:resource url is http://127.0.0.1:10003/v1.0/resource
INFO:root:start completed..
INFO:tornado.access:304 GET /v1.0/service/web/main (223.3.96.196) 4.85ms
WARNING:tornado.access:404 GET /v1.0/service/web/v3/default3.jpg (223.3.96.196) 0.52ms
INFO:tornado.access:304 GET /v1.0/service/web/main (223.3.96.196) 0.57ms
WARNING:tornado.access:404 GET /v1.0/service/web/v3/default3.jpg (223.3.96.196) 0.45ms
INFO:tornado.access:304 GET /v1.0/service/web/main (223.3.73.169) 0.72ms
WARNING:tornado.access:404 GET /v1.0/service/web/v3/default3.jpg (223.3.73.169) 0.42ms
INFO:root:in recognize, upload is HTTPServerRequest(protocol='http', host='139.196.207.155:10001', method='POST', uri='/v1.0/service/hololens/upload', version='HTTP/1.1', remote_ip='223.3.73.169', headers={'Origin': 'http://139.196.207.155:10001', 'Content-Length': '10536455', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Host': '139.196.207.155:10001', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36', 'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest', 'Referer': 'http://139.196.207.155:10001/v1.0/service/web/main', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryYUGK4hyU0Pn8xLWs'})
INFO:root:in get b64 encode
INFO:root:in get oss key
ERROR:tornado.application:Uncaught exception POST /v1.0/service/hololens/upload (223.3.73.169)
HTTPServerRequest(protocol='http', host='139.196.207.155:10001', method='POST', uri='/v1.0/service/hololens/upload', version='HTTP/1.1', remote_ip='223.3.73.169', headers={'Origin': 'http://139.196.207.155:10001', 'Content-Length': '10536455', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Host': '139.196.207.155:10001', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36', 'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest', 'Referer': 'http://139.196.207.155:10001/v1.0/service/web/main', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryYUGK4hyU0Pn8xLWs'})
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/tornado/web.py", line 1425, in _stack_context_handle_exception
    raise_exc_info((type, value, traceback))
  File "/usr/local/lib/python2.7/dist-packages/tornado/stack_context.py", line 314, in wrapped
    ret = fn(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/tornado/gen.py", line 199, in final_callback
    if future.result() is not None:
  File "/usr/local/lib/python2.7/dist-packages/tornado/concurrent.py", line 237, in result
    raise_exc_info(self._exc_info)
  File "/usr/local/lib/python2.7/dist-packages/tornado/gen.py", line 285, in wrapper
    yielded = next(result)
  File "/home/burningbear/WirelessLaboratory/Application_service/Handler/Hololens/Recognize.py", line 49, in post
    res = self.big_requester(self.resource_service+'/project/post',data)
  File "/home/burningbear/WirelessLaboratory/Application_service/Handler/Hololens/Base.py", line 101, in big_requester
    res = requests.post(url, params=data)
  File "/usr/lib/python2.7/dist-packages/requests/api.py", line 88, in post
    return request('post', url, data=data, **kwargs)
  File "/usr/lib/python2.7/dist-packages/requests/api.py", line 44, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 421, in request
    prep = self.prepare_request(req)
  File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 359, in prepare_request
    hooks=merge_hooks(request.hooks, self.hooks),
  File "/usr/lib/python2.7/dist-packages/requests/models.py", line 287, in prepare
    self.prepare_url(url, params)
  File "/usr/lib/python2.7/dist-packages/requests/models.py", line 373, in prepare_url
    enc_params = self._encode_params(params)
  File "/usr/lib/python2.7/dist-packages/requests/models.py", line 86, in _encode_params
    return urlencode(result, doseq=True)
  File "/usr/lib/python2.7/urllib.py", line 1338, in urlencode
    v = quote_plus(v)
  File "/usr/lib/python2.7/urllib.py", line 1295, in quote_plus
    return quote(s, safe)
  File "/usr/lib/python2.7/urllib.py", line 1288, in quote
    return ''.join(map(quoter, s))
MemoryError
ERROR:tornado.access:500 POST /v1.0/service/hololens/upload (223.3.73.169) 6852.03ms
INFO:tornado.access:304 GET /v1.0/service/web/main (223.3.73.169) 0.98ms
WARNING:tornado.access:404 GET /v1.0/service/web/v3/default3.jpg (223.3.73.169) 0.38ms
INFO:root:in recognize, upload is HTTPServerRequest(protocol='http', host='139.196.207.155:10001', method='POST', uri='/v1.0/service/hololens/upload', version='HTTP/1.1', remote_ip='223.3.73.169', headers={'Origin': 'http://139.196.207.155:10001', 'Content-Length': '10536455', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Host': '139.196.207.155:10001', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36', 'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest', 'Referer': 'http://139.196.207.155:10001/v1.0/service/web/main', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7AK7eTKDZB1rGsLS'})
INFO:root:in get b64 encode
INFO:root:in get oss key
ERROR:tornado.application:Uncaught exception POST /v1.0/service/hololens/upload (223.3.73.169)
HTTPServerRequest(protocol='http', host='139.196.207.155:10001', method='POST', uri='/v1.0/service/hololens/upload', version='HTTP/1.1', remote_ip='223.3.73.169', headers={'Origin': 'http://139.196.207.155:10001', 'Content-Length': '10536455', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Host': '139.196.207.155:10001', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36', 'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest', 'Referer': 'http://139.196.207.155:10001/v1.0/service/web/main', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7AK7eTKDZB1rGsLS'})
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/tornado/web.py", line 1425, in _stack_context_handle_exception
    raise_exc_info((type, value, traceback))
  File "/usr/local/lib/python2.7/dist-packages/tornado/stack_context.py", line 314, in wrapped
    ret = fn(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/tornado/gen.py", line 199, in final_callback
    if future.result() is not None:
  File "/usr/local/lib/python2.7/dist-packages/tornado/concurrent.py", line 237, in result
    raise_exc_info(self._exc_info)
  File "/usr/local/lib/python2.7/dist-packages/tornado/gen.py", line 285, in wrapper
    yielded = next(result)
  File "/home/burningbear/WirelessLaboratory/Application_service/Handler/Hololens/Recognize.py", line 49, in post
    res = self.big_requester(self.resource_service+'/project/post',data)
  File "/home/burningbear/WirelessLaboratory/Application_service/Handler/Hololens/Base.py", line 101, in big_requester
    res = requests.post(url, params=data)
  File "/usr/lib/python2.7/dist-packages/requests/api.py", line 88, in post
    return request('post', url, data=data, **kwargs)
  File "/usr/lib/python2.7/dist-packages/requests/api.py", line 44, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 421, in request
    prep = self.prepare_request(req)
  File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 359, in prepare_request
    hooks=merge_hooks(request.hooks, self.hooks),
  File "/usr/lib/python2.7/dist-packages/requests/models.py", line 287, in prepare
    self.prepare_url(url, params)
  File "/usr/lib/python2.7/dist-packages/requests/models.py", line 373, in prepare_url
    enc_params = self._encode_params(params)
  File "/usr/lib/python2.7/dist-packages/requests/models.py", line 86, in _encode_params
    return urlencode(result, doseq=True)
  File "/usr/lib/python2.7/urllib.py", line 1338, in urlencode
    v = quote_plus(v)
  File "/usr/lib/python2.7/urllib.py", line 1295, in quote_plus
    return quote(s, safe)
  File "/usr/lib/python2.7/urllib.py", line 1288, in quote
    return ''.join(map(quoter, s))
MemoryError
ERROR:tornado.access:500 POST /v1.0/service/hololens/upload (223.3.73.169) 7066.01ms
WARNING:tornado.access:404 GET /web/index (223.3.96.196) 0.41ms
INFO:tornado.access:304 GET /v1.0/service/web/main (223.3.96.196) 0.95ms
WARNING:tornado.access:404 GET /v1.0/service/web/v3/default3.jpg (223.3.96.196) 0.33ms
INFO:root:in recognize, upload is HTTPServerRequest(protocol='http', host='139.196.207.155:10001', method='POST', uri='/v1.0/service/hololens/upload', version='HTTP/1.1', remote_ip='223.3.96.196', headers={'Origin': 'http://139.196.207.155:10001', 'Content-Length': '22028', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Host': '139.196.207.155:10001', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36', 'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest', 'Referer': 'http://139.196.207.155:10001/v1.0/service/web/main', 'Cookie': '_xsrf=2|382f81e3|013dd420c6a8166ef06c8447ce4a924c|1492578250', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryGvm1XtxZatky8Svu'})
INFO:root:in get b64 encode
INFO:root:in get oss key
INFO:urllib3.connectionpool:Starting new HTTP connection (1): 127.0.0.1
INFO:root:{"message": "success", "code": 0, "data": {"key": "1:12017-04-19 13:12:07.0317211.txt"}}
INFO:root:res type <type 'unicode'>
INFO:root:1:12017-04-19 13:12:07.0317211.txt
INFO:root:in bracode pirc
INFO:root:response.body is {"message": "default message", "code": 0, "data": {"key": "1:12017-04-19 13:12:07.441467.png"}}
INFO:root:in get url
INFO:root:response.body is {"message": "default message", "code": 0, "data": {"url": "http://imgcuphololens.oss-cn-shanghai.aliyuncs.com/1%3A12017-04-19%2013%3A12%3A07.441467.png?OSSAccessKeyId=LTAIkY3jD1E5hu8z&Expires=1492582327&Signature=WxZOrp89%2F5j2Y5q7y1tIETxG0SI%3D"}}
INFO:tornado.access:200 POST /v1.0/service/hololens/upload (223.3.96.196) 585.58ms
INFO:tornado.access:200 GET /v1.0/service/web/main (223.3.73.169) 0.67ms
WARNING:tornado.access:404 GET /v1.0/service/web/v3/default3.jpg (223.3.73.169) 0.38ms
INFO:tornado.access:200 GET /static/js/bootstrap.min.js?v=5869c96cc8f19086aee625d670d741f9 (223.3.73.169) 47.18ms
INFO:root:in recognize, upload is HTTPServerRequest(protocol='http', host='139.196.207.155:10001', method='POST', uri='/v1.0/service/hololens/upload', version='HTTP/1.1', remote_ip='223.3.96.196', headers={'Origin': 'http://139.196.207.155:10001', 'Content-Length': '218931', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Host': '139.196.207.155:10001', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36', 'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest', 'Referer': 'http://139.196.207.155:10001/v1.0/service/web/main', 'Cookie': '_xsrf=2|382f81e3|013dd420c6a8166ef06c8447ce4a924c|1492578250', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarybDzOzXAOAfU8CanH'})
INFO:root:in get b64 encode
INFO:root:in get oss key
INFO:urllib3.connectionpool:Starting new HTTP connection (1): 127.0.0.1
INFO:root:{"message": "success", "code": 0, "data": {"key": "1:12017-04-19 13:19:05.409395nicola3.en.pdf"}}
INFO:root:res type <type 'unicode'>
INFO:root:1:12017-04-19 13:19:05.409395nicola3.en.pdf
INFO:root:in bracode pirc
INFO:root:response.body is {"message": "default message", "code": 0, "data": {"key": "1:12017-04-19 13:19:05.550927.png"}}
INFO:root:in get url
INFO:root:response.body is {"message": "default message", "code": 0, "data": {"url": "http://imgcuphololens.oss-cn-shanghai.aliyuncs.com/1%3A12017-04-19%2013%3A19%3A05.550927.png?OSSAccessKeyId=LTAIkY3jD1E5hu8z&Expires=1492582745&Signature=EsAaiFP0kadwbyatxxBytgf11U4%3D"}}
INFO:tornado.access:200 POST /v1.0/service/hololens/upload (223.3.96.196) 1352.28ms
INFO:root:in recognize, upload is HTTPServerRequest(protocol='http', host='139.196.207.155:10001', method='POST', uri='/v1.0/service/hololens/upload', version='HTTP/1.1', remote_ip='223.3.96.196', headers={'Origin': 'http://139.196.207.155:10001', 'Content-Length': '10536455', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Host': '139.196.207.155:10001', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36', 'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest', 'Referer': 'http://139.196.207.155:10001/v1.0/service/web/main', 'Cookie': '_xsrf=2|382f81e3|013dd420c6a8166ef06c8447ce4a924c|1492578250', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryuTN4sQWwVSq5tMxY'})
INFO:root:in get b64 encode
INFO:root:in get oss key
ERROR:tornado.application:Uncaught exception POST /v1.0/service/hololens/upload (223.3.96.196)
HTTPServerRequest(protocol='http', host='139.196.207.155:10001', method='POST', uri='/v1.0/service/hololens/upload', version='HTTP/1.1', remote_ip='223.3.96.196', headers={'Origin': 'http://139.196.207.155:10001', 'Content-Length': '10536455', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Host': '139.196.207.155:10001', 'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36', 'Connection': 'keep-alive', 'X-Requested-With': 'XMLHttpRequest', 'Referer': 'http://139.196.207.155:10001/v1.0/service/web/main', 'Cookie': '_xsrf=2|382f81e3|013dd420c6a8166ef06c8447ce4a924c|1492578250', 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryuTN4sQWwVSq5tMxY'})
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/tornado/web.py", line 1425, in _stack_context_handle_exception
    raise_exc_info((type, value, traceback))
  File "/usr/local/lib/python2.7/dist-packages/tornado/stack_context.py", line 314, in wrapped
    ret = fn(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/tornado/gen.py", line 199, in final_callback
    if future.result() is not None:
  File "/usr/local/lib/python2.7/dist-packages/tornado/concurrent.py", line 237, in result
    raise_exc_info(self._exc_info)
  File "/usr/local/lib/python2.7/dist-packages/tornado/gen.py", line 285, in wrapper
    yielded = next(result)
  File "/home/burningbear/WirelessLaboratory/Application_service/Handler/Hololens/Recognize.py", line 49, in post
    res = self.big_requester(self.resource_service+'/project/post',data)
  File "/home/burningbear/WirelessLaboratory/Application_service/Handler/Hololens/Base.py", line 101, in big_requester
    res = requests.post(url, params=data)
  File "/usr/lib/python2.7/dist-packages/requests/api.py", line 88, in post
    return request('post', url, data=data, **kwargs)
  File "/usr/lib/python2.7/dist-packages/requests/api.py", line 44, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 421, in request
    prep = self.prepare_request(req)
  File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 359, in prepare_request
    hooks=merge_hooks(request.hooks, self.hooks),
  File "/usr/lib/python2.7/dist-packages/requests/models.py", line 287, in prepare
    self.prepare_url(url, params)
  File "/usr/lib/python2.7/dist-packages/requests/models.py", line 373, in prepare_url
    enc_params = self._encode_params(params)
  File "/usr/lib/python2.7/dist-packages/requests/models.py", line 86, in _encode_params
    return urlencode(result, doseq=True)
  File "/usr/lib/python2.7/urllib.py", line 1338, in urlencode
    v = quote_plus(v)
  File "/usr/lib/python2.7/urllib.py", line 1295, in quote_plus
    return quote(s, safe)
  File "/usr/lib/python2.7/urllib.py", line 1288, in quote
    return ''.join(map(quoter, s))
MemoryError
ERROR:tornado.access:500 POST /v1.0/service/hololens/upload (223.3.96.196) 15699.77ms
