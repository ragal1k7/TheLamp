<?php

function set_hand(bool $close): void {
    if ($close) {
        error_log("Рука СЖАТА");
    } else {
        error_log("Рука РАЗЖАТА");
    }
}

if (isset($_GET['action'])) {
    $action = $_GET['action'];
    if ($action === 'on') {
        set_hand(true);
        die("CLOSED");
    } elseif ($action === 'off') {
        set_hand(false);
        die("OPENED");
    }
}

http_response_code(400);
echo "Use ?action=on or ?action=off";
