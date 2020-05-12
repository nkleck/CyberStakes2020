<?php

// REMOTE_ADDR not working because CONTAINERS are the FUTURE and the FUTURE is NOW.
// This should effectively restrict it to local requests.
if (isset($_SERVER["HTTP_X_REAL_IP"]) && $_SERVER["HTTP_X_REAL_IP"] != "challenge.acictf.com") {
	die("unauthorized: locals only");
}

$expr = "sed -r -e '1h;2,\$H;$!d;g' -e " .
	"'s/data-id=\"(" .
	join("|", $_GET['country']) .
	")\"(\s+)style=\"fill:#333333/" .
	"data-id=\"\\1\"\\2style=\"fill:#00f200/g' world.svg";
$out = shell_exec($expr);
?>
<html>
	<head>
		<title><?php echo htmlspecialchars($_GET["name"]); ?></title>
		<style>
			body {
				background-color: #00004d;
			}
		</style>
	</head>
	<body>
		<?php echo($out); ?>
	</body>
</html>
