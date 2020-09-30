<script>
    import { setModal } from './stores.js'
    import RecipeAdd from './RecipeAdd.svelte'
    import SearchBox from './SearchBox.svelte'

    let hidden = true

    function ShowSearchOverlay(ev) {
        setModal.set({ showModal: true, component: SearchBox, header: 'Search recipes' })
        hidden = false
    }

    function HideSearchOverlay(ev) {
        setModal.set({ showModal: false, component: SearchBox, header: 'Search recipes' })
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
            <a class="button" href="#" on:click|preventDefault={ShowSearchOverlay}>🔎</a>
            <div class="toolbar-right" />
        </span>
    </div>
</nav>
<!-- {#if !hidden}
    <div class="search-overlay" transition:fade on:click|preventDefault|self={HideSearchOverlay} />
{/if} -->
