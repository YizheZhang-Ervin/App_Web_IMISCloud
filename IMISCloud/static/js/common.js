function setHeight(){
    let mainpart = document.getElementById("mainpart");
    mainpart.style.height = window.innerHeight+"px";
}

function rememberMe(){
    alert('Sorry, you have to choose remember');
    let rememberme = document.getElementById("rememberme");
    rememberme.checked = "checked";
}

function details(filename){
    document.getElementById("btn-details").click();
    document.getElementById("embed-content").src= "/CloudStorage/"+filename;
    document.getElementById("dld").href = "/CloudStorage/"+filename;
    document.getElementById("dld").download = filename;
}

window.onload=function(){
    setHeight();
}

// form validation
(function () {
  window.addEventListener('load', function () {
    var forms = document.getElementsByClassName('needs-validation')
    Array.prototype.filter.call(forms, function (form) {
      form.addEventListener('submit', function (event) {
        if (form.checkValidity() === false) {
          event.preventDefault()
          event.stopPropagation()
        }
        form.classList.add('was-validated')
      }, false)
    })
  }, false)
}())
