function readURLforDisplay(input)
{

    if(input.files && input.files[0])
    {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#cover_img').attr('src',e.target.result);

        };

        reader.readAsDataURL(input.files[0])

    }
}