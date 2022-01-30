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

const setVisible = (elementOrSelector, visible) => 
  (typeof elementOrSelector === 'string'
    ? document.querySelector(elementOrSelector)
    : elementOrSelector
  ).style.display = visible ? 'block' : 'none';

// function countDivs() {
//   countTags("div", function(num) {
//       console.log("Found %i divs", num);
//   });
// }

// document.getElementById("myButton").addEventListener("click", countDivs);
// countDivs();
getSource(function(src) {
    setVisible('.page', false);
    setVisible('#loading', true);
    console.log("Image source", src);
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        const response = JSON.parse(this.responseText);

        var num_components = 3;
        var title = document.querySelectorAll(".title");
        var cloth_img = document.querySelectorAll(".cloth-img");
        var ul = document.querySelectorAll(".info");
        var link = document.querySelectorAll(".link");

        for (var i=1; i <= num_components; i++) {

        title[i-1].innerHTML += (response[i+'title']);
        cloth_img[i-1].src = (response[i+'img']);
        // ul[i].innerHTML += ('<li><b>Thrift platform: </b>'+ response.[i+brand] +'</li>');
        ul[i-1].innerHTML += ('<li><b>Brand: </b>'+ response[i+'brand'] +'</li>');
        ul[i-1].innerHTML += ('<li><b>Price: </b>'+ response[i+'prize'] +'</li>');
        ul[i-1].innerHTML += ('<li><b>Size: </b>'+ response[i+'size'] +'</li>');
        link[i-1].href = (response[i+'link']);
        }

        // title[i].innerHTML += (response[i+'title']);
        // cloth_img[i].src = (response[i+'img']);
        // // ul[i].innerHTML += ('<li><b>Thrift platform: </b>'+ response.[i+brand] +'</li>');
        // ul[i].innerHTML += ('<li><b>Brand: </b>'+ response[i+'brand'] +'</li>');
        // ul[i].innerHTML += ('<li><b>Price: </b>'+ response[i+'prize'] +'</li>');
        // ul[i].innerHTML += ('<li><b>Size: </b>'+ response[i+'size'] +'</li>');
        // link[i].href = (response[i+'link]');


        setVisible('.page', true);
        setVisible('#loading', false);

      }
    };
    // TODO: fill in url
    url = "http://0.0.0.0:80/" + "query?url=" + src
    xhttp.open("GET", url, true);
    xhttp.send();
});
