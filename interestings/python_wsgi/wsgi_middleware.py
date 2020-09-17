class Router(object):
    def __init__(self):
        self.path_info = {}

    def route(self, environ, start_response):
        application = self.path_info[environ['PATH_INFO']]
        return application(environ, start_response)

    def __call__(self, path):
        def wrapper(application):
            self.path_info[path] = application

        return wrapper


router = Router()


# here is the application
@router('/hello')  # 调用 route 实例，把函数注册到 PATH_INFO 字典
def hello(environ, start_response):
    status = '200 OK'
    output = b'Hello'
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]


@router('/world')
def world(environ, start_response):
    status = '200 OK'
    output = b'World!'
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]


from wsgiref.simple_server import make_server


def main():
    server = make_server('localhost', 8001, router.route)
    print('Serving HTTP on port 8001...')
    server.serve_forever()


if __name__ == '__main__':
    main()
