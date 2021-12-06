
const postForm = document.querySelector("#create_form");
function handleSubmit(postForm) {
    postForm.addEventListener("submit", e => {
        e.preventDefault();
        formData = new FormData(postForm);
        fetch('/', {
            method: 'POST',
            body: formData,
        })
            .then(response => response.json())
            .then(data => {
                postForm.reset();
                html_to_insert =`<ul>
                <li>Title: ${ data.title }</li>
                <li>Author: ${ data.owner.username }</li>
                <li>Created: Just now </li>
                <li>Content: ${ data.content } </li>

            </ul>`;
                document.getElementById('posts').insertAdjacentHTML('beforeend', html_to_insert);

            })
            .catch((error) => {
                console.error('Error:', error);
            });
    })
}

handleSubmit(postForm)
