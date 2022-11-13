var valorStr = prompt("Digite um valor: ");
var valor = parseInt(valorStr);

if(valor>10){
    document.write("Maior que 10!")
}else if(valor<10){
    document.write("Menor que 10!")
}else{
    document.write("Igual a 10!")
}