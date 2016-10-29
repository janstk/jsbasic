//邮箱验证
function mail(a){

	var arr = a.split('@');
	var str1 = arr[0];
	var str2 = arr[1];

	if(arr.length !=2){
		return true;
	}
	for(var i = 0;i<str1.length;i++) {

		if (str1.charCodeAt(i) == 95 || (str1.charCodeAt(i) >= 48 && 57 >= str1.charCodeAt(i))|| (str1.charCodeAt(i) >= 65 && 90 >= str1.charCodeAt(i))|| (str1.charCodeAt(i) >= 97 && str1.charCodeAt(i) <= 122)){}
		else{return true;}	}

	var arr2 = str2.split('.');
	var str3 =arr2[0];
	var str4 =arr2[1];
	if(arr2.length!=2){
	     return true;
	}
    for(j=0;j<str3.length;j++){

		if((str3.charCodeAt(j)>=48 && 57>=str3.charCodeAt(j))||(str3.charCodeAt(j)>=65 && 90>=str3.charCodeAt(j))||(str3.charCodeAt(j)>=97 &&str3.charCodeAt(j)<=122)) {}
		else{return true;}
	}
	for(m=0;m<str4.length;m++){

		if((str4.charCodeAt(m)>=65 && 90>=str4.charCodeAt(m))||(str4.charCodeAt(m)>=97 &&str4.charCodeAt(m)<=122)){}
		else{return true;}
	}
}

//手机号验证
function tel(b){
	if(b.length != '11'){
		return true;
	}
	if(b[1] != '3' && b[1] != '5' && b[1] != '8'){
		return true;
	}
	if((parseInt(b)+'').length!='11'){
		return true;
	}

}

window.onload = function(){
     var oTxt = document.getElementById('text');
     var oBtn = document.getElementById('button');

     oBtn.onclick = function(){

     		var oBox = oTxt.value;
     		if(oBox.indexOf('@')!=-1){

				 //邮箱验证
				if(mail(oBox)){
					alert('格式输入错误，请重新输入mail');
				}
     		}
     		else{
     			
     			  //手机验证
				 if(tel(oBox)){
					 alert('格式输入错误，请重新输入tel');
				 }
     		}
              
     };

};

