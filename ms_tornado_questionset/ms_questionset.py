import tornado.ioloop
import tornado.web

# import application
from ms_tornado_questionset.application.application_context import ApplicationContext


def setup_server():

    application_context = ApplicationContext()
    return application_context


if __name__ == "__main__":
    app = setup_server()
    app.listen(8001)
    tornado.ioloop.IOLoop.current().start()
