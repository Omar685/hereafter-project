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

  function mediaScreen() {
    function handleMediaQuery(mediaQuery) {
      if (mediaQuery.matches) {
        $("main").css({ "marginTop": navHeight * 2 + "px", "marginLeft": "0" });
        $("aside").removeClass("vh-100");
        $(".show .close").css("top", navHeight * 2 + "px");
        $(".body-comment").addClass("z-3");

      } else {
        $(".show .close").css("top", navHeight + "px");
        $("main").css({ "marginLeft": asideWidth + "px", "marginTop": asideWidth + "px" });
        $("aside").addClass("vh-100");

      }
    }

    let mediaQuery = window.matchMedia("(max-width: 780px)");

    handleMediaQuery(mediaQuery);

    mediaQuery.addListener(handleMediaQuery);
  }

  mediaScreen()




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


$(".cover-image img,.post .image-post img").on("click", function () {
  let imgSrc = $(this).attr("src");
  $(".show img").attr("src", imgSrc)
  $(".profile .show").fadeIn(500).addClass("d-flex")
});




$(".profile .show .close").on("click", function () {
  $(".profile .show").fadeOut(500, function () {
    $(".profile .show").removeClass("d-flex")
  })
})


$(".show-more p").hover(
  function () {
    $(this).addClass("text-primary-emphasis");
  },
  function () {
    $(this).removeClass("text-primary-emphasis");
  }
);

$(".show-more p").on("click", function () {
  const $this = $(this);
  $this.siblings(".more-info").toggle(300);
  $this.text($this.text() === 'Show more' ? 'Show less' : 'Show more');
  $this.parent().toggleClass("open");
});

// cooments show
$(".post .comment").on("click", function () {
  $(this).siblings(".body-comment").fadeIn(300).addClass("d-flex");
});

$(".post .close").on("click", function () {
  $(this).closest(".body-comment").fadeOut(300).removeClass("d-flex");
});

// share show

$(".post .share").on("click", function () {
  $(this).siblings(".body-share").fadeIn(300).addClass("d-flex");
});

$(".post .close").on("click", function () {
  $(this).closest(".body-share").fadeOut(300).removeClass("d-flex");
});
$(".parentComment").on("click", function () {
  var $contentElement = $(this).nextAll(".body-comment").find(".content-comment");
  var content = $contentElement.html();

  if (content) {
    console.log("match");
  } else {
    $contentElement.html('<img src="static/images/no-comment.jpg" class="position-relative top-50 start-50 translate-middle rounded no-comment" alt="Not Found"> ');
  }
});
