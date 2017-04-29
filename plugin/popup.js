// retrieves the url of the current tab 
function getUrl(callback) {
    var info = {
        active: true,
        currentWindow: true
    };
    
    chrome.tabs.query(info, function(tabs) {
        var tab = tabs[0];
        callback(url);
    });
}

// enumerator of the different agb states
StateEnum = {
    GOOD: 0,
    MEDIUM: 1,
    BAD: 2,
    NOTFOUND: 3
};

// sets the background color of the extension
function setBackGroundColor(color) {
    document.body.style.backgroundColor = color;
}

function setIcon(icon) {
    chrome.browserAction.setIcon({path: "icons/" + icon + ".png"});
}

// sets the status of the extension
function setStatus(state) {
    switch (state) {
    case StateEnum.GOOD:
        setBackGroundColor("#5fba7d");
        setIcon("icon_green");
        break;
        
    case StateEnum.MEDIUM: 
        setBackGroundColor("#fbbc05");
        setIcon("icon_yellow");
        break;
        
    case StateEnum.BAD: 
        setBackGroundColor("#ea4335");
        setIcon("icon_red");
        break;
        
    }
}

// sets the text of the extension
function setText(text) {
    document.getElementById('mainText').textContent = text;
}

document.addEventListener('DOMContentLoaded', function() {
    setStatus(StateEnum.GOOD);
});

