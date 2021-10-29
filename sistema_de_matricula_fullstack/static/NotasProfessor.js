/*

Arquitetura de Software - Sistema de Matrícula FullStack (Notas Professor)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

*/

$(function() { 
    $('#btn').click(function() {
        $.ajax({
            url: '/notasProfessor',
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
                    html += "<tr> <td>" + myDict[i].aluno + "</td> <td> <div class=form-group col-md-5> <input type=text class=form-control id=inputContry name =" + myDict[i].id_matricula + "a value =" + myDict[i].nota + "> </dev> </td> <td> <div class=form-group col-md-5>" + "<input type=text class=form-control id=inputContry name = " + myDict[i].aluno + "value = " + myDict[i].faltas + "> </dev> </td> </tr>";  
                }
                $("#notasprofessor").html(html);
            },
            error: function(error){
                console.log(error);
            }
        });
    });
});
