<?php
/**
 * Заглушка управления рукой.
 * Замените содержимое на реальные команды (GPIO, Serial, вызов скрипта и т.п.)
 */
function set_hand(bool $close): void {
    if ($close) {
        // Здесь код для СЖАТИЯ руки
        error_log("Рука СЖАТА");  // пишем в консоль сервера (терминал)
    } else {
        // Здесь код для РАЗЖАТИЯ руки
        error_log("Рука РАЗЖАТА");
    }
}

// Обработка команд
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

// Если команды нет – возвращаем ошибку
http_response_code(400);
echo "Use ?action=on or ?action=off";