from aiohttp import web
import asyncio
import aiohttp

session = aiohttp.ClientSession()
methods = ['get', 'post', 'put', 'patch', 'head', 'delete']
base_url = 'http://localhost:8081/'

bad_word_list = [b"bad", b"test"]
hop_by_hop_headers = {"Connection",
                      "Keep-Alive",
                      "Proxy-Authenticate",
                      "Proxy-Authorization",
                      "TE",
                      "Trailers",
                      "Transfer-Encoding",
                      "Upgrade",
                      "Content-Length"}


async def handle(request: web.BaseRequest):
    method = request.method
    request_uri = request.match_info.get('request_uri', '/')
    body = await request.read()
    headers = request.headers
    async with aiohttp.ClientSession() as session:
        async with session.request(method=method, url=base_url+request_uri, data=body, headers=headers) as response:
            _body = await response.read()
            for word in bad_word_list:
                _body = _body.replace(word, b" ")
            status = response.status
            _headers = {}
            for header in response.headers:
                if not header in hop_by_hop_headers:
                    _headers[header] = response.headers[header]
            return web.Response(status=status, body=_body, headers=_headers)

app = web.Application()
app.add_routes([getattr(web, method)(
    r'/{request_uri:.*}', handle) for method in methods])

if __name__ == '__main__':
    web.run_app(app)
