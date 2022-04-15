// Update price on product details page when changing size
$('#id_product_size').change(function() {
    let size = $("#id_product_size").val();
    let base_price = parseFloat($("#base_price").val());
    let size_multi = {
        "A6": 0,
        "A5": 1,
        "A4": 2,
        "A3": 3,
        "A2": 4,
        "A1": 5};
    let new_price = Math.round(base_price * (1.1 ** size_multi[size]))-0.01;
    $(".lead").html(new_price);
});