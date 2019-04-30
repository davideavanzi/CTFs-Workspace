<?php

require_once '../config.inc.php';

class User {
    var $username;
    var $role;

    function __construct($username) {
        $this->username = $username;
        $this->role = 'user';
    }

    function is_admin() {
        return $role == "admin";
    }
}

function register($username, $password) {
    global $db;
    $q = "insert into users (username, password, role) values (:user, :pass, 'user')";
    $stmt = $db->prepare($q);
    $stmt->bindParam(":user", $username, PDO::PARAM_STR);
    $stmt->bindParam(":pass", $password, PDO::PARAM_STR);
    return $stmt->execute();
}

function login($username, $password) {
    global $db;
    $q = "select username, role from users where username = :user and password = :pass limit 1;";
    $stmt = $db->prepare($q);
    $stmt->bindParam(":user", $username, PDO::PARAM_STR);
    $stmt->bindParam(":pass", $password, PDO::PARAM_STR);
    if(!$stmt->execute()) {
        return false;
    }
    if($stmt->rowCount() === 1) {
        $row = $stmt->fetch();
        if(!row)
            return false;
        return new User($row['username'], $row['role']);
    } else {
        return false;
    }
}

function set_session($user) {
    global $sign_secret;
    $s = serialize($user);
    $hm = hash_hmac('sha512', base64_encode($s), $sign_secret);
    if(!setcookie('s', base64_encode($hm) . ':' . base64_encode($s))) {
        print_r("Can't set the cookie!");
    }
}

function check_session() {
    global $_COOKIE, $sign_secret;
    $a = explode(':', $_COOKIE['s']);
    $hm = hash_hmac('sha512', $a[1], $sign_secret);
    if(base64_decode($a[0]) === $hm) {
        return unserialize(base64_decode($a[1]));
    }
    return NULL;
}

function get_secret($user) {
    global $db;
    $q = "select secret from users where username = :user;";
    $stmt = $db->prepare($q);
    $stmt->bindParam(':user', $user);
    if($stmt->execute()) {
        while($row = $stmt->fetch()) {
            return $row['secret'];
        }
    }
}

