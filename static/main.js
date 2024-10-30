function dewdd() {
    let inputValue = $('.uacas').val();

    $.ajax({
        url: '/send',
        type: 'POST',
        data: JSON.stringify({ input: inputValue }),
        contentType: 'application/json',
        success: function(response) {
            console.log('Response:', response);
            if (response['status'] === "success") {
                $('#dddasx').append(inputValue + " sounding <br><br>");
            }
        }
    });
}

function ewcwe() {
    $.ajax({
        url: '/get_index',
        type: 'POST',
        data: JSON.stringify({ input: "dd" }),
        contentType: 'application/json',
        success: function(response) {
            $('.ccwefe').val(response['index']);
        }
    });
}

function vsvwe() {
    let inputValue = $('.ccwefe').val();

    $.ajax({
        url: '/index_change',
        type: 'POST',
        data: JSON.stringify({ input: inputValue }),
        contentType: 'application/json',
        success: function(response) {
            if (response['status'] === "success") {
                $('#dddasx').append("edit index sound on " + inputValue + "<br><br>");
            }
        }
    });
}