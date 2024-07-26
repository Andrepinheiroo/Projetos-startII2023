<?php
session_start();

$email = "felipemelo@msn.com";

$_SESSION['email'] = $email;

echo $_SESSION['email'];

?>
