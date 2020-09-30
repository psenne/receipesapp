<script>
    import { createEventDispatcher, onDestroy } from 'svelte'
    import {fade} from 'svelte/transition'
    import { setModal } from './stores.js'

    const dispatch = createEventDispatcher()
    const close = () => {
        dispatch('close')
        setModal.set({showModal: false})
    }

    let modal

    const handle_keydown = (e) => {
        if (e.key === 'Escape') {
            close()
            return
        }

        if (e.key === 'Tab') {
            // trap focus
            const nodes = modal.querySelectorAll('*')
            const tabbable = Array.from(nodes).filter((n) => n.tabIndex >= 0)

            let index = tabbable.indexOf(document.activeElement)
            if (index === -1 && e.shiftKey) index = 0

            index += tabbable.length + (e.shiftKey ? -1 : 1)
            index %= tabbable.length

            tabbable[index].focus()
            e.preventDefault()
        }
    }

    const previously_focused = typeof document !== 'undefined' && document.activeElement

    if (previously_focused) {
        onDestroy(() => {
            previously_focused.focus()
        })
    }
</script>

<style>
    .modal-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.75);
        display: grid;
        place-content: center;
    }

    .header{
        color: white;
        font-size: 1.2rem;;
    }

    .modalx {
        position: absolute;
        left: 50%;
        top: 50%;
        width: calc(100vw - 4em);
        max-width: 32em;
        max-height: calc(100vh - 4em);
        overflow: hidden;
        transform: translate(-50%, -50%);
        padding: 1em;
        border-radius: 0.2em;
        background: white;
    }

    .btn-close {
        display: block;
        float: right;
        cursor: pointer;
        color: var(--pink);
    }
</style>

<svelte:window on:keydown={handle_keydown} />

<div class="modal-background" on:click|self|preventDefault={close}>
    <div class="modal" role="dialog" aria-modal="true" bind:this={modal} transition:fade>
        <slot />
    </div>
</div>