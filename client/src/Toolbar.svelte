<script>
    import { setModal } from './stores.js'
    import RecipeAdd from './RecipeAdd.svelte'
    import {fade} from 'svelte/transition'

    let searchterm = ''
    let hidden = true

    function ShowSearchOverlay(ev) {
        hidden = false
    }

    function HideSearchOverlay(ev) {
        hidden = true
    }
</script>

<style>
    .nav {
        display: flex;
        flex-flow: row nowrap;
        justify-content: space-between;
        align-items: center;
    }
    .button {
        display: inline-block;
        width: auto;
        padding: 0.5rem;
        text-decoration: none;
        color: var(--blackpink);
        text-align: center;
        border: 1px solid hsl(0 0% 0% / 50%);
        background-color: hsl(0 0% 100% / 25%);
        border-radius: 1px;
    }
    .button-group {
        display: flex;
    }
    .button-group a {
        margin-right: -1px;
    }
    /* .toolbar-left{
        margin-left: 1rem;
    } */
    .toolbar-right {
        margin-right: 1rem;
    }
    .search-bar {
        width: 50vw;
        height: 2.5rem;
        border-radius: 5px;    
    }
    .btn-submit-search {
        margin-left: -24px;
    }
    .search-overlay {
        display: grid;
        place-content: center;
        position: absolute;
        top: 0;
        bottom: 0;
        right: 0;
        left: 0;
        background: hsl(0 0% 0% / 75%);
        z-index: 1000;
    }
    .hidden {
        display: none;
    }
</style>

<nav class="nav">
    <div class="toolbar-left">
        <span class="button-group">
            <button
                class="button"
                on:click|preventDefault={(ev) => {
                    setModal.set({ showModal: true, component: RecipeAdd, header: 'Add new recipe' })
                }}>
                ➕
            </button>
            <a href="#" class="button">Categories</a>
        </span>
    </div>
    <div class="toolbar-right"><a class="btn-submit-search" href="#" on:click|preventDefault={ShowSearchOverlay}>🔎</a></div>
</nav>
{#if !hidden}
    <div class="search-overlay" transition:fade="{{ duration: 500 }}" on:click|preventDefault|self={HideSearchOverlay}>
        <input name="search" type="text" class="search-bar" placeholder="Search recipes..." bind:value={searchterm} />
    </div>
{/if}