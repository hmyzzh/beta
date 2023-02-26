/*!
=========================================================
* JoeBlog Landing page
=========================================================

* Copyright: 2019 DevCRUD (https://devcrud.com)
* Licensed: (https://devcrud.com/licenses)
* Coded by www.devcrud.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

// smooth scroll
$(document).ready(function(){
    $(".navbar .nav-link").on('click', function(event) {

        if (this.hash !== "") {

            event.preventDefault();

            var hash = this.hash;

            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 700, function(){
                window.location.hash = hash;
            });
        } 
    });
});

function ImgID_finder(sw,dictt) {
  var pic;
  pic=dictt[sw]
  document.getElementById(sw).src = pic;
}

function ImgID_finder1() {
  return "https://live.staticflickr.com/65535/52711514698_eae834868b_h.jpg";
}
