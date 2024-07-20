// let mailInputRegister = $(".register .mailInput");
// let nameInputRegister = $(".register .nameInput");
// let passInputRegister = $(".register .passInput");

// let emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
// let passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;


// function clearForm() {
//     mailInputRegister.val(null).removeClass("is-valid is-invalid");
//     nameInputRegister.val(null).removeClass("is-valid is-invalid");
//     passInputRegister.val(null).removeClass("is-valid is-invalid");
// }


$(document).ready(function () {
  let navHeight = $("nav").outerHeight(true);
  let asideWidth = $("aside").outerWidth(true);
  let asideHeight = $("aside").outerHeight(true);

  $("aside").css("top", navHeight + "px");

  function handleMediaQuery(mediaQuery) {
    if (mediaQuery.matches) {
      $("main").css({ "marginTop": navHeight + "px", "marginLeft": "0" });
      $("aside").removeClass("vh-100");
    } else {
      $("main").css({ "marginLeft": asideWidth + "px", "marginTop": "0" });
    }
  }

  let mediaQuery = window.matchMedia("(max-width: 780px)");

  handleMediaQuery(mediaQuery);

  mediaQuery.addListener(handleMediaQuery);

  $("aside ul li").on("click", function () {
    $("aside ul li").removeClass("active");
    $("aside ul li i").removeClass("active");

    $(this).addClass("active");
    $(this).find("i").addClass("active");
  });

  $(window).on("scroll", function () {
    if ($(window).scrollTop() > asideHeight / 2) {
      $(".top").fadeIn(500);
    } else {
      $(".top").fadeOut(500);
    }
  });
});
$(".top").on("click", function () {
  $("html, body").animate({ scrollTop: 0 }, "slow");
});


$(".heart").on("click", function () {
  $(this).find("i").toggleClass("active");
});