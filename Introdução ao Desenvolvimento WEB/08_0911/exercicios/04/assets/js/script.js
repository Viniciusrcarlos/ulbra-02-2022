var nome = prompt("Digite um nome: ");
var numeroFirts = prompt("Digite a quantidade de vezes que você quer printar seu nome no html: ");

var numero = parseInt(numeroFirts);

for (var i = 0; i < numero; i++){
    document.write(nome,"<br>")
}