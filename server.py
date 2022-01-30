from spyne import Application, rpc, ServiceBase, Integer, Iterable

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from math import isqrt


class matematica(ServiceBase):

    @rpc(Integer, _returns=Iterable(Integer))
    def crivo_eratostenes(ctx, n):
        if n <= 2:
            return []
        
        primos = [True] * n
        primos[0] = False
        primos[1] = False

        for i in range(2, isqrt(n)):
            if primos[i]:
                for x in range(i*i, n, i):
                    primos[x] = False
        
        return [i for i in range(n) if primos[i]]

        

    @rpc(Integer, _returns=Iterable(Integer))
    def fibonacci(ctx, n):

        if n == 0:
            return[0]
        if n == 1:
            return[0, 1]
        
        nums = [0,1]

        for i in range(n - 2):
            nums.append(nums[-1] + nums[-2])
        
        return nums
    
        




application = Application([matematica], 'soaps',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    import logging

    from wsgiref.simple_server import make_server

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("listening to http://127.0.0.1:8000")
    logging.info("wsdl is at: http://localhost:8000/?wsdl")

    server = make_server('127.0.0.1', 8000, wsgi_application)
    server.serve_forever()