<?php 
error_reporting(0);
$pswd = $_SESSION['pswd'];
$code = $_SESSION['code'];
if ($_SERVER['REQUEST_METHOD'] == "POST")
{
	// declare encrypt and decrypt funtions
	require_once('enkripsi.php');
	
	// set the variables
	$key = $_POST['key'];
	$code = $_POST['masukkan'];
	
	// check if password is provided
	if (empty($_POST['key']))
	{
		$error = "Please enter a password!";
		$valid = false;
	}
	
	// check if text is provided
	else if (empty($_POST['masukkan']))
	{
		$error = "Please enter some text or masukkan to encrypt or decrypt!";
		$valid = false;
	}
	
	// check if password is alphanumeric
	else if (isset($_POST['key']))
	{
		if (!ctype_alpha($_POST['key']))
		{
			$error = "Password should contain only alphabetical characters!";
			$valid = false;
		}
	}
	
	// inputs valid
	if ($valid)
	{
		// if encrypt button was clicked
		if (isset($_POST['encrypt']))
		{
			$masukkan = encrypt($key, $code);
			$error = "Text encrypted successfully!";
			$color = "#526F35";
		}
			
		// if decrypt button was clicked
		if (isset($_POST['decrypt']))
		{
			$masukkan = decrypt($key, $code);
			$error = "masukkan decrypted successfully!";
			$color = "#526F35";
		}
	}
}

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enkripsi Web</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    
    
    <form action="enkripsi.php" method="post">
        <!-- berfungsi untuk mengirim nilai ke halaman lain -->
        <fieldset>

       <legend><h1>Web Enkripsi</h1></legend>
       <ul>
           <li> <input type="text" name="masukkan" id="masukkan" placeholder="Masukkan Kata yang ingin dienkripsi"></li>  <!--
               Memasukkan nilai yang ingin di enkripsi di sini
            -->
           <li> <input type="text" name="key" id="key" placeholder="masukkan Key"></li> <!-- memasukkan kunci pergeseran chaesar chiper -->
           <li ><input type="submit" name="enkripsi" value="Enkripsi" /></li>  
           <!-- Jika ingin melakkan enkripsi mengeklik tombol ini -->
           <li><input type="submit" name="enkripsi" value="Deskripsi"/></li>
           <!-- Jika ingin melakukan deskripsi mengeklik tombol deskripsi -->
           <li><a style="background-color: aqua; height: 20px; text-decoration: none; color: grey;" href="clear.php">Clear</a></li>
           <!-- untuk melakukan logout -->
           <li class="enkripsi">
               <!-- Berfungsi menampilkan Enkripsi dan Deskripsi -->
                <h2>Enkripsi    :<?php echo  $_SESSION['code'];?></h2>
                <h2>Deskripsi   :<?php echo  $_SESSION['code'];?></h2>
           </li>
       </ul>
       
        
        
        </fieldset>

    </form>
    
</body>
</html>