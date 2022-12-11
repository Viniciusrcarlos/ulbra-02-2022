function calculadora(){
    var numero1 = parseFloat(document.getElementById('valor1').value)
    var numero2 = parseFloat(document.getElementById('valor2').value)
    var operacao = document.getElementById('operacao').value
    var resultado;
    
    switch(operacao){
        case '+':
            resultado = numero1 + numero2;
            break;
            console.log(operacao);
        case '-':
            resultado = numero1 - numero2;
            break;
            console.log(operacao);
        case '/':
            resultado = numero1 / numero2;
            break;
            console.log(resultado);
        case '*':
            resultado = numero1 * numero2;
            break;
            console.log(resultado);
    }
    document.getElementById('resultado').innerHTML = 'O resultado é: ' + resultado

}