<?php
  echo "lol";
  $_POST = "lol"


$address = '';
$port = 1425;

if (($sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP)) === false) {
    echo "socket_create() failed: reason: " . socket_strerror(socket_last_error()) . "\n";
}

$result = socket_connect($sock, $address, $service_port);

socket_write($socket, $_POST, strlen($in));


 ?>
