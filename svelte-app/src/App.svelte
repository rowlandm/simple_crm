<!-- src/App.svelte -->
<script>
  import { Router, Link, Route } from 'svelte-routing';
  import AddPerson from './routes/AddPerson.svelte';


  import { onMount } from 'svelte';
  import Table from './components/Table.svelte';
  import { getUsers } from './services/UserService';



  let users = [];

  onMount(async () => {
    try {
      users = await getUsers();
    } catch (error) {
      console.error('Error loading users:', error);
      // Handle error as needed (e.g., show error message)
    }
  });
</script>


<main>
  <h1>User List</h1>
  <Table {users} />
</main>





<style>
  main {
    padding: 20px;
  }
</style>

