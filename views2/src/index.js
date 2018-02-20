var robotImageUrl = 'https://s3-us-west-2.amazonaws.com/chrisnielsen/robot.png';
// Cartoon vector designed by Freepik
// http://www.freepik.com/free-photos-vectors/cartoon

// Pre-load image
$('<img/>')[0].src = robotImageUrl;


$('form').submit(function (event) {
  event.preventDefault();
  
  var $userInput = $(this).find('input');
  var message = $userInput.val();

  var settings = {
  "async": true,
  "crossDomain": true,
  "url": "http://localhost:8000/api/fbk",
  "method": "GET",
  "mode": "no-cors",
  "crossDomain" : "true",
  "headers": {

    "content-type": "text/html",
    "content-type": "application/json",
    "cache-control": "no-cache",
    'Access-Control-Allow-Origin': '*'
    // "postman-token": "2d8aac14-e7d4-e674-7122-639305bf19a6"
  },
  // "data": '{"msg":" '+ message +' "}'
      // "data": "{\"msg\":\"Hello\"}"
}

function createInput(value){
    
    var input = $('<input type="button" value='+ value +' />');
    return input;
    // input.appendTo($(".content"));

   }


$.ajax(settings).done(function (response) {
  // obj = JSON.parse(response);
  // console.log(obj[0]);
  // debugger

  console.log(response);
  // addToLog(response[1].question,false)
  // debugger
  addToLog(response[1].question,false);
  // createInput(response[1].pre_ans1),
  //   createInput(response[1].pre_ans2),
  //   createInput(response[1].pre_ans3),
  //   createInput(response[1].pre_ans4),

  var1 = createInput(response[1].pre_ans1);
  var2 = createInput(response[1].pre_ans2);
  var3 = createInput(response[1].pre_ans3);
  var4 = createInput(response[1].pre_ans4);



  var1.appendTo($(".content"));
  var2.appendTo($(".content"));
  var3.appendTo($(".content"));
  var4.appendTo($(".content"));

  });


  if (!_.isEmpty(message)) {
    addToLog(message, true);  
    // sendMessgeToServer(message);
  }
  
  $userInput.val('');
});



// function sendMessgeToServer(message) {
//     setTimeout(function () {
//       addToLog(message, false);
//     }, 2000);
// }

// function pre_defined_answer()






function addToLog(message, user) {
  var $message = $('<div class="message animated container"></div>');
  
  if (!user) {
    var $picture = $('<img src="' + robotImageUrl + '"></img>');
    $message.append($picture);
  }
  
  var $content = $('<div class="content"></div>');
  $content.html(message);
  $message.append($content);
  
  var $log = $('.log');
  $log.append($message);
  
  if (user) {
    $message.addClass('user');
  } 
  
  $log.animate({ scrollTop: $log[0].scrollHeight }, "slow", 'linear');
  
  setTimeout(function () {
    if (user) {
      $message.addClass('user');
      $message.addClass('fadeInRightBig');
    } else {
      $message.addClass('fadeInLeftBig');
    }
  }, 0);
}