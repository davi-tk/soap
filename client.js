const soap = require('soap')
const url = 'http://localhost:8000/?wsdl'


soap.createClient(url, function(err, client) {
    client.fibonacci({n:20}, function(err, result) {
        console.log(result)
    })
    client.crivo_eratostenes({n:100}, function(err, result) {
        console.log(result)
    })
})