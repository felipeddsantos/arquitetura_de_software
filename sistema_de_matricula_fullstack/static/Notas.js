/*

Arquitetura de Software - Sistema de Matrícula FullStack (Notas Aluno)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

*/

$(function() { 
    $('#btn').click(function() {
        $.ajax({
            url: '/notas',
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
                var html = "<tr> <th scope=row>Disciplinas</th>";
                for(var i = 0; i < len; i++){
                    html += "<td>" + myDict[i].disciplina + "</td>";  
                }
                html += "</tr> <tr> <th scope=row>Notas</th>"
                for(var i = 0; i < len; i++){
                    html += "<td>" + myDict[i].nota + "</td>";  
                }
                html += "</tr> <tr> <th scope=row>Faltas</th>"
                for(var i = 0; i < len; i++){
                    html += "<td>" + myDict[i].faltas + "</td>";  
                }
                html += "</tr>"
                $("#notas").html(html);
            },
            error: function(error){
                console.log(error);
            }
        });
    });
});
