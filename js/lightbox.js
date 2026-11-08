(function(){
  var links=document.querySelectorAll('a.lb[data-video]'); if(!links.length) return;
  var layer=document.createElement('div'); layer.className='layer'; layer.hidden=true;
  layer.innerHTML='<div class="layer-box"><video controls playsinline preload="metadata"></video></div><button class="layer-close" aria-label="Close">&times;</button>';
  document.body.appendChild(layer);
  var v=layer.querySelector('video'), last=null;
  function open(a){ last=a; v.src=a.getAttribute('data-video'); layer.hidden=false; document.body.classList.add('noscroll'); layer.querySelector('.layer-close').focus(); v.play().catch(function(){}); }
  function close(){ v.pause(); v.removeAttribute('src'); v.load(); layer.hidden=true; document.body.classList.remove('noscroll'); if(last) last.focus(); }
  links.forEach(function(a){ a.addEventListener('click',function(e){ e.preventDefault(); open(a); }); });
  layer.addEventListener('click',function(e){ if(e.target===layer||e.target.classList.contains('layer-close')) close(); });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape'&&!layer.hidden) close(); });
})();
