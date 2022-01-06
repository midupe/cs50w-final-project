function copyClipboard(text) {
    /* Copy the text inside the text field */
    navigator.clipboard.writeText(text);

    /* Alert the copied text */
    alert(`${text} copied to clipboard`);
}

function submitShortenUrl() {
    form = document.getElementById("shortenUrlForm");
    $.post("newUrl", $(form).serialize(), function (data) {
        updateUrlsList();
        document.getElementById("url").value = "";
        copyClipboard(data.urlShorten);
    });

}

function updateUrlsList() {
    fetch('/urls/1', {
        method: 'GET'
    }).then(response => response.json())
        .then(results => {
            var listUrls = document.getElementById("listUrls");
            var newHtmlCode = "";
            for (let i = 0; i < results.results.urls.length; i++) {
                if (results.results.urls[i].url.length > 27) {
                    results.results.urls[i].url = results.results.urls[i].url.slice(0, 27) + "..."
                }
                newHtmlCode += `
                <tr>
                    <td scope="row" onclick="copyClipboard('${results.results.host}${results.results.urls[i].shorten}')" style="cursor: pointer;" colspan="2">
                        ${results.results.urls[i].url}
                    </td>
                    <th style="cursor: pointer;"><a href="${results.results.host}${results.results.urls[i].shorten}" target="_blank" style="text-decoration: none;">/${results.results.urls[i].shorten}</a></th>
                    `;
                if (results.results.urls[i].userNotSignIn_id == null) {
                    newHtmlCode += `
                        <td>
                            ${results.results.urls[i].visits}
                            <i class="fas fa-copy" style="float: right; cursor: pointer !important;" aria-label="Copy" onclick="copyClipboard('${results.results.host}${results.results.urls[i].shorten}')"></i>
                        </td>
                    `;
                } else {
                    newHtmlCode += `
                        <td>
                        <a href="/login" style="text-decoration: none; color: black;"><i class="far fa-eye-slash"></i></a>
                        <i class="fas fa-copy" style="float: right; cursor: pointer !important;" aria-label="Copy" onclick="copyClipboard('${results.results.host}${results.results.urls[i].shorten}')"></i>
                        </td>
                    </tr>
                    `;
                }
            }
            if (results.results.urls.length > 0) {
                listUrls.innerHTML = newHtmlCode;
                document.getElementById("listaDosURLS").style.display = "block";
            }
        });
}


document.addEventListener("DOMContentLoaded", function (event) {
    try {
        if (document.getElementById("accessFeatures") == null) {
            var intervalID = window.setInterval(myCallback, 3000);

            function myCallback() {
                updateUrlsList();
            }
        }
    } catch {
        //pass
    }
});

