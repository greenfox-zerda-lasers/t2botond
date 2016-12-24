
/*********************************************
This relay module demo toggles both relay
channels every two seconds, logging the new
values to the console upon latching.
*********************************************/

var tessel = require('tessel');
var relaylib = require('relay-mono');

var relay = relaylib.use(tessel.port['A']);


    var code = "-- . .-. .-. -.--  -.-. .... .-. .. ... - -- .- ...";
    // var code = '...---... ';
    var i = 0;
    var signal = true

    function step(){
      switch (code[i]) {
        case "-":
          delay = 900;
        break;
        case ".":
          delay = 300;
        break;
        case " ":
          delay = 2000;
          signal = false
        break;
      }

      if(signal==false){
        if (i < code.length - 1){
          i++;
        } else {
          i = 0;
        }
      }

      if (signal){
        console.log('on: ' + code[i], i, code.length)
        relay.turnOn(2, function () {})
        signal = false
      } else {
        console.log('off' + code[i])
        relay.turnOff(2, function (){})
        signal = true
        delay = 300
      }
      setTimeout(step,delay);
    }
    step();

// // Wait for the module to connect
// relay.on('ready', function relayReady () {
//   console.log('Ready! Toggling relays...');
//   setInterval(function toggle() {
//
//     relay.toggle(2, function toggleTwoResult(err) {
//       if (err) console.log("Err toggling 2", err);
//     });
//   }, 1000); // Every 2 seconds (2000ms)
// });
//
// // When a relay channel is set, it emits the 'latch' event
// relay.on('latch', function(channel, value) {
//   console.log('latch on relay channel ' + channel + ' switched to', value);
// });
