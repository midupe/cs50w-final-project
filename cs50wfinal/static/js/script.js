function copyClipboard(text) {
    /* Copy the text inside the text field */
    navigator.clipboard.writeText(text);

    /* Alert the copied text */
    alert("Url copied to clipboard");
}

function submitShortenUrl(){
    form = document.getElementById("shortenUrlForm");
    $.post("", $(form).serialize(), function(data){
        // TODO GET json response com shortenurl
        //copair resultado para o clipboard
        // atualizar UI com novo site
    });

    copyClipboard("caraca");
}