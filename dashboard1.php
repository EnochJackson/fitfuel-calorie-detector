<?php
session_start();
if (!isset($_SESSION["user_id"])) {
    echo json_encode(["error" => "User not logged in"]);
    exit();
}

$conn = new mysqli("localhost", "root", "Qwaszx086*", "calories");
if ($conn->connect_error) {
    die(json_encode(["error" => "Connection failed: " . $conn->connect_error]));
}
$user_id = $_SESSION["user_id"];
$stmt = $conn->prepare("SELECT username, age, weight, height, bmi, bmr, recommended_calories, breakfast, lunch, dinner, snacks FROM users WHERE id=?");
$stmt->bind_param("i", $_SESSION["user_id"]);
$stmt->execute();
$stmt->bind_result($username, $age, $weight, $height, $bmi, $bmr, $recommended_calories, $breakfast, $lunch, $dinner, $snacks);
$stmt->fetch();
$stmt->close();
$conn->close();

echo json_encode([
    "username" => $username,
    "age" => $age,
    "weight" => $weight,
    "height" => $height,
    "bmi" => $bmi,
    "bmr" => $bmr,
    "recommended_calories" => $recommended_calories,
    "breakfast" => $breakfast,
    "lunch" => $lunch,
    "dinner" => $dinner,
    "snacks" => $snacks
]);
?>
