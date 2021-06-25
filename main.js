const {app, BrowserWindow}=require('electron');

function createApp(){
    const win=new BrowserWindow(
        {
            width:800,
            height:450,
        }
    );
    
    win.loadFile('main.html');
}

app.whenReady().then(()=>{
    createApp();
});