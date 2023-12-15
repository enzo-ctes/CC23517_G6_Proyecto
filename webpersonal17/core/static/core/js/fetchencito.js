let url = "https://jsonplaceholder.typicode.com/todos/1"
let query = "coment?postID=1"

fetch()
      .then(response => response.json())
      .then(json => console.log(json))