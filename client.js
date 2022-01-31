/*
Para o node, temos um módulo chamado soap, que permite criarmos um client que consegue 
realizar as invocações dos métodos
*/
const soap = require('soap')
const url = 'http://localhost:8000/?wsdl'


// Aqui se tem a criação do client soap e a invocação dos métodos que foram definidos no servidor
soap.createClient(url, function(err, client) {
    client.fibonacci({n:20}, function(err, result) {
        console.log(result)
    })
    client.crivo_eratostenes({n:100}, function(err, result) {
        console.log(result)
    })
})