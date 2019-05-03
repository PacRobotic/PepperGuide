<?php
// Lire la base de donnees et creer un json pour les salles administrative
// ATTENTION, ne pas mettre de " dans la base de données

header("Access-Control-Allow-Origin: *");

// Lecture base de données picardap
$hostname = "localhost:/var/run/mysql/mysql_tp.sock";
$username = "picardap";
$password = "s7n5hpeq";
$database_name = "picardap";

$conn = mysql_pconnect($hostname, $username, $password) or die("Impossible de se connecter : ". mysql_error());    
mysql_select_db($database_name, $conn)or die("Impossible de sélectionner la base: ". mysql_error()); 
mysql_query("SET NAMES UTF8");

$sql = "SELECT * FROM `Salles` WHERE `type`='Administration' ORDER BY `localisation`";
$result = mysql_query($sql) or die("Requête invalide: ". mysql_error()."\n".$sql);

$first = true;
$json = "[";
while ($row = mysql_fetch_assoc($result)){
	if(!$first){
		$json .= ",";
	}else{
		$first = false;
	}
	$json .= "{\"id\":";
	$json .= $row["id"];
	$json .= ", \"localisation\":\"";
	$json .= $row["localisation"];
	$json .= "\", \"type\":\"";
	$json .= $row["type"];
	$json .= "\", \"description\":\"";
	$json .= $row["description"];
	$json .= "\"}";
}
$json .= "]";
echo $json;