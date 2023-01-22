<?php

// get the url from the form
$url = $_POST["url"];

// if the form has been submitted
if (!empty($url)) {
    // get the contents of the url
    $contents = file_get_contents($url);

    // display the contents
    echo $contents;
}

?>
<!DOCTYPE html>
<html>
<head>
    <title>Simple Web Browser</title>
</head>
<body>
    <form method="post">
        <label for="url">URL:</label>
        <input type="text" id="url" name="url" placeholder="Enter URL">
        <input type="submit" value="Go">
    </form>
</body>
</html>
