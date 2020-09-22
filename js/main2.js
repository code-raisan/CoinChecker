let requestURL = "https://riyblog.shop/arg/?u=https://api.bitflyer.jp/v1/ticker?product_code=BTC_JPY";
let request = new XMLHttpRequest();
let old = 0;
let mo = 20;
const dom = document.getElementById("dom");
const dom2 = document.getElementById("dom2");

dom.innerText = "お待ちください...";

function xhr(){
    request.open("GET", requestURL);
    request.responseType = "json";
    request.send();
    request.onload = function() {
        ps(request.response);
    }
    
    function ps(res){
        let mo = res.ltp;
        console.log(mo);
        if(old === 0){
            dom.innerText = "現在の価格 : " + mo;
            dom2.innerText = "お待ちください...";
        }else if(old < mo){
            dom2.innerText = "価格が上がりました";
            dom.innerText = "現在の価格 : " + mo;
        }else if(mo < old){
            dom2.innerText = "価格が下がりました";
            dom.innerText = "現在の価格 : " + mo;
        }
        old = mo;
    }
}

setInterval("xhr()",1000);
