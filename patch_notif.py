import re

with open("finalize_cloud.py", "r") as f:
    content = f.read()

# 1. Add notification button + status line to the settings modal HTML
old_html = '''      <div class="btn-row">
        <button class="aim" id="settings-save">Save</button>
      </div>
    </div>
  </div>
</div>'''

new_html = '''      <div class="field" style="border-top:1px solid var(--chrome-border); padding-top:10px; margin-top:6px;">
        <label>Notifications</label>
        <div id="notif-status" style="font-size:11px; margin-bottom:6px; color:#555;">Checking...</div>
        <button class="aim" id="btn-enable-notif" type="button">Enable Notifications</button>
      </div>
      <div class="btn-row">
        <button class="aim" id="settings-save">Save</button>
      </div>
    </div>
  </div>
</div>'''

if old_html in content:
    content = content.replace(old_html, new_html, 1)
    print("✅ Settings modal HTML patched.")
else:
    print("⚠️ Could not find settings modal anchor — HTML not patched (may already be patched).")

# 2. Add updateNotifStatus function + button handler + call it on settings open
old_js = '''document.getElementById('btn-settings').onclick = () => {
  document.getElementById('wallpaper-custom').value = settings.wallpaper;
  document.getElementById('font-size-select').value = settings.fontSize;
  document.getElementById('font-color-input').value = settings.fontColor;
  document.getElementById('bold-toggle').checked = settings.bold;
  document.getElementById('italic-toggle').checked = settings.italic;
  buildWallpaperSwatches();
  document.getElementById('settings-modal').style.display = 'flex';
};'''

new_js = '''function updateNotifStatus(){
  const el = document.getElementById('notif-status');
  if(!('Notification' in window)){ el.innerText = 'Not supported on this browser.'; return; }
  notifPermission = Notification.permission;
  if(notifPermission === 'granted') el.innerText = '✅ Enabled';
  else if(notifPermission === 'denied') el.innerText = '❌ Blocked — enable manually in browser site settings.';
  else el.innerText = '⏳ Not enabled yet — tap the button below.';
}
document.getElementById('btn-enable-notif').onclick = async () => {
  if(!('Notification' in window)){ alert('Notifications not supported on this browser.'); return; }
  notifPermission = await Notification.requestPermission();
  updateNotifStatus();
};
document.getElementById('btn-settings').onclick = () => {
  document.getElementById('wallpaper-custom').value = settings.wallpaper;
  document.getElementById('font-size-select').value = settings.fontSize;
  document.getElementById('font-color-input').value = settings.fontColor;
  document.getElementById('bold-toggle').checked = settings.bold;
  document.getElementById('italic-toggle').checked = settings.italic;
  buildWallpaperSwatches();
  updateNotifStatus();
  document.getElementById('settings-modal').style.display = 'flex';
};'''

if old_js in content:
    content = content.replace(old_js, new_js, 1)
    print("✅ Settings JS patched.")
else:
    print("⚠️ Could not find settings JS anchor — JS not patched (may already be patched).")

with open("finalize_cloud.py", "w") as f:
    f.write(content)
