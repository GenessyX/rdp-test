1. Запустить docker-compose.

```
docker-compose up
```

2. Перейти в контейнер клиента и сделать запрос.

```
docker-compose exec client /bin/sh
curl 192.168.255.2/bad
```

Ожидаемый вывод:

```json
{
  "host": {
    "hostname": "192.168.255.2",
    "ip": "::ffff:192.168.255.4",
    "ips": []
  },
  "http": {
    "method": "GET",
    "baseUrl": "",
    "originalUrl": "/bad",
    "protocol": "http"
  },
  "request": {
    "params": {
      "0": "/bad"
    },
    "query": {},
    "cookies": {},
    "body": {},
    "headers": {
      "host": "192.168.255.2",
      "user-agent": "curl/7.74.0",
      "accept": "*/*"
    }
  },
  "environment": {
    "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    "HOSTNAME": "3b3c6c6829e0",
    "NODE_VERSION": "16.16.0",
    "YARN_VERSION": "1.22.19",
    "HOME": "/root"
  }
```

Полученный результат:

```json
{
  "host": {
    "hostname": "192.168.255.2",
    "ip": "::ffff:192.168.255.4",
    "ips": []
  },
  "http": {
    "method": "GET",
    "baseUrl": "",
    "originalUrl": "/ ",
    "protocol": "http"
  },
  "request": {
    "params": {
      "0": "/ "
    },
    "query": {},
    "cookies": {},
    "body": {},
    "headers": {
      "host": "192.168.255.2",
      "user-agent": "curl/7.85.0-DEV",
      "accept": "*/*",
      "accept-encoding": "gzip, deflate",
      "content-length": "0",
      "content-type": "application/octet-stream"
    }
  },
  "environment": {
    "PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
    "HOSTNAME": "3b3c6c6829e0",
    "NODE_VERSION": "16.16.0",
    "YARN_VERSION": "1.22.19",
    "HOME": "/root"
  }
}
```
