/*

Arquitetura de Software - Sistema de Matrícula FullStack (Matrículas Coordenador)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

*/

$(function() { 
    $('#btn').click(function() {
        $.ajax({
            url: '/matriculasCoordenador',
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
                    html += "<div class=form-check>" + "<input class=form-check-input type=checkbox value=" + myDict[i].disciplina + myDict[i].aluno + "id=defaultCheck1" + "name=" + myDict[i].disciplina + myDict[i].aluno + ">" + "<label class=form-check-label for=defaultCheck1>" + "Aluno: " + myDict[i].aluno + " - Disciplina: " + myDict[i].disciplina + "</label>" + "/div";
                    console.log(myDict[i])
                }
                $("#matriculascoordenador").html(html);
            },
            error: function(error){
                console.log(error);
            }
        });
    });
});
