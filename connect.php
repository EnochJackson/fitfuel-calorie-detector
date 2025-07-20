<?php
$host = "localhost";  // Change if using a remote database
$user = "root";       // Your MySQL username
$pass = "Qwaszx086*";           // Your MySQL password
$dbname = "calories";  // Your database name

$conn = new mysqli($host, $user, $pass, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
