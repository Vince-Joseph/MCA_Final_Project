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

// function getContent() {
//   let content = document.getElementById("textBox");
//   // alert(content.innerText);
//   // if(content.innerText == "")
//   // return content.innerHTML;
//   return content.innerText;
// }


// function formattedContent() {
//   let content = oDoc.innerHTML;
//   // console.log(content);
//   return content;
// }

// const data = document.getElementById("info")
const button = document.getElementById("submit");
// Create an array of cars to send to the server:
// let cars = [
//   { "make": "Porsche", "model": "911S" },
//   { "make": "Mercedes-Benz", "model": "220SE" },
//   { "make": "Jaguar", "model": "Mark VII" }
// ];

// cars = {'abc':1}



/*  *************************************** Creation of JSON format starts here  ****************************************  */
/*  *********************************************************************************************************************  */


let formattedInfo = new Array();



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


  // get all heading elements from the document
  let headingArray = [
    oDoc.getElementsByTagName('h1'),
    oDoc.getElementsByTagName('h2'),
    oDoc.getElementsByTagName('h3'),
    oDoc.getElementsByTagName('h4'),
    oDoc.getElementsByTagName('h5')
  ];




  // define the object structure
  /* 
      {
        [
          {
            heading: "first heading", 
            subtitle: "subtitle", 
            paraContent: "following paragraph", 
            bold:[["bold1", "bold2", "bold3"], ["bold1", "bold2", "bold3"], ["bold1", "bold2", "bold3"]],
            italic:[["italic1", "italic2", "italic3"], ["italic1", "italic2", "italic3"]],
            underline:[["underline1", "underline2", "underline3"], ["underline1", "underline2", "underline3"], ["underline1", "underline2", "underline3"]],
            hyperlink:[["link1", "link1", "link1", "link1"], ["link1", "link1", "link1", "link1"], ["link1", "link1", "link1", "link1"]]
          }
        ]
      }
    */      
      
      
      // for each type of head elements
      for (const headTag of headingArray) {
        
        // for each head array element,
        for (const ele of headTag) {

            let currentObj = {};

            // set the title of the current object 
            currentObj.heading = ele.textContent;
            let subtitle = "";
            let paraContent = "";

            // if current h1 element is immediately followed by a paragraph then
            if($(ele).next().is($('p')))
            {
              // get the paragraphs
              let p = $(ele).next();
              let paragraphs = new Array();

              // retrieving all the paragraph elements under current title
              while($(p).is($('p')))
              {
                paragraphs.push(p);
                p = $(p).next();
              }              
              
              // look into the paragraphs under current title and extract important features from it
              // like bold, italic, underline, hyperlink text
              let boldTextArray = new Array();
              let italicTextArray = new Array();
              let underlineTextArray = new Array();
              let hyperlinkTextArray = new Array();

              for (const para of paragraphs) {
                        
                paraContent += para[0].textContent;

                boldTextArray.push(returnArray(para[0].getElementsByTagName('b'), false));
                italicTextArray.push(returnArray(para[0].getElementsByTagName('i'), false));
                underlineTextArray.push(returnArray(para[0].getElementsByTagName('u'), false));
                hyperlinkTextArray.push(returnArray(para[0].getElementsByTagName('a'), true));
                
              }
              
              // add other extracted elements into current object
              currentObj.bold = boldTextArray;
              currentObj.italic = italicTextArray;
              currentObj.underline = underlineTextArray;
              currentObj.hyperlink = hyperlinkTextArray;
              currentObj.paraContent = paraContent; // the paragraph's content altogether              
             
            
            } 
            // else if heading has a subtitle then
            // the format is <div> <h2>...</h2> </div>
            else if(
                ($(ele).next().is($('div')) && (($(ele).next()).children().is($('h2')))) ||
                ($(ele).next().is($('div')) && (($(ele).next()).children().is($('h3')))) ||
                ($(ele).next().is($('div')) && (($(ele).next()).children().is($('h4')))) ||
                ($(ele).next().is($('div')) && (($(ele).next()).children().is($('h5')))) ||
                ($(ele).next().is($('div')) && (($(ele).next()).children().is($('h6')))) 
                                            )
            {
              // console.log(((($(ele).next()).children())));

              // get the subtitle only if subtitle text is defiend by a tag lesser than then main title
              if((ele.tagName < (($(ele).next()).children())))
              {
                subtitle = (($(ele).next()).children())[0].textContent;
                // console.log(subtitle);
              }
              currentObj.subtitle = subtitle;

            }

            // now push the current object to the array of objects
            formattedInfo.push(currentObj);
    }    

    console.log(formattedInfo);
  }

  // this method accepts a collection of html elements and returns the text content inside them as an array
  function returnArray(collection, isAnchorElement)
  {
    let arr = new Array();
  
    if(isAnchorElement)
    {
      for (let i = 0; i < collection.length; i++) {
        let text = (collection[i].getAttribute('href')).trim();
        // console.log(collection[i]);
        // console.log(text);
        if(text !== "" && text !== " ")
          arr.push(text);
      }    
    }
    else
    {
      for (let i = 0; i < collection.length; i++) {
        let text = (collection[i].textContent).trim();
        // console.log(text);
        if(text !== "" && text !== " ")
          arr.push(text);
      }
    }
    return arr;
  }

  // console.log(fontTitles);
  // console.log(h1);
  // console.log(h2);
  // console.log(h3);
  // console.log(h4);
  // console.log(h5);

  $.ajax({
      url: 'http://127.0.0.1:5000/results',
      data: JSON.stringify({'content':formattedInfo}),
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


