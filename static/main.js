function dewdd() {
    var inputValue = $('.uacas').val();

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