$(document).ready(function(){
  // Activate Carousel with a specified interval
  $("#myCarousel").carousel({interval: 500});
        
  // Enable Carousel Indicators
  $(".item1").click(function(){
    $("#myCarousel").carousel(0);
  });
  $(".item2").click(function(){
    $("#myCarousel").carousel(1);
  });
  $(".item3").click(function(){
    $("#myCarousel").carousel(2);
  });
    
  // Enable Carousel Controls
  $(".carousel-control-prev").click(function(){
    $("#myCarousel").carousel("prev");
  });
  $(".carousel-control-next").click(function(){
    $("#myCarousel").carousel("next");
  });
});

// tooltip 

// $(document).ready(function(){
//   $('[data-toggle="tooltip"]').tooltip();
// });

// $(document).ready(function(){
// 	$(window).scroll(function () {
// 			if ($(this).scrollTop() > 50) {
// 				$('#back-to-top').fadeIn();
// 			} else {
// 				$('#back-to-top').fadeOut();
// 			}
// 		});
// 		// scroll body to 0px on click
// 		$('#back-to-top').click(function () {
// 			$('body,html').animate({
// 				scrollTop: 0
// 			}, 400);
// 			return false;
// 		});
// });