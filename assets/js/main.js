
$("#id_month > a").on("click", function(e){
    let id = $(this).data("id");
    $("#id_table").load("http://127.0.0.1:8000/load-table/" + id + "/");
});