<script>
    import { routes } from './routes.js'
    import Router from 'svelte-spa-router'
    import Layout from './Layout.svelte'
    import MessageBox from './MessageBox.svelte'
    import Modal from './Modal.svelte'
    import { setModal, setMessageBox } from './stores.js'

    let showModal = false
    let component = null
    let header = null

    let messageBox = {
        showMessageBox: false,
        messageBoxTitle: '',
        messageBoxText: ''
    }

    setModal.subscribe((value) => {
        header = value.header
        showModal = value.showModal
        component = value.component
    })
    setMessageBox.subscribe((params) => {
        messageBox = { ...params }
    })

    function DisplayMessage({ title, text }) {
        messageBoxTitle = title
        messageBoxText = text
        showMessageBox = true
    }

    function CloseMessage() {
        messageBoxTitle = ''
        messageBoxText = ''
        showMessageBox = false
    }
</script>

<style>
    :global(:root) {
        --pink: hotpink;
        --blackpink: #1f000f;
        --success-bkgd: darkgreen;
        --success-text: white;
        --light-header-bkgd: #ff69b452;
    }
</style>

<Layout>
    <Router {routes} />
</Layout>
<MessageBox {messageBox} hidden={!messageBox.showMessageBox} on:closeMessageBox={CloseMessage} />
{#if showModal}
    {@debug showModal}
    <Modal>
        <h1 slot="header">{header}</h1>
        <svelte:component this={component} />
    </Modal>
{/if}
