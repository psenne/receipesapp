<script>
    import { link } from 'svelte-spa-router'
    import { format } from 'date-fns'
    import marked from 'marked'
    import Icon from 'svelte-awesome'
    import { beer, refresh, comment, codeFork, camera, ban } from 'svelte-awesome/icons'
    import { faArrowCircleLeft, faArrowCircleRight, faCalendar } from '@fortawesome/free-solid-svg-icons'
    import { faPlusSquare, faUser, faClock } from '@fortawesome/free-regular-svg-icons'
    import FlipCard from './FlipCard.svelte'

    // var title = ''
    // var ingredients = ''
    // var directions = ''
    // var preptime = ''
    // var cooktime = ''
    // var imageURL = ''
    export let recipe = {}

    var { id, title, summary, image, author, user_id, timestamp } = recipe
    var flipped = false

    function ShowBackside() {
        flipped = true
    }
    function ShowFrontside() {
        flipped = false
    }
</script>

<style>
    h1 {
        font-size: 1rem;
        font-weight: bold;
    }
    .subtitle {
        padding: 0.5em;
        text-transform: uppercase;
        font-size: 0.8rem;
        font-weight: bold;
        line-height: 1.2rem;
    }
    img {
        width: 250px;
        height: 250px;
    }
    hr {
        opacity: 0.25;
    }
    .recipe-summary-content {
        display: grid;
        place-content: center;
        width: 100%;
        height: 100%;
    }
    .recipe-summary-content p {
        margin: 0;
        padding: 0;
        font-size: 0.8rem;
        font-style: italic;
    }
    .recipe-summary-content p.summary {
        font-style: normal;
        font-size: 1.2em;
    }
    .recipe-summary {
        background-color: rgba(0, 0, 0, 6%);
        box-shadow: 1px 1px 3px rgba(0, 0, 0, 15%);
        flex: 0 1 200px;
    }
</style>

<div class="recipe-summary" on:mouseover={ShowBackside} on:mouseout={ShowFrontside}>
    <a href="/recipe/{id}" use:link><FlipCard>
    <img src={image || `${process.env.APIURL}/images/noimage.gif`} alt="" slot="front" />
    <div class="recipe-summary-content" slot="back">
    <p class="summary">
    {@html marked(summary || '')}
    </p>
    <p>Prep Time: 45 minutes</p>
    <p>Cooking Time: 30 minutes</p>
    </div>
    </FlipCard></a>
    <div class="subtitle">
        <h1>
            <a href="/recipe/{id}" use:link>{title}</a>
        </h1>
        <hr />
        <div class="author">
            <Icon data={faUser} />
            <a href="/user/{user_id}" use:link>{user_id}</a>
        </div>
        <div class="time">
            <Icon data={faCalendar} />
            <time datetime={timestamp}>{format(new Date(timestamp), 'MMM d, yyyy')}</time>
        </div>
    </div>
</div>
