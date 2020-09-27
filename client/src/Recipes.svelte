<script>
    import axios from 'axios'
    import RecipeSummary from './RecipeSummary.svelte'
    import Loading from './Loading.svelte'

    let recipes = ''

    function GetRecipes() {
        return axios
            .get(`${process.env.APIURL}/api/recipes/`)
            .then((results) => {
                return results.data
            })
            .catch((err) => {
                console.error(err.toJSON())
            })
    }
    recipes = GetRecipes()
</script>

<style>
    .recipes {
        display: flex;
        flex-flow: row wrap;
        gap: 1em;
    }
</style>

<h1>Recent recipes</h1>
<div class="recipes">
    {#await recipes}
        <Loading />
    {:then data}
        {#each data as recipe}
            <RecipeSummary {recipe} />
        {/each}
    {/await}
</div>
