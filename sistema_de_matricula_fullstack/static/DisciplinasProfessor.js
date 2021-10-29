/*

Arquitetura de Software - Sistema de Matrícula FullStack (Disciplinas Professor)
Felipe Daniel Dias dos Santos - 11711ECP004
Graduação em Engenharia de Computação - Faculdade de Engenharia Elétrica - Universidade Federal de Uberlândia

*/

$(function() { 
    $('#btn').click(function() {
        $.ajax({
            url: '/disciplinasProfessor',
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
                    html += "<option value =" + myDict[i].codigo + ">" + myDict[i].nome + "</option>";
                    console.log(myDict[i])
                }
                $("#disciplinasprofessor").html(html);
            },
            error: function(error){
                console.log(error);
            }
        });
    });
});
