import socket
import views
from setting import SERVER_HOST, SERVER_PORT

URLS = {
    '/': views.index,
    '/index': views.index,
}


def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return method, url


def generate_headers(method, url):
    if not method == 'GET':
        return 'HTTP/1.1 405 Method not allowed\n\n', 405

    if url not in URLS and not url.startswith('/static/'):
        return 'HTTP/1.1 404 Method not found\n\n', 404

    return 'HTTP/1.1 200 OK\n\n', 200


def generate_content(code, url):
    if code == 404:
        return views.not_found()
    if code == 405:
        return views.not_allowed()
    if url.startswith('/static/'):
        with open(url[1:]) as file:
            return file.read()

    return URLS[url]()


def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)
    return f'{headers}{body}'.encode()


def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)

        print(request)

        if request == b'':
            continue

        response = generate_response(request.decode('utf-8'))
        print(response)
        client_socket.sendall(response)
        client_socket.close()


if __name__ == '__main__':
    run_server()
