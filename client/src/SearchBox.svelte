<script>
    import { fly } from 'svelte/transition'
    let searchterm = ''
</script>

<style>
    .search-bar {
        width: 50vw;
        height: 2.5rem;
        border-radius: 5px;
    }
</style>

<input name="search" type="text" class="search-bar" placeholder="Search recipes..." bind:value={searchterm} transition:fly={{ x: -200, y: -200, duration: 500 }} />
