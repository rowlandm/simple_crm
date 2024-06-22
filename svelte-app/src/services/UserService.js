// src/services/UserService.js

const apiUrl = 'http://127.0.0.1:8000/persons/'; // Replace with your API endpoint URL

export async function getUsers() {
  try {
    const response = await fetch(apiUrl);
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching users:', error);
    throw error;
  }
}

