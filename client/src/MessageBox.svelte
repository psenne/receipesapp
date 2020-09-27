<script>
    export let messageBoxTitle = ''
    export let messageBoxText = ''
    export let hidden = true

    import { createEventDispatcher } from 'svelte'
    import { fly, fade } from 'svelte/transition'

    const dispatch = createEventDispatcher()
</script>

<style>
    .message-box-overlay {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background-color: rgba(0, 0, 0, 0.5);
        filter: blur(5px);
    }
    .message-box {
        background-color: antiquewhite;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.5);
        position: absolute;
        top: 0;
        width: 50%;
        margin-inline: auto;
        min-height: 200px;
    }
</style>

{#if !hidden}
    {@debug messageBoxTitle}
    <div class="message-box-overlay" />
    <div class="message-box" transition:fly={{ y: -200 }}>
        <h1 class="title">{messageBoxTitle}</h1>
        <div class="text">{messageBoxText}</div>
        <div class="footer">
            <button on:click={() => dispatch('closeMessageBox')}>Ok</button>
        </div>
    </div>
{/if}
