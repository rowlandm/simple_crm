<!-- src/components/Table.svelte -->
<script>
  export let users = [];
  let searchTerm = '';
  
  function sortBy(key) {
    users = users.sort((a, b) => {
      if (a[key] < b[key]) return -1;
      if (a[key] > b[key]) return 1;
      return 0;
    });
  }
</script>

<style>
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  
  th, td {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
  }
  
  th {
    background-color: #f2f2f2;
    cursor: pointer;
  }
  
  input[type="text"] {
    padding: 5px;
    margin-bottom: 10px;
  }
</style>

<input type="text" placeholder="Search..." bind:value={searchTerm}>

<table>
  <thead>
    <tr>
      <th on:click={() => sortBy('id')}>ID</th>
      <th on:click={() => sortBy('full_name')}>Name</th>
      <th on:click={() => sortBy('email')}>Email</th>
      <th on:click={() => sortBy('job_title')}>Job Title</th>
      <th on:click={() => sortBy('last_note_date')}>Last Note Date</th>
    </tr>
  </thead>
  <tbody>
    {#each users as user}
      {#if user.full_name.toLowerCase().includes(searchTerm.toLowerCase())}
        <tr>
          <td>{user.id}</td>
          <td>{user.full_name}</td>
          <td>{user.email}</td>
          <td>{user.job_title}</td>
          <td>{user.last_note_date}</td>
        </tr>
      {/if}
    {/each}
  </tbody>
</table>

