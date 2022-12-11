function calculo(){
    var kwh = parseFloat(document.getElementById('kwh').value)
    var hora = parseFloat(document.getElementById('horas').value)
    var resultado;

    if(kwh <=100){
        resultado = kwh*hora
        document.getElementById('resultado').innerHTML = 'Total gasto: R$' + resultado
    }else if(kwh > 100 && kwh <= 200){
        resultado = (kwh*hora)*1.25
        document.getElementById('resultado').innerHTML = 'Total gasto + 25% devido ao consumo de mais de 100kwh: R$' + resultado
    }else{
        resultado = (kwh*hora)*1.5
        document.getElementById('resultado').innerHTML = 'Total gasto + 50% devido ao consumo de mais de 200khw: R$' + resultado
    }

}