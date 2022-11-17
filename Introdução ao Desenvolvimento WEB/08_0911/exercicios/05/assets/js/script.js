var nome = prompt("Digite seu nome: ");
var end = prompt("Digite seu endereço: ");
var email = prompt("Digite seu email: ");

var obj = {
    propriedadenome: nome,
    propriedadeend: end,
    propriedadeemail: email   
}

document.write(obj.propriedadenome);
document.write(obj.propriedadeend);
document.write(obj.propriedadeemail);