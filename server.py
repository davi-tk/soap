from spyne import Application, rpc, ServiceBase, Integer, Iterable

from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from math import isqrt


'''
Service base é uma classe base que define o webservice
'''
class matematica(ServiceBase):

    '''
    O decorador @rpc faz com que um método seja disponibilizado para invocação remota.
    Nele, definimos o tipo de entrada e o tipo da saída do método
    '''
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
    
        
'''
Application é uma classe do spyne que nos permite definir como vai ser a comunicação 
entre servidor e client, que no caso é o Soap11.
Nela também é necessário incluir as classes que vão ser disponibilizadas, nesse caso 'matematica'
e um nome para a aplicação
'''
application = Application([matematica], 'soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

wsgi_application = WsgiApplication(application)



import logging

from wsgiref.simple_server import make_server

'''
A biblioteca logging é uma forma simples de conseguirmos ter um log de tudo que acontece no servidor
'''

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

logging.info("Ouvindo a porta http://127.0.0.1:8000")
logging.info("wsdl em : http://localhost:8000/?wsdl")

'''
o simple server outra biblioteca que permite inicialização de um servidor e 
o funcionamento dele indefinidamente
'''
server = make_server('127.0.0.1', 8000, wsgi_application)
server.serve_forever()