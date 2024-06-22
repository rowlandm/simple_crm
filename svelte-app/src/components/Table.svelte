<!-- src/components/Table.svelte -->
<script>
  export let users = [];

  // State variables for sorting
  let sortKey = null;
  let sortDirection = 1; // 1 for ascending, -1 for descending

  // State variable for search term
  let searchTerm = '';

  function sortBy(key) {
    if (sortKey === key) {
      sortDirection = -sortDirection; // Toggle direction if same key clicked
    } else {
      sortKey = key;
      sortDirection = 1; // Default to ascending when changing sort key
    }

    // Perform sorting
    users = users.slice().sort((a, b) => {
      const modifier = sortDirection === 1 ? 1 : -1;
      if (a[key] < b[key]) return -1 * modifier;
      if (a[key] > b[key]) return 1 * modifier;
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
      <th on:click={() => sortBy('id')}>ID {sortKey === 'id' ? (sortDirection === 1 ? '▲' : '▼') : ''}</th>
      <th on:click={() => sortBy('full_name')}>Name {sortKey === 'full_name' ? (sortDirection === 1 ? '▲' : '▼') : ''}</th>
      <th on:click={() => sortBy('email')}>Email {sortKey === 'email' ? (sortDirection === 1 ? '▲' : '▼') : ''}</th>
      <th on:click={() => sortBy('job_title')}>Job Title {sortKey === 'job_title' ? (sortDirection === 1 ? '▲' : '▼') : ''}</th>
      <th on:click={() => sortBy('last_note_date')}>Last Note Date {sortKey === 'last_note_date' ? (sortDirection === 1 ? '▲' : '▼') : ''}</th>
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

