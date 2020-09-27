<script>
    import axios from 'axios'
    let name = ''
    let email = ''
    let successmsg = ''
    let errormsg = ''

    function RegisterUser(ev) {
        ev.preventDefault()
        // form validation
        const newuser = {
            name,
            email,
            username: email
        }
        const u = CreateUser(newuser)
            .then((d) => {
                name = ''
                email = ''
                successmsg = `Username ${email} created with ID ${d.data.userid}.`
            })
            .catch((err) => {
                console.log(err.toJSON())
                errormsg = err.response.data.error
            })
    }

    async function CreateUser(newuser) {
        return await axios.post(`${process.env.APIURL}/api/user/add`, newuser)
    }
</script>

<style>
    #errormsg {
        color: red;
    }
</style>

<h1>Register account</h1>
<form on:submit={RegisterUser}>
    <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" required bind:value={name} />
    </div>
    <div class="form-group">
        <label for="email">Email Address:</label>
        <input type="email" name="email" id="email" required bind:value={email} />
    </div>
    <button type="submit">Register</button>
</form>

{#if successmsg}
    <div id="successmsg">{successmsg}</div>
{/if}
{#if errormsg}
    <div class="alert alert-danger" role="alert">{errormsg}</div>
{/if}
