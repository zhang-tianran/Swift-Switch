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
      code: "document.querySelector('div.product-detail-main-image-container img').src"
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
    // console.log("Image source", src);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        const response = JSON.parse(this.responseText);
        let url1 = response.a;
        let url2 = response.b;
        let url3 = response.c;
      }
    };
    // TODO: fill in url
    url = "127.0.0.1"
    xhttp.open("GET", url + "/query?url=" + src, true);
    xhttp.send();
});
