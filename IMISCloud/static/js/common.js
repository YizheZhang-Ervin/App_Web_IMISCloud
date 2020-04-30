function setHeight(){
    let mainpart = document.getElementById("mainpart");
    mainpart.style.height = window.innerHeight+"px";
}

function rememberMe(){
    alert('Sorry, you have to choose remember');
    let rememberme = document.getElementById("rememberme");
    rememberme.checked = "checked";
}

window.onload=setHeight;