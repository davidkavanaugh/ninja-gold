$(document).ready(() => {
  $.ajax({
    url: "/gold_api",
    success: function (result) {
      $("#activities").append(result.activities);
    },
  });
});
