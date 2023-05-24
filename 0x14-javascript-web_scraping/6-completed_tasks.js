#!/usr/bin/node

const request = require('request');

// Retrieve the API URL from command line arguments
// The first argument (index 2) is the API URL
const apiUrl = process.argv[2];

// Perform a GET request to the specified API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
  } else {
    try {
      // Parse the response body as JSON
      const todosData = JSON.parse(body);

      // Create an object to store the number of completed tasks per user ID
      const completedTasksByUser = {};

      // Iterate through the todos and count completed tasks for each user
      todosData.forEach((todo) => {
        if (todo.completed) {
          const userId = todo.userId;
          if (completedTasksByUser[userId]) {
            completedTasksByUser[userId]++;
          } else {
            completedTasksByUser[userId] = 1;
          }
        }
      });

      // Print the number of completed tasks by user ID
      Object.entries(completedTasksByUser).forEach(([userId, count]) => {
        console.log(`User ID ${userId}: ${count} completed tasks`);
      });
    } catch (error) {
      console.error(`Error parsing JSON: ${error}`);
    }
  }
});
