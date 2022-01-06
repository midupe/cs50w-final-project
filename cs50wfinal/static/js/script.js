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
                    <th scope="row" onclick="copyClipboard('${results.results.host}${results.results.urls[i].shorten}')" style="cursor: pointer;" colspan="2">
                        ${results.results.urls[i].url}
                    </th>
                    <td style="cursor: pointer;"><a href="${results.results.host}${results.results.urls[i].shorten}" target="_blank" style="text-decoration: none;">/${results.results.urls[i].shorten}</a></td>
                    `;
                if (results.results.urls[i].userNotSignIn_id == null) {
                    newHtmlCode += `
                        <th>
                            ${results.results.urls[i].visits}
                        </th>
                    `;
                } else {
                    newHtmlCode += `
                        <th>
                        <a href="/login">Sign in required</a>
                        </th>
                    </tr>
                    `;
                }
            }
            listUrls.innerHTML = newHtmlCode;
            document.getElementById("listaDosURLS").style.display = "block";
        });
}


document.addEventListener("DOMContentLoaded", function (event) {
    try {
        var intervalID = window.setInterval(myCallback, 3000);

        function myCallback() {
            updateUrlsList();
        }
    } catch {
        //pass
    }
});

