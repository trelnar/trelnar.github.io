document.querySelectorAll('.vid').forEach(function(w){
  var v=w.querySelector('video'), b=w.querySelector('.play');
  function start(){ w.classList.add('playing'); v.controls=true; v.play(); }
  function reset(){ w.classList.remove('playing'); v.controls=false; v.load(); }
  b.addEventListener('click',start);
  v.addEventListener('click',function(){ if(!w.classList.contains('playing')) start(); });
  v.addEventListener('ended',reset);
});
