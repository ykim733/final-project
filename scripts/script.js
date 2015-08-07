// Create a clone of the menu, right next to original.

function stickIt() {

  var orgElementPos = $('.original').offset();
  orgElementTop = orgElementPos.top;

  if ($(window).scrollTop() >= (orgElementTop)) {
    // scrolled past the original position; now only show the cloned, sticky element.

    // Cloned element should always have same left position and width as original element.
    orgElement = $('.original');
    coordsOrgElement = orgElement.offset();
    leftOrgElement = coordsOrgElement.left;
    widthOrgElement = orgElement.css('width');
    $('.cloned').css('left',leftOrgElement+'px').css('top',0).css('width',widthOrgElement).show();
    $('.original').css('visibility','hidden');
  } else {
    // not scrolled past the menu; only show the original menu.
    $('.cloned').hide();
    $('.original').css('visibility','visible');
  }
}

function enableTab(id) {
    var el = document.getElementById(id);
    console.log("called");
    el.onkeydown = function(e) {
        console.log("here " + e.keyCode);
        if (e.keyCode === 9) { // tab was pressed

            // get caret position/selection
            var val = this.value,
                start = this.selectionStart,
                end = this.selectionEnd;


            // set textarea value to: text before caret + tab + text after caret
            this.value = val.substring(0, start) + '\t' + val.substring(end);

            // put caret at right position again
            this.selectionStart = this.selectionEnd = start + 1;

            // prevent the focus lose
            return false;

        }
    };
}

$(window).bind("scroll", function() {
        if ($(this).scrollTop() > 1000) {
            $("#game_center").fadeIn(3000);
        }
        else {
            $("#game_center").stop().fadeOut('3000');
        }
    });


//$('.carousel')89uh'u/0.carousel()

$(document).ready(function() {
  $('.menu').addClass('original').clone().insertAfter('.menu').addClass('cloned').css('position','fixed').css('top','0').css('margin-top','0').css('z-index','500').removeClass('original').hide();
  scrollIntervalID = setInterval(stickIt, 10);
  // Enable the tab character onkeypress (onkeydown) inside textarea...
  // ... for a textarea that has an `id="my-textarea"`
  enableTab('essay');
  $('.carousel').carousel()

})
