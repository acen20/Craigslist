function activate_preloader(){
  loader = document.getElementById('search_preloader');
  loader.style.display = 'block';
}

window.onscroll = function() {scrollFunction()};
mybutton = document.getElementsByClassName("top-btn")[0];

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
