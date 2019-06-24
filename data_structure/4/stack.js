let operations = {
    '+': function(v1, v2) {
        return v1 + v2;
    },
    '-': function(v1, v2) {
        return v1 - v2;
    },
    '*': function(v1, v2) {
        return v1 * v2;
    },
    '/': function(v1, v2) {
        return v1 / v2;
    }
}


function compute(input, operations) {
    // for x in y: x is index
    // for x of y: x is ele
    while ( input.length > 1 ) {
        let value1 = parseInt(input[0])
        let value2 = parseInt(input[2])
        let op = input[1]
        fun = operations[op]
        input[2] = fun(value1, value2)
        console.log(input)
        input = input.slice(2)
    } 
    if ( input.length == 1 ) {
        return input[0]
    } else {
        throw 1
    }
}


let str = ["1", "+", "100", "*", "-2"]
console.log(compute(str, operations))
