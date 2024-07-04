let readline = require("readline-sync");

function calculadora() {
    let n1 = readline.question("Digite um número: ");
    let n2 = readline.question("Digite outro número: ");
    let op = readline.question("Digite uma operação (+ - * /): ");
    
    
    n1 = parseFloat(n1);
    n2 = parseFloat(n2);
    
    // Verificando se as entradas são números válidos
    if (isNaN(n1) || isNaN(n2)) {
        console.log("Por favor, insira números válidos.");
        return;
    }

    // Processando a operação
    switch(op) {
        case "+":
            console.log("Soma = " + (n1 + n2));
            break;
        case "-":
            console.log("Subtração = " + (n1 - n2));
            break;
        case "*":
            console.log("Multiplicação = " + (n1 * n2));
            break;
        case "/":
            if (n2 === 0) {
                console.log("Erro: Divisão por zero não é permitida.");
            } else {
                console.log("Divisão = " + (n1 / n2));
            }
            break;
        default:
            console.log("Operação inválida. Por favor, insira uma operação válida (+, -, *, /).");
            break;
    }
}

// Chamando a função calculadora
calculadora();