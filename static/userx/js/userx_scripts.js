function doTransfer() {
	var xhr = new XMLHttpRequest();
	var form = document.forms.formTransfer;
	var data = new FormData(form);
	xhr.open('POST', '/do_transfer', true);
	xhr.setRequestHeader("X-CSRFToken", form.csrfmiddlewaretoken.value);
	xhr.onload = function () {
		if (xhr.readyState == 4 || xhr.readyState == "complete") {
            div_message=document.getElementById('result_message');
			// Распакуем полученный JSON
			eval("server_reply = " + xhr.responseText);
			if(server_reply.status == 0) {
           		div_message.className = "";
				div_message.className = "alert alert-success";
				form.inn.value="";
				form.sum.value="";
            	div_message.innerHTML = "Проведено! На счёт "+server_reply.count+" пользователей поступило "+server_reply.send_money+" руб.";
			} 
            else {
				div_message.className = "";
				div_message.className = "alert alert-danger";
            	div_message.innerHTML = server_reply.message ;
            } 
		}
	}
    xhr.send(data);
	return false;
}