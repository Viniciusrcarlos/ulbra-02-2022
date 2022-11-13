var valorUm = prompt("Digite um número: ");
var valorDois = prompt("Digite um outro número: ");
var operacao = prompt("Digite a operação que deseja fazer: ")

var valor01 = parseFloat(valorUm);
var valor02 = parseFloat(valorDois);

if(operacao == "-"){
    resultado = valor01 - valor02
    document.write("A subtração dos dois números é: ",resultado)
}else if(operacao == "+"){
    resultado = valor01 + valor02
    document.write("A soma dos dois números é: ",resultado)
}else if(operacao == "*"){
    resultado = valor01*valor02
    document.write("A multiplicação dos dois valores é: ",resultado)
}else if(operacao == "/"){
    resultado = valor01/valor02
    document.write("A divisão dos dois valores é: ",resultado)
}

