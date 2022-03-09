var oDoc, sDefTxt;
var hiddenField;
function initDoc() {
  oDoc = document.getElementById("textBox");
  hiddenField = document.getElementById("myDoc");
  sDefTxt = oDoc.innerHTML;
  // if (document.compForm.switchMode.checked) 
  // {
  //   setDocMode(true);
  // }
}

function formatDoc(sCmd, sValue) {
  if (validateMode()) {
    document.execCommand(sCmd, false, sValue);
    oDoc.focus();
  }
}

function validateMode() {
  // if (!document.compForm.switchMode.checked) {
  //   return true;
  // }
  // alert('Uncheck "Show HTML".');
  // oDoc.focus();
  return true;
}

function setDocMode(bToSource) {
  var oContent;
  if (bToSource) {
    oContent = document.createTextNode(oDoc.innerHTML);
    oDoc.innerHTML = "";
    var oPre = document.createElement("pre");
    oDoc.contentEditable = false;
    oPre.id = "sourceText";
    oPre.contentEditable = true;
    oPre.appendChild(oContent);
    oDoc.appendChild(oPre);
    document.execCommand("defaultParagraphSeparator", false, "div");
  } else {
    if (document.all) {
      oDoc.innerHTML = oDoc.innerText;
    } else {
      oContent = document.createRange();
      oContent.selectNodeContents(oDoc.firstChild);
      oDoc.innerHTML = oContent.toString();
    }
    oDoc.contentEditable = true;
  }
  oDoc.focus();
}

function printDoc() {
  if (!validateMode()) {
    return;
  }
  var oPrintWin = window.open(
    "",
    "_blank",
    "width=450,height=470,left=400,top=100,menubar=yes,toolbar=no,location=no,scrollbars=yes"
  );
  oPrintWin.document.open();
  oPrintWin.document.write(
    '<!doctype html><html><head><title>Print<\/title><\/head><body onload="print();">' +
    oDoc.innerHTML +
    "<\/body><\/html>"
  );
  oPrintWin.document.close();
}


// function showBold()
// {
//   var oDoc = document.getElementById("textBox");
//   var sDefTxt = oDoc.innerHTML;
//   var arr = oDoc.getElementsByTagName('b');

//   for(let i=0; i<arr.length; i++)
//   {
//     console.log((arr[i])['textContent']);
//   }
//   // console.log(());
// }

// function getContent()
// {
//   var textBox = document.getElementById("textBox");
//   var result = document.getElementById("result");

//   console.log(textBox.innerHTML);
//   result.innerHTML = String(textBox.innerHTML);
// }




function getContent() {
  let content = document.getElementById("textBox");
  // alert(content.innerText);
  // if(content.innerText == "")
  // return content.innerHTML;
  return content.innerText;
}


function formattedContent() {
  let content = oDoc.innerHTML;
  console.log(content);
  return content;
}

// function exe()
// {
//       var formdata = [1, 2, 3 ,4 ];
//       var xhttp = new XMLHttpRequest();
//       xhttp.open("POST", "http://127.0.0.1:5000/", true); 
//       xhttp.setRequestHeader("Content-Type", "application/json");
//       xhttp.onreadystatechange = function() {
//         if (this.readyState == 4 && this.status == 200) {
//           // Response
//           var response = this.responseText;
//         }
//       };
//       var data = {name:'yogesh',salary: 35000,email: 'yogesh@makitweb.com'};
//       xhttp.send(JSON.stringify(data));


//   //     document.ajax({
//   //       type: 'POST',
//   //     contentType: 'application/json',
//   //     data: JSON.stringify("values", formdata),
//   //     dataType: 'json',
//   //     url: 'http://127.0.0.1:5000/',
//   //     success: function (e) {
//   //         console.log(e);
//   //         window.location = "http://127.0.0.1:5000/";
//   //     },
//   //     error: function(error) {
//   //     console.log(error);
//   // }
//   // });
// }
//     $(document).ready( function() {
//       $('#submit').click(function() {
//          var formdata = serialize();
//          $.ajax({
//                type: 'POST',
//               contentType: 'application/json',
//               data: JSON.stringify(formdata),
//               dataType: 'json',
//               url: 'http://127.0.0.1:5000/',
//               success: function (e) {
//                   console.log(e);
//                   window.location = "http://127.0.0.1:5000/";
//               },
//               error: function(error) {
//               console.log(error);
//           }
//           });
//       });
// });




// const data = document.getElementById("info")
const button = document.getElementById("submit");
// Create an array of cars to send to the server:
let cars = [
  { "make": "Porsche", "model": "911S" },
  { "make": "Mercedes-Benz", "model": "220SE" },
  { "make": "Jaguar", "model": "Mark VII" }
];

cars = {'abc':1}


// Create an event listener on the button element:
button.onclick = function () {

  var content = oDoc.innerHTML;
  console.log(oDoc.getElementsByTagName('font'));
  $.ajax({
      url: 'http://127.0.0.1:5000/results',
      data: JSON.stringify({'content':content}),
      dataType:'json',
      contentType: 'application/json;charset=UTF-8',
      type: 'POST',
      success: function(response) {
          console.log(response);
      },
      error: function(error) {
          console.log(error);
      }

  });
}


