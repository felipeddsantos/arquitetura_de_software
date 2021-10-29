/*

Arquitetura de Software - Sistema de Matrícula FullStack (Matrículas Aluno)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

*/

$(function() { 
    $('#btn').click(function() {
        $.ajax({
            url: '/matricula',
            callback: 'calback',
            crossDomain: true,
            contentType: 'application/json; charset=utf-8',
            dataType: 'application/json',
            complete: function(data){
                alert(data.status);
                var myResult = data
                console.log(myResult);
                var myDict = JSON.parse(data.responseText);
                var len = myDict.length;
                var html = "";
                for(var i = 0; i < len; i++){
                    html += "<div class=form-check>" + "<input class=form-check-input type=checkbox value=" + myDict[i].nome + "id=defaultCheck1" + "name=" + myDict[i].codigo + ">" + "<label class=form-check-label for=defaultCheck1>" + myDict[i].nome + "</label>" + "/div";
                    console.log(myDict[i])
                }
                $("#matricula").html(html);
            },
            error: function(error){
                console.log(error);
            }
        });
    });
});
