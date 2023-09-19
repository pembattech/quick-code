# Interactive Character Counter for Textarea

This is a simple HTML document that demonstrates an interactive character counter for a textarea input field. It provides real-time character count feedback as the user types in the textarea.

## Usage

To use this character counter, simply open the HTML file in a web browser. It presents a textarea where you can enter text, and a character count will be displayed at the bottom right corner of the textarea.

## Features

- Real-time character count feedback as you type.
- The character count is limited to a maximum of 255 characters (adjustable in the `maxlength` attribute of the textarea).
- The character count is hidden when the textarea is not in focus, providing a clean user interface.

## How it Works

This interactive character counter is implemented using HTML, CSS, and JavaScript. The key components are:

- HTML: It contains a textarea element and a character count span.
- CSS: Styling rules for positioning the character count and hiding it by default.
- JavaScript: Event listeners are used to show/hide the character count based on textarea focus and to update the count as the user types.
