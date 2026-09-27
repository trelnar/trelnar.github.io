(function(){
  if(!window.matchMedia('(hover: none)').matches) return;
  var tiles=document.querySelectorAll('.tile');
  tiles.forEach(function(t){
    t.addEventListener('click',function(e){
      if(!t.classList.contains('show')){
        e.preventDefault();
        tiles.forEach(function(o){o.classList.remove('show');});
        t.classList.add('show');
      }
    });
  });
  document.addEventListener('click',function(e){
    if(!e.target.closest('.tile')) tiles.forEach(function(o){o.classList.remove('show');});
  });
})();
