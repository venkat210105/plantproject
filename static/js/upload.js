document.querySelector('input[type="file"]').addEventListener('change', function (event) {
    const file = event.target.files[0];
    const fileSizeKB = file.size / 1024; // Convert bytes to KB

    if (fileSizeKB < 15 || fileSizeKB > 50) {
        alert('Please upload an image between 15KB and 50KB.');
        event.target.value = ''; // Clear the file input
    } else {
        alert('Image size is valid. Proceed with upload.');
    }
});