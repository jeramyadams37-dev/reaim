#!/usr/bin/env python3
import os

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<title>ReAIM Cloud</title>
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#0A246A">
<style>
:root{ --titlebar-start:#0A246A; --titlebar-end:#A6CAF0; --chrome-bg:#ECE9D8; --chrome-border:#7F9DB9; --gold:#FFCC00; --online:#3DA84A; --away:#F2A93B; --offline:#9A9A9A; --ink:#1A1A1A; }
*{box-sizing:border-box;}
body{ margin:0; font-family:"Segoe UI","Tahoma",Verdana,sans-serif; background:#3A6EA5; background-image:linear-gradient(160deg,#5C8FC4,#2B4F77); height:100vh; height:100dvh; overflow:auto; color:var(--ink); }
.window{ background:var(--chrome-bg); border:1px solid var(--chrome-border); border-radius:6px; box-shadow:2px 2px 10px rgba(0,0,0,.35); overflow:hidden; display:flex; flex-direction:column; }
.titlebar{ background:linear-gradient(to right,var(--titlebar-start),var(--titlebar-end)); color:#fff; font-weight:bold; font-size:13px; padding:5px 8px; display:flex; align-items:center; justify-content:space-between; cursor:default; user-select:none; }
.titlebar .dot{width:8px;height:8px;border-radius:50%;display:inline-block;margin-right:6px;}
.titlebar-btns{display:flex;gap:4px;}
.titlebar-btns button{ width:18px;height:18px;border:1px solid #fff;background:#3A6EA5;color:#fff; font-size:11px;line-height:1;border-radius:2px;cursor:pointer; }
#login-screen{ position:fixed;inset:0;display:flex;align-items:center;justify-content:center; }
#login-screen .window{width:300px;}
#login-screen .body{padding:16px;}
.logo{ text-align:center;font-size:28px;font-weight:800;color:var(--gold); text-shadow:1px 1px 0 #0A246A, -1px -1px 0 #0A246A, 1px -1px 0 #0A246A, -1px 1px 0 #0A246A; margin-bottom:4px;letter-spacing:1px; }
.tagline{text-align:center;font-size:11px;color:#555;margin-bottom:14px;}
.field{margin-bottom:10px;}
.field label{display:block;font-size:11px;margin-bottom:3px;color:#333;}
.field input{width:100%;padding:6px 7px;border:1px solid var(--chrome-border);border-radius:3px;font-size:14px;}
.btn-row{display:flex;gap:8px;margin-top:12px;}
button.aim{ flex:1;padding:7px;border-radius:4px;border:1px solid #5077a0; background:linear-gradient(to bottom,#dceaf7,#a9c8e6); font-weight:bold;font-size:12px;cursor:pointer;color:#0A246A; }
button.aim:active{background:#a9c8e6;}
.error-msg{color:#B00020;font-size:11px;margin-top:6px;min-height:14px;}
#mode-toggle{text-align:center;font-size:11px;margin-top:10px;color:#0A246A;text-decoration:underline;cursor:pointer;}
#app{display:none;height:100vh;height:100dvh;padding:10px;gap:10px;}
#app.shown{display:flex;}
#buddylist{width:230px;min-width:230px;height:100%;}
#buddylist .body{flex:1;overflow-y:auto;padding:4px 0;}
.group-label{ background:#D4D0C8;font-size:11px;font-weight:bold;padding:3px 8px;color:#333; border-top:1px solid #fff;border-bottom:1px solid #b8b8b8; }
.buddy-row{ display:flex;align-items:center;gap:6px;padding:6px 8px;cursor:pointer;font-size:13px; }
.buddy-row:hover{background:#cfe4fb;}
.status-dot{width:9px;height:9px;border-radius:50%;flex-shrink:0;}
.buddy-name{flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}
.buddy-away-note{ font-size:10px;background:#fff7c2;border:1px solid #e6d68a;color:#5a4d00; padding:1px 5px;border-radius:3px;margin-left:24px;margin-top:-2px;margin-bottom:4px; white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:170px; }
.unread-badge{ background:var(--gold);color:#5a4400;font-size:10px;font-weight:bold; border-radius:8px;padding:1px 6px; }
#buddylist .footer{padding:6px 8px;border-top:1px solid var(--chrome-border);display:flex;gap:6px;}
#buddylist .footer input{flex:1;font-size:12px;padding:4px;border:1px solid var(--chrome-border);border-radius:3px;}
#buddylist .footer button{font-size:11px;padding:4px 8px;border-radius:3px;border:1px solid #5077a0;background:#dceaf7;cursor:pointer;}
.my-status-row{padding:6px 8px;border-bottom:1px solid var(--chrome-border);font-size:12px;display:flex;align-items:center;gap:6px;}
.my-status-row select{font-size:11px;}
.my-status-row input{flex:1;font-size:11px;padding:3px;border:1px solid var(--chrome-border);border-radius:3px;}
#im-windows{flex:1;display:flex;flex-wrap:wrap;align-content:flex-start;gap:10px;overflow:auto;height:100%;}
.im-window{width:300px;height:380px;}
.im-window .body{flex:1;overflow-y:auto;padding:8px;font-size:13px;background:#fff;}
.im-msg{margin-bottom:8px;max-width:90%;}
.im-msg .who{font-weight:bold;font-size:11px;}
.im-msg.me .who{color:#0A246A;} .im-msg.them .who{color:#7a1f1f;}
.im-msg .bubble{padding:4px 0;word-wrap:break-word;} .im-msg .meta{font-size:9px;color:#999;}
.im-msg.auto .bubble{font-style:italic;color:#5a4d00;} .typing-note{font-size:11px;color:#888;font-style:italic;padding:2px 8px;}
.im-input-row{display:flex;border-top:1px solid var(--chrome-border);}
.im-input-row textarea{ flex:1;border:none;resize:none;padding:7px;font-size:13px;font-family:inherit;height:44px; }
.im-input-row textarea:focus{outline:none;}
.im-input-row button{border:none;background:var(--gold);padding:0 14px;font-weight:bold;font-size:12px;cursor:pointer;}
@media (max-width:700px){
  #app{padding:0;gap:0;}
  #buddylist{width:100%;min-width:0;border-radius:0;display:flex;}
  #buddylist.hide-on-mobile{display:none;}
  #im-windows{padding:0;}
  .im-window{width:100%;height:100%;border-radius:0;flex:1;}
  #im-windows.hide-on-mobile{display:none;}
}
</style>
</head>
<body>

<div id="login-screen">
  <div class="window">
    <div class="titlebar"><span>Sign In</span><div class="titlebar-btns"><button>_</button><button>x</button></div></div>
    <div class="body">
      <div class="logo">ReAIM Cloud</div>
      <div class="tagline">serverless, worldwide.</div>
      <div class="field">
        <label>Screen Name</label>
        <input id="login-username" autocomplete="username" maxlength="20">
      </div>
      <div class="field">
        <label>Password</label>
        <input id="login-password" type="password" autocomplete="current-password">
      </div>
      <div class="btn-row">
        <button class="aim" id="btn-submit">Sign In</button>
      </div>
      <div class="error-msg" id="login-error"></div>
      <div id="mode-toggle">New here? Create a screen name</div>
    </div>
  </div>
</div>

<div id="app">
  <div class="window" id="buddylist">
    <div class="titlebar">
      <span><span class="dot" id="my-dot" style="background:var(--online)"></span><span id="my-username">Buddy List</span></span>
      <div class="titlebar-btns"><button id="btn-signout">x</button></div>
    </div>
    <div class="my-status-row">
      <select id="my-status">
        <option value="online">Online</option>
        <option value="away">Away</option>
      </select>
      <input id="my-away-msg" placeholder="Away message (optional)" style="display:none;">
    </div>
    <div class="body" id="buddy-list-body"></div>
    <div class="footer">
      <input id="add-buddy-input" placeholder="Add a buddy by screen name">
      <button id="add-buddy-btn">Add</button>
    </div>
  </div>
  <div id="im-windows" class="hide-on-mobile"></div>
</div>

<!-- FIREBASE SDK (ES Modules via CDN) -->
<script type="module">
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-app.js";
import { getAuth, signInWithEmailAndPassword, createUserWithEmailAndPassword, onAuthStateChanged, signOut } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-auth.js";
import { getDatabase, ref, set, push, onValue, onChildAdded, update, serverTimestamp, onDisconnect, get, child } from "https://www.gstatic.com/firebasejs/10.8.1/firebase-database.js";

const firebaseConfig = {
  apiKey: "AIzaSyDI_R76XopGLngLC1TbPbB4xAnbVRCNVxY",
  authDomain: "reaim-cloud.firebaseapp.com",
  projectId: "reaim-cloud",
  storageBucket: "reaim-cloud.firebasestorage.app",
  messagingSenderId: "945466693919",
  appId: "1:945466693919:web:52b5ea1d9c2c1422fd782a"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getDatabase(app);

let myUsername = null;
let buddies = {};
let openWindows = {};

let actx = null;
function ctx(){ if(!actx){ actx = new (window.AudioContext||window.webkitAudioContext)(); } return actx; }
function tone(freq, start, dur, type='sine', gain=0.15){
  const c = ctx(); const osc = c.createOscillator(); const g = c.createGain();
  osc.type = type; osc.frequency.value = freq; g.gain.value = gain;
  osc.connect(g); g.connect(c.destination); osc.start(c.currentTime+start);
  g.gain.setValueAtTime(gain, c.currentTime+start);
  g.gain.exponentialRampToValueAtTime(0.001, c.currentTime+start+dur);
  osc.stop(c.currentTime+start+dur);
}
function soundSignOn(){ tone(440,0,.12); tone(660,.12,.18); }
function soundSignOff(){ tone(660,0,.12); tone(440,.12,.18); }
function soundIM(){ tone(880,0,.08,'triangle',0.2); tone(1320,.09,.1,'triangle',0.18); }

function statusColor(s){ return s==='online' ? 'var(--online)' : (s==='away' ? 'var(--away)' : 'var(--offline)'); }
function fmtTime(ts){ const d = new Date(ts); return d.toLocaleTimeString([], {hour:'numeric', minute:'2-digit'}); }
function esc(s){ const d=document.createElement('div'); d.innerText=s; return d.innerHTML; }
function formatEmail(user){ return user.toLowerCase() + '@reaim.app'; } 

let isRegisterMode = false;
document.getElementById('mode-toggle').onclick = () => {
  isRegisterMode = !isRegisterMode;
  document.getElementById('btn-submit').innerText = isRegisterMode ? 'Create Screen Name' : 'Sign In';
  document.getElementById('mode-toggle').innerText = isRegisterMode ? 'Already have a screen name? Sign in' : "New here? Create a screen name";
};

document.getElementById('btn-submit').onclick = async () => {
  const username = document.getElementById('login-username').value.trim();
  const password = document.getElementById('login-password').value;
  const errEl = document.getElementById('login-error'); errEl.innerText = '';
  if(!username || !password) return errEl.innerText = "Screen name and password required";
  
  try {
    const email = formatEmail(username);
    if(isRegisterMode) {
      await createUserWithEmailAndPassword(auth, email, password);
      await set(ref(db, `users/${username.toLowerCase()}`), { username: username });
    } else {
      await signInWithEmailAndPassword(auth, email, password);
    }
  } catch(e) { errEl.innerText = e.message.replace('Firebase: ', ''); }
};

document.getElementById('btn-signout').onclick = () => { soundSignOff(); signOut(auth); };

onAuthStateChanged(auth, (user) => {
  if (user) {
    myUsername = user.email.split('@')[0]; 
    startApp();
  } else {
    document.getElementById('login-screen').style.display = 'flex';
    document.getElementById('app').classList.remove('shown');
  }
});

function startApp(){
  document.getElementById('login-screen').style.display='none';
  document.getElementById('app').classList.add('shown');
  document.getElementById('my-username').innerText = myUsername;
  soundSignOn();
  
  const myPresenceRef = ref(db, `presence/${myUsername}`);
  onDisconnect(myPresenceRef).set({ status: 'offline', away_message: '' });
  
  document.getElementById('my-status').onchange = (e) => {
    document.getElementById('my-away-msg').style.display = e.target.value==='away' ? 'block' : 'none';
    pushMyStatus();
  };
  document.getElementById('my-away-msg').addEventListener('change', pushMyStatus);
  pushMyStatus(); 

  document.getElementById('add-buddy-btn').onclick = addBuddy;
  loadBuddies();
}

function pushMyStatus(){
  const status = document.getElementById('my-status').value;
  const away_message = document.getElementById('my-away-msg').value;
  document.getElementById('my-dot').style.background = statusColor(status);
  set(ref(db, `presence/${myUsername}`), { status, away_message });
}

async function addBuddy(){
  const input = document.getElementById('add-buddy-input');
  const target = input.value.trim().toLowerCase();
  if(!target || target === myUsername) return;
  
  const snapshot = await get(child(ref(db), `users/${target}`));
  if(snapshot.exists()) {
    const realName = snapshot.val().username;
    await set(ref(db, `buddies/${myUsername}/${target}`), realName);
    input.value = '';
  } else {
    alert("No screen name found with that name");
  }
}

function loadBuddies(){
  const buddiesRef = ref(db, `buddies/${myUsername}`);
  onValue(buddiesRef, (snapshot) => {
    const data = snapshot.val() || {};
    Object.values(data).forEach(name => {
      if(!buddies[name]) {
        buddies[name] = {status:'offline', away_message:'', unread:0};
        onValue(ref(db, `presence/${name.toLowerCase()}`), (presSnap) => {
          const p = presSnap.val() || {status:'offline', away_message:''};
          buddies[name].status = p.status;
          buddies[name].away_message = p.away_message;
          renderBuddyList();
        });
      }
    });
    renderBuddyList();
  });
}

function renderBuddyList(){
  const body = document.getElementById('buddy-list-body');
  body.innerHTML = '';
  const groups = {online:[], away:[], offline:[]};
  Object.entries(buddies).forEach(([name, b]) => groups[b.status].push(name));
  
  [['online','Online'], ['away','Away'], ['offline','Offline']].forEach(([key, label]) => {
    if(groups[key].length === 0) return;
    const gl = document.createElement('div'); gl.className = 'group-label'; gl.innerText = `${label} (${groups[key].length})`;
    body.appendChild(gl);
    groups[key].sort((a,b)=>a.localeCompare(b)).forEach(name => {
      const b = buddies[name];
      const row = document.createElement('div'); row.className = 'buddy-row';
      row.innerHTML = `<span class="status-dot" style="background:${statusColor(b.status)}"></span><span class="buddy-name">${esc(name)}</span>${b.unread? `<span class="unread-badge">${b.unread}</span>`:''}`;
      row.onclick = () => openIM(name); body.appendChild(row);
      if(b.status==='away' && b.away_message){
        const note = document.createElement('div'); note.className = 'buddy-away-note'; note.innerText = b.away_message; body.appendChild(note);
      }
    });
  });
}

function getChatId(user1, user2) {
  return [user1.toLowerCase(), user2.toLowerCase()].sort().join('_');
}

function openIM(name){
  if(openWindows[name]){ openWindows[name].scrollIntoView(); return; }
  if(buddies[name]) buddies[name].unread = 0;
  renderBuddyList();

  document.getElementById('buddylist').classList.add('hide-on-mobile');
  document.getElementById('im-windows').classList.remove('hide-on-mobile');

  const win = document.createElement('div'); win.className = 'window im-window';
  win.innerHTML = `
    <div class="titlebar">
      <span><span class="status-dot" style="background:${statusColor(buddies[name]?.status||'offline')}"></span> ${esc(name)}</span>
      <div class="titlebar-btns"><button class="im-close">x</button></div>
    </div>
    <div class="body"></div>
    <div class="typing-note" style="display:none;"></div>
    <div class="im-input-row">
      <textarea placeholder="Type a message..."></textarea>
      <button>Send</button>
    </div>
  `;
  document.getElementById('im-windows').appendChild(win);
  openWindows[name] = win;

  const bodyEl = win.querySelector('.body');
  const textarea = win.querySelector('textarea');
  const sendBtn = win.querySelector('button');
  win._bodyEl = bodyEl;

  const chatId = getChatId(myUsername, name);
  const messagesRef = ref(db, `messages/${chatId}`);

  win.querySelector('.im-close').onclick = () => { 
    win.remove(); delete openWindows[name]; 
    if(Object.keys(openWindows).length === 0) {
      document.getElementById('buddylist').classList.remove('hide-on-mobile');
      document.getElementById('im-windows').classList.add('hide-on-mobile');
    }
  };

  function send(){
    const bodyText = textarea.value.trim(); if(!bodyText) return;
    push(messagesRef, { sender: myUsername, body: bodyText, sent_at: serverTimestamp() });
    
    if(buddies[name] && buddies[name].status === 'away' && buddies[name].away_message) {
      setTimeout(() => {
         push(messagesRef, { sender: name, body: buddies[name].away_message, sent_at: serverTimestamp(), auto_reply: true });
      }, 500);
    }
    textarea.value='';
  }
  sendBtn.onclick = send;
  textarea.addEventListener('keydown', e=>{ if(e.key==='Enter' && !e.shiftKey){ e.preventDefault(); send(); } });

  let initialLoad = true;
  onChildAdded(messagesRef, (data) => {
    const msg = data.val();
    appendMessage(win, msg);
    if(!initialLoad && msg.sender !== myUsername) soundIM();
  });
  setTimeout(() => { initialLoad = false; }, 1000);
}

function appendMessage(win, msg){
  const mine = msg.sender.toLowerCase() === myUsername.toLowerCase();
  const row = document.createElement('div'); row.className = 'im-msg ' + (mine?'me':'them') + (msg.auto_reply?' auto':'');
  row.innerHTML = `<div class="who">${esc(msg.sender)}${msg.auto_reply?' (auto-reply)':''}</div><div class="bubble">${esc(msg.body)}</div><div class="meta">${fmtTime(msg.sent_at || Date.now())}</div>`;
  win._bodyEl.appendChild(row);
  win._bodyEl.scrollTop = win._bodyEl.scrollHeight;
}
</script>
</body>
</html>"""

with open("index.html", "w") as f:
    f.write(HTML_CONTENT)

print("✅ index.html strictly overwritten with correct Firebase configurations.")
