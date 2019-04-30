<?php

error_reporting(0);

$db_name = 'asdrubale';
$db_host = 'db';
$db_username = 'ermenegilda';
$db_password = 'supersecret';

$sign_secret = '3@#54!%&aiobe:th1s1sav3radandomandd1ff1culttoguesss3cr3t!';

try {
    $db = new PDO("mysql:host=$db_host;dbname=$db_name;charset=utf8", $db_username, $db_password);
} catch(PDOException $e) {
    die("Error connecting to the database $db_name. If the problem persists, please contact an administrator (chall@necst.it).");
}

