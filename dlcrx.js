(window.crx = function () {

    if (document.location.hostname != "chrome.google.com") {
        alert("This will only work on the Google Chrome extensions website.");
        return;
    }

    if (document.location.pathname.substring(0,17) != "/webstore/detail/") {
        alert("You should open some extension specific page to get the download link.");
        return;
    }
    
    var c = "http://graspcrx.sinaapp.com/bookmark/" + document.location.pathname.split("/")[3];
    window.open(c);
})();