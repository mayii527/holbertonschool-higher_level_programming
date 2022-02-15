//fetches and displays the value of hello
//from that fetch in the HTML tag DIV#hello.
$('header').getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function(resp){
    $('#hello').text(resp.hello);
});
