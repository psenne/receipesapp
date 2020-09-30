<script>
    import {  fly, slide } from 'svelte/transition'
    import axios from 'axios'
    import Icon from 'svelte-awesome'
    import { plus, beer, refresh, comment, codeFork, camera, ban } from 'svelte-awesome/icons'
    import { faArrowCircleLeft, faArrowCircleRight } from '@fortawesome/free-solid-svg-icons'
    import { faPlusSquare } from '@fortawesome/free-regular-svg-icons'
    import ImageReader from './ImageReader.svelte'

    var title = ''
    var ingredients = ''
    var directions = ''
    var preptime = ''
    var cooktime = ''
    var imageURL = ''
    var summary = ''

    var frame = 1

    function AddRecipe(ev) {
        ev.preventDefault()
        let recipe = { title, ingredients, directions, preptime, cooktime, imageURL, summary }
        alert('form submitted')
        // return axios
        //     .post(`${process.env.APIURL}/api/recipe/add`, recipe)
        //     .then((response) => console.log(response.data))
        //     .catch((err) => {
        //         console.error(err.toJSON())
        //         alert(err.response.data.reason)
        //     })
    }
</script>

<style>
    .addrecipe-frame{
        width: calc(100vw - 4em);
        max-width: 32em;
        max-height: calc(100vh - 4em);
        overflow: hidden;
        padding: 1em;
        border-radius: 0.2em;
        background: white;
    }
    label {
        display: block;
    }
    .recipe-info {
        min-height: 35vh;
    }
    .buttons {
        display: flex;
        justify-content: space-between;
    }
    button{
        background-color: var(--success-bkgd);
        color: var(--success-text);
    }
    .nav-button {
        color: var(--pink);
    }
    .section {
        height: 300px;
        position: absolute;
    }
    .section input[type='text'] {
        width: 400px;
    }
    .section textarea {
        width: 400px;
        height: 150px;
    }
</style>


<div class="addrecipe-frame">
    <h1>Add Recipe</h1>
    <form on:submit|preventDefault={AddRecipe}>
        <div class="recipe-info">
            {#if frame == 1}
                <div class="section" in:fly={{ x: 200, duration: 500 }} out:fly={{ x: -200, duration: 500 }}>
                    <label for="">Title</label>
                    <input type="text" name="title" bind:value={title} required />
                    <label for="">Summary</label>
                    <textarea name="summary" id="summary" bind:value={summary} />
                    <ImageReader name="imageURL" bind:imageURL />
                </div>
            {/if}
    
            {#if frame == 2}
                <div class="section" in:fly={{ x: 200, duration: 500 }} out:fly={{ x: -200, duration: 500 }}>
                    <label for="">🥗 Ingredients</label>
                    
                    <textarea name="ingredients" id="ingredients" bind:value={ingredients} />
                </div>
            {/if}
    
            {#if frame == 3}
                <div class="section" in:fly={{ x: 200, duration: 500 }} out:fly={{ x: -200, duration: 500 }}>
                    <label for="">📑 Directions</label>
                    <textarea name="directions" id="directions" bind:value={directions} />
                </div>
            {/if}
            {#if frame == 4}
                <div class="section" in:fly={{ x: 200, duration: 500 }} out:fly={{ x: -200, duration: 500 }}>
                    <label for="">⏱ Prep Time</label>
                    <input type="number" step="15" name="preptime" bind:value={preptime} />
                    minutes
                    <label for="">⏱ Cook Time</label>
                    <input type="number" step="15" name="cooktime" bind:value={cooktime} />
                    minutes
                </div>
            {/if}
    
        </div>
        <div class="buttons">
            <a href="#" class="nav-button" on:click|preventDefault={() => frame--}>
                {#if frame > 1}
                    <Icon data={faArrowCircleLeft} scale="2"/>
                {/if}
            </a>
            <a href="#" class="nav-button" on:click|preventDefault={() => frame++}>
                {#if frame < 4}
                    <Icon data={faArrowCircleRight}  scale="2"/>
                {/if}
            </a>
            {#if frame == 4}
                <button type="submit">
                    <Icon data={faPlusSquare} /> Add Recipe
                </button>
            {/if}
        </div>
    </form>
</div>
