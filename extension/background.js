chrome.browserAction.onClicked.addListener(function(activeTab){
    var newURL = "https://www.baidu.com/";
    chrome.tabs.create({ url: newURL });
});