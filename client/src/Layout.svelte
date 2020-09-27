<script>
    // import User from './User.svelte';
    // import AddUser from './AddUser.svelte';
    import Recipes from './Recipes.svelte'
    import MessageBox from './MessageBox.svelte'
    import Toolbar from './Toolbar.svelte'

    let showMessageBox = false
    let messageBoxTitle = ''
    let messageBoxText = ''

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
    main {
        display: grid;
        grid-template-areas:
            'header'
            'toolbar'
            'content'
            'footer';
        grid-template-rows: 100px min-content 1fr 100px;
        grid-template-columns: 1fr;
        background-color: ivory;
    }
    main .content {
        grid-row: content;
        grid-column: content;
        padding: 1rem;
    }
    main .toolbar {
        grid-row: toolbar;
        grid-column: toolbar;
        background-color: hotpink;
    }
    main footer {
        grid-row: footer;
        grid-column: footer;
        background-color: rgba(0, 0, 0, 0.25);
    }
    main header {
        background-color: hotpink;
        background-image: url('/bkgd.png');
        box-shadow: 2px 0 5px black;
        grid-row: header;
        grid-column: header;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    main header img{
        opacity: 75%;
    }
</style>

<main>
    <header>
        <img src="piacere_sm.png" alt="" />
    </header>
    <div class="toolbar">
        <Toolbar />
    </div>
    <div class="content">
        <slot />
    </div>
    <footer>by andream.com</footer>
</main>
