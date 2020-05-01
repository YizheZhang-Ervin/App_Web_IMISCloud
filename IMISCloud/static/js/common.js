function setHeight(){
    let mainpart = document.getElementById("mainpart");
    mainpart.style.height = window.innerHeight+"px";
}

function rememberMe(){
    alert('Sorry, you have to choose remember');
    let rememberme = document.getElementById("rememberme");
    rememberme.checked = "checked";
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
