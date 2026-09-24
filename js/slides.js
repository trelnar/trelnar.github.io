document.querySelectorAll('.slides').forEach(function(s){
  var imgs=s.querySelectorAll('img'), i=0; if(imgs.length<2) return;
  setInterval(function(){ imgs[i].classList.remove('on'); i=(i+1)%imgs.length; imgs[i].classList.add('on'); },3200);
});
