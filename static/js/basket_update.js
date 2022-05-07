// Update quantity on click
$(".update-link").click(function(e) {
    let form = $(this).prev(".update-form");
    form.submit();
});

// Remove item and reload on click
$(".remove-item").click(function(e) {
    let csrfToken = getCookie("csrftoken")
    let itemId = $(this).attr("id").split("remove_")[1];
    let size = $(this).data("product_size");
    let url = `/basket/remove/${itemId}/`;
    let data = {"csrfmiddlewaretoken": csrfToken, "product_size": size};

    $.post(url, data)
        .done(function() {
            location.reload();
        });
});


// function from https://www.w3schools.com/js/js_cookies.asp
function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }