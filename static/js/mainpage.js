function sendData(){
	if (document.getElementById("cur-list1").value =="null"|| document.getElementById("cur-list2").value == "null"){
		alert("You have to select both currencies!")	
		return
	}
	if (!document.getElementById("cval1").value.match(/^[0-9.]+$/))
	{
		alert("Enter a numeric value!");
		return
	}
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
    		if (xhttp.readyState == 4 && xhttp.status == 200) {
			var response = JSON.parse(xhttp.responseText)
     			document.getElementById("cval2").value = response.result;
    		}
  	};
	xhttp.open('POST', '/');
	xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	var postVars =  'cval1='+document.getElementById("cval1").value+'&curname1='+document.getElementById("cur-list1").value+'&curname2='+document.getElementById("cur-list2").value;
	
	xhttp.send(postVars);
	return;
	
}
