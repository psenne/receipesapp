<script>
    import {link} from 'svelte-spa-router'
    import marked from 'marked';
    // var title = ''
    // var ingredients = ''
    // var directions = ''
    // var preptime = ''
    // var cooktime = ''
    // var imageURL = ''
    export let recipe = {}
    
    var { id, title,  summary, image, author, user_id } = recipe;
</script>

<style>
    h1 {
        font-size: 1rem;
        font-weight: bold;
    }
    p {
        font-size: 0.8rem;
        font-style: italic;
    }
    img {
        float: left;
        margin-right: 5px;
        width: 200px;
        height: 150px;
    }
    .recipe-summary {
        box-shadow: 0 0 5px rgba(0, 0, 0, 25%);
    }
</style>

<div class="recipe-summary">
    <img src={image || `${process.env.APIURL}/images/noimage.gif`} alt="" />
    <div class="recipe-summary-content">
        <h1><a href="/recipe/{id}" use:link>{title}</a></h1>
        <p>{@html marked(summary || "🍞🍞🍞")}</p>
        <p>🔪 45m 👩‍🍳 30m</p>
    </div>
    <div class="author">Author: <a href="/user/{user_id}" use:link>{user_id}</a></div>
</div>
