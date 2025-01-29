const { spawnSync } = require('child_process');


// array
arr = ['node.py', 'jack', 'goa']

// Execute the Python script synchronously
const pythonProcess = spawnSync('python', arr, {
    encoding: 'utf-8'
});

// Check for errors
if (pythonProcess.error) {
    console.error('Error executing Python script:', pythonProcess.error);
    return;
}

// Capture and log the output
const output = pythonProcess.stdout;
const response = JSON.parse(output.toString())
console.log(typeof output);
console.log('Python:\n', output);
console.log('Response:\n', response.response);
