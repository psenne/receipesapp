<script>
    import { fade } from 'svelte/transition'
    import axios from 'axios'
    import Loading from './Loading.svelte'
    import marked from 'marked'

    export let params
    let recipe = ''

    function GetRecipe() {
        return axios
            .get(`${process.env.APIURL}/api/recipe/${params.id}`)
            .then((results) => {
                return results.data
            })
            .catch((err) => {
                console.error(err.toJSON())
            })
    }
    recipe = GetRecipe()
</script>

<style>
    .recipe {
        margin: 0.5rem;
        background-color: beige;
        border-radius: 5px;
    }
    .title {
        background-color: var(--light-header-bkgd);
        color: var(--dark-pink);
        margin: 0 0 1em 0;
        padding: 1em 2em;
    }
    .recipe img {
        width: 100%;
        height: 300px;
        object-fit: cover;
    }
    figcaption{
        font-size: 0.8em;
        font-weight: 700;
    }
    .recipe .body {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(1fr, 1fr));
    }
    .recipe .ingredients,
    .recipe .directions {
        padding: 1rem;
        margin: 1rem;
    }
    .recipe .ingredients {
        /* background-color: hsla(60, 56%, 80%, 0.4); */
        background-color: teal;
    }
    .recipe .directions{
        background-color: tomato;
    }
    .recipe footer {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        grid-template-rows: 1fr 1fr;
    }
    .recipe footer h2 {
        grid-column-start: 1;
        grid-column-end: 4;
    }
</style>

{#await recipe}
    <Loading />
{:then data}
    <div class="recipe" in:fade>
        <div class="header">
            <h1 class="title">{data.title}</h1>
            <figure>
                <img src={data.image || `${process.env.APIURL}/images/noimage.gif`} alt="" />
                <figcaption>{data.summary || ''}</figcaption>
            </figure>
        </div>
        <div class="body">
            <div class="ingredients">
                <h2>Ingredients</h2>
                {@html marked(data.ingredients)}
            </div>
            <div class="directions">
                <h2>Directions</h2>
                {@html marked(data.directions)}
            </div>
        </div>
    </div>
{:catch err}
    <div class="error">{err.message}</div>
{/await}
