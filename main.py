/**
 * Converts text to Morse code
 * @param {string} text The text to be converted to Morse code
 * @returns {string} The Morse code representation of the text
 */
function textToMorse(text) {
    // Check if the argument is a string
    if (typeof text !== 'string') {
        throw new Error('The argument must be a string');
    }

    // Create a dictionary with the Morse code representation of each character
    const morseCodeDict = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        ' ': ' '
    };

    // Convert the text to uppercase
    text = text.toUpperCase();

    // Convert the text to Morse code
    let morseCode = '';
    for (let i = 0; i < text.length; i++) {
        const character = text[i];
        morseCode += morseCodeDict[character] + ' ';
    }

    // Log the result
    console.log(`Text: ${text}\nMorse code: ${morseCode}`);

    // Return the Morse code
    return morseCode;
}
