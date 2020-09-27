<script>
  import axios from "axios";

  let userInfo = "";
  let userID = 1;

  function getUser(userid) {
    return axios
      .get(`${process.env.APIURL}/api/user/${userid}`)
      .then((results) => {
        return results.data;
      })
      .catch((err) => {
        console.log(err.response);
        throw err;
      });
  }

  function setUserID(ev) {
    userID = ev.target.value;
  }
</script>

<form>
  <h1>Get user information by ID</h1>
  <div class="form-group">
    <label for="userID">User ID:</label>
    <input
      name="userID"
      class="form-control"
      type="number"
      bind:value={userID}
      on:change={setUserID} />
  </div>
  <button
    type="submit"
    class="btn btn-primary"
    on:click={(ev) => {
      ev.preventDefault();
      userInfo = getUser(userID);
    }}>
    Get user information
  </button>
</form>

{#if userInfo}
  {#await userInfo}
    <div>Loading user information...</div>

  {:then data}
    <h1>User Information:</h1>
    <p>{JSON.stringify(data.user)}</p>

  {:catch error}
    <p class="alert alert-danger" role="alert">{error.message}</p>
  {/await}
{/if}
