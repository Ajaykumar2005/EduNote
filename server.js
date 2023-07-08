const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// In-memory user data store
const users = [];

// Middleware to parse request body
app.use(bodyParser.urlencoded({ extended: true }));

// Serve the sign-up page
app.get('/signup', (req, res) => {
  res.sendFile(__dirname + '/signup.html');
});

// Handle sign-up POST request
app.post('/signup', (req, res) => {
  const { username, password } = req.body;

  // Check if the username is already taken
  const existingUser = users.find((user) => user.username === username);
  if (existingUser) {
    return res.send('Username already taken');
  }

  // Create a new user and store in the data store
  const newUser = { username, password };
  users.push(newUser);

  res.send('Sign up successful');
});

// Serve the login page
app.get('/login', (req, res) => {
  res.sendFile(__dirname + '/login.html');
});

// Handle login POST request
app.post('/login', (req, res) => {
  const { username, password } = req.body;

  // Find the user in the data store
  const user = users.find((user) => user.username === username && user.password === password);

  if (user) {
    // Successful login
    res.send('Login successful');
  } else {
    // Invalid credentials
    res.send('Invalid username or password');
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
