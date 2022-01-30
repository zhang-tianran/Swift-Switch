// chrome.runtime.onMessage.addListener(
//   function(request, sender, sendResponse) {
//     console.log(sender.tab ?
//                 "from a content script:" + sender.tab.url :
//                 "from the extension");
//     if (request.greeting === "hello")
//       sendResponse({farewell: "goodbye"});
//   }
// );

// function countTags(tag, callback) {
//     chrome.tabs.executeScript({
//         code: "document.getElementsByTagName('" + tag + "').length"
//     }, function(result) {
//         if (chrome.runtime.lastError) {
//             console.error(chrome.runtime.lastError);
//         } else {
//             callback(result[0]);
//         }
//     });
// }

function getSource(callback) {
  chrome.tabs.executeScript({
      code: "document.querySelector('#product > div.l--sticky-wrapper.pdp-mfe-dd4axt > div.l--breadcrumb-photo-wrapper.pdp-mfe-dkc8kg > div:nth-child(2) > div.pdp-mfe-11qso3a > div > div:nth-last-child(1) > div > a').href"
  }, function(result) {
      if (chrome.runtime.lastError) {
          console.error(chrome.runtime.lastError);
      } else {
          callback(result[0]);
      }
  });
}

// function countDivs() {
//   countTags("div", function(num) {
//       console.log("Found %i divs", num);
//   });
// }

// document.getElementById("myButton").addEventListener("click", countDivs);
// countDivs();
getSource(function(src) {
    console.log("Image source", src);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        const response = JSON.parse(this.responseText);
        let url1 = response.a;
        let url2 = response.b;
        let url3 = response.c;
        document.getElementById("url1").href = url1;
      }
    };
    // TODO: fill in url
    url = "http://0.0.0.0:80/" + "query?url=" + src
    xhttp.open("GET", url, true);
    xhttp.send();
});
