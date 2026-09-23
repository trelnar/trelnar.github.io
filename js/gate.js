(async function(){
  const H='c485ef4fb737514123b0e48a447f351744f4a5f166415aeb29fddb048cf2076b';
  const body=document.body;
  function open(){const g=document.getElementById('gate');if(g)g.remove();body.classList.remove('locked');}
  try{ if(sessionStorage.getItem('ok')==='1'){open();return;} }catch(e){}
  const g=document.createElement('div');g.id='gate';
  g.innerHTML='<form id="gateForm" autocomplete="off"><h1>Kevin Ellis</h1><p>Design leadership portfolio. Enter the password from my note.</p><input id="pw" type="password" placeholder="Password" aria-label="Password" autofocus><button type="submit">Open</button><div class="err" id="err"></div></form>';
  body.prepend(g);
  async function sha(s){const b=new TextEncoder().encode(s);const d=await crypto.subtle.digest('SHA-256',b);return [...new Uint8Array(d)].map(x=>x.toString(16).padStart(2,'0')).join('');}
  document.getElementById('gateForm').addEventListener('submit',async e=>{
    e.preventDefault();
    const v=document.getElementById('pw').value.trim().toLowerCase();
    if(await sha(v)===H){ try{sessionStorage.setItem('ok','1');}catch(e){} open(); }
    else{ document.getElementById('err').textContent='Not it. Check the note.'; }
  });
})();
