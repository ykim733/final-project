// $(document).ready(function()

  function enableTab(id) {
      var el = document.getElementById(id);
      el.onkeydown = function(e) {
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


       function () {
           $("#essay").on("button", function(e) {
               e.preventDefault()
                });
             });





  // Enable the tab character onkeypress (onkeydown) inside textarea...
  // ... for a textarea that has an `id="my-textarea"`
  enableTab('essay');

  function bold() {
      var x = $('#description-box');
      if (x.css("font-weight") !== "bold") {
         (x.css("font-weight", "bold"))


      $function e(){
         e.preventDefault()
         $.post(essay)
         }

)
      }
  }
