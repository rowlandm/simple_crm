<script>
    let name = '';
    let age = '';
    
    function addPerson() {
        // Implement logic to add the person (e.g., send data to backend)
        console.log('Adding person:', { name, age });
        
        // Optionally, you can navigate back to the list or another page
        // For simplicity, let's assume you're using a router
        // $router.navigate('/persons'); // Example router navigation
    }
</script>

<h1>Add a Person</h1>

<form on:submit|preventDefault={addPerson}>
    <label>
        Name:
        <input type="text" bind:value={name} />
    </label>
    <label>
        Age:
        <input type="number" bind:value={age} />
    </label>
    <button type="submit">Add Person</button>
</form>

