const dfd = require('danfojs-node');
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

// Function to prompt user for input
function promptInput(question) {
    return new Promise((resolve) => {
        readline.question(question, (answer) => {
            resolve(answer);
        });
    });
}

// Main function to collect input and create a DataFrame
async function main() {
    // Prompt the user for input
    const age = await promptInput('Enter your age: ');
    const gender = await promptInput('Enter your gender: ');
    const income = await promptInput('Enter your income: ');

    // Create a dictionary from the input
    const data = {
        Age: [parseInt(age)], // Convert age to a number
        Gender: [gender],
        Income: [parseFloat(income)] // Convert income to a number
    };

    // Create a single-row DataFrame from the dictionary
    const df = new dfd.DataFrame(data);

    // Print the DataFrame
    console.log('\nSingle-Row DataFrame:');
    df.print();

    // Close the readline interface
    readline.close();
}

// Run the main function
main();