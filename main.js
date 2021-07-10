const {app, BrowserWindow}=require('electron');

function createApp(){
    const win=new BrowserWindow();
    
    win.loadFile('setup_ui.html');
}

app.whenReady().then(()=>{
    createApp();
});