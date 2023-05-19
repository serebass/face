Explanation
The textToMorse function takes a string as an argument and returns the Morse code representation of the string.
The function first checks if the argument is a string. If it is not a string, the function throws an error.

The function then creates a dictionary object that maps each character to its Morse code representation.
The dictionary object is used to convert each character in the input string to its Morse code representation.

The function converts the input string to uppercase and iterates through each character in the string.
For each character, the function looks up its Morse code representation in the dictionary object and appends it to a
string variable. The function also adds a space character after each Morse code representation to separate the
characters.

Finally, the function logs the input string and its Morse code representation to the console and returns the Morse code
representation.

Possible bugs
The function assumes that the input string contains only alphanumeric characters and spaces. If the input string
contains other characters, the function may not return the correct Morse code representation.
The function does not handle errors that may occur when logging to the console.
Possible improvements
Add input validation to ensure that the input string contains only alphanumeric characters and spaces.
Add error handling for logging to the console.
Add an optional argument to allow the user to specify the separator character between Morse code representations.
