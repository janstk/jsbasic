function checkmain(mailaddress){
    // mailaddress = "";
    if(!mailaddress){
        return false;
    }
    if(mailaddress.indexOf("@") == -1){
        return false;
    }
    // console.log(mailaddress)
    arr  = mailaddress.split("@")
    // console.log(arr)
    var username = arr[0];
    var mailhost = arr[1];
    // console.log(username.split(""))
    // console.log(mailhost.split(""))
    var ret = false;
    for(var x = 0;x<username.split("").length + mailhost.split("").length ;x++){
        if(x > username.split("").length-1){
            // mailhost
            ret = checkisVaild(mailhost.split("")[x - username.split("").length],true);
            // console.log("check character    " +mailhost.split("")[x - username.split("").length] + "   ret = " + ret);
        }else{
            //username
            ret = checkisVaild(username.split("")[x],false)
            // console.log("check character   " + username.split("")[x] + "   ret = " + ret);
        }
        if(ret == false){
            break;
        }
        // console.log("ret = " +ret)
    }
    if(!ret){
        return ret;
    }
    // console.log(ret);
    ret = chackisVaild(mailhost,true);
    // console.log("check---mailhost   " + ret);
    if(!ret){
          return ret;
    }
    ret = chackisVaild(username);
    // console.log("check---username   " + ret);
    if(!ret){
          return ret;
    }
    ret = checkisbeside(username,"-");
    if(!ret){
          return ret;
    }
    // console.log(ret);
    ret = checkisbeside(username,".");
    if(!ret){
          return ret;
    }
    // console.log(ret);
    ret = checkisbeside(username,"_");
    if(!ret){
          return ret;
    }
    // console.log(ret);
    ret = checkisbeside(mailhost,"-");
     if(!ret){
          return ret;
    }
    // console.log(ret);
    ret = checkisbeside(mailhost,".");
    if(!ret){
          return ret;
    }
    // console.log(ret);
    // console.log(ret);
    return ret;
}
function checkisVaild(character,ishost){
    var ret = false;
    // typeof character
    if(!character){
        ret =  false;
    }
    if(typeof character === typeof ""){
        if(character >= "a" && character <= "z"){
            ret =  true;
        }else if(character >= "A" && character <= "Z"){
            ret =  true;
        }
        else if(character >= "0" && character <= "9"){
            ret =  true;
        }
        else if(character === "_" || !ishost?(character === "-"):true || character === "."){
            ret = true;
        }else{
            ret = false;
        }
    }
    // console.log("ret = " + ret + ".. check " + character);
    return ret;
    
}
function chackisVaild(address,ishost){
    // hostaddress = "";
    if(!ishost || address.indexOf(".") > 0 && address.indexOf(".") < address.length-1){        
        var hostarr = address.split('\.');
        //  console.log(hostarr.length);
        if(hostarr.length > 0){
            for(var x = 0;x<hostarr.length;x++){
                // console.log(hostarr[x] + "---");
                if(true === ishost){
                    // console.log(hostarr[x] + "---" + hostarr[x].length < 2);
                    if(x == hostarr.length-1){
                        // console.log(hostarr[x] + "---111---" +((isalldigital(hostarr[x]))));
                        if(isalldigital(hostarr[x])){
                            return false;
                        }
                        if((hostarr[x].length < 2)){
                            return false;
                        }
                    }                   
                }
                if(hostarr[x].length == 0){
                    return false;
                }
            }
            return true;
        }
    }
    return false;
}
function isalldigital(str){
    if(!str || str.length == 0){
        return false;
    }
    var strarr = str.split("");
    for(var x = 0;x<strarr.length;x++){
        if(strarr[x] >= "0" && strarr[x] <= "9"){
            continue;
        }else{
            return false;
        }
    }
    return true;
}
function checkisbeside(str,emo){
    if(!str || !emo){
        return false;
    }
    if(str.indexOf(emo)<0){
        return true;
    }
    //  console.log(str,emo);
    
    var strarr = str.split(emo)
    // console.log(strarr);
    for(var x = 0;x<strarr.length;x++){
        if(strarr[x].length == 0){
            return false;
        }
    }
    return true;
}

function test(mailaddress){
    console.log(mailaddress + '\nis vaild mailaddress ?= ' + checkmain(mailaddress))
}
var mailaddress1 = "helllo@123123.cooadsi.sda"
var mailaddress2 = "hell--lo@123123.cooadsi.sda.123"
var mailaddress3 = "hell-l.o.@123123.cooadsi.sda"
var mailaddress4 = "hell--lo@123123.cooadsi.sda"
var mailaddress5 = "helllo@1231..23.cooadsi.sda"
var mailaddress6 = "helllo@123123.cooadsi.sda"
var mailaddress7 = "helllo@123123...sda"
var mailaddress8 = "helllo@123123.cooadsi.sda."
test(mailaddress1);
test(mailaddress2);
test(mailaddress3);
test(mailaddress4);
test(mailaddress5);
test(mailaddress6);
test(mailaddress7);
test(mailaddress8);