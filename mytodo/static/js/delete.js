// document.getElementById("delete_point").checked = true;

function delete_task(task_id)
{   
    // alert("/task/delete/"+String(task_id))
    var xhr = new XMLHttpRequest();

    // // 2. Конфигурируем его: GET-запрос на URL 'phones.json'
    // xhr.open('GET', "/tasks/delete/"+String(task_id), false);

    // // 3. Отсылаем запрос
    // xhr.send();


    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "/tasks/delete/"+String(task_id), false );
    xmlHttp.send( null );

    document.location.reload(true);
    
    return xmlHttp.responseText;
}