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

// const data = document.getElementById("info")
const button = document.getElementById("submit");
// Create an array of cars to send to the server:
let cars = [
  { "make": "Porsche", "model": "911S" },
  { "make": "Mercedes-Benz", "model": "220SE" },
  { "make": "Jaguar", "model": "Mark VII" }
];

cars = {'abc':1}



// Font size: >= 14
// Formatting: h1 to h5


// Create an event listener on the button element:
button.onclick = function () {

  var content = oDoc.innerHTML;
  let fontElements = oDoc.getElementsByTagName('font');
  let fontTitles = []; 

  // selecting eligible elements from group of font elements
  for (const element of fontElements) {
    if(element.getAttribute('size')>=4)
    {
      fontTitles.push(element);
    }
  }



  // console.log($("h2").next());

  let headingArray = [
    oDoc.getElementsByTagName('h1'),
    oDoc.getElementsByTagName('h2'),
    oDoc.getElementsByTagName('h3'),
    oDoc.getElementsByTagName('h4'),
    oDoc.getElementsByTagName('h5')
  ];




  // define the object structure
// {
  
// }
  // for each type of head elements
  for (const headTag of headingArray) {

    // for each head array element,
    for (const ele of headTag) {
  
      // if current h1 element is immediately followed by a paragraph then
      if($(ele).next().is($('p')))
      {
        // get the paragraph
        let paragraphs = $(ele).next();
  
  
        // look into the paragraph and extract important features from it
        // like bold, italic, underline, hyperlink text
        let boldArray = new Array();
        let italicArray = new Array();
        let underlineArray = new Array();
        let hyperlinkArray = new Array();
        
        for (const para of paragraphs) {
          boldArray.push(para.getElementsByTagName('b'));
          italicArray.push(para.getElementsByTagName('i'));
          underlineArray.push(para.getElementsByTagName('u'));
          hyperlinkArray.push(para.getElementsByTagName('a'));
        }
        
        console.log(ele);
        console.log(boldArray);
        console.log(italicArray);
        console.log(underlineArray);
        console.log(hyperlinkArray);
      } 
         
    }    
  }


  // console.log(fontTitles);
  // console.log(h1);
  // console.log(h2);
  // console.log(h3);
  // console.log(h4);
  // console.log(h5);

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
          // console.log(error);
      }

  });
}


