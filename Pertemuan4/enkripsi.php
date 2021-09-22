<?php
session_start();


function encrypt($key, $text)
// melakukan operasi enkript
{
	
	$key = ctype_upper($text) ? strtoupper($key) :strtolower($key); 
    // memilih key apakah besar atau kecil
	

	$code = "";
	$keyint = 0;
    // nilai awal perulangan
    $keylength = strlen($key);
    // menampung panjang key
	$length = strlen($text);
    // menampung panjang text
	

	for ($i = 0; $i < $length; $i++)
	{
		// Melakukan perulangan berdasar panjang text
		if (ctype_alpha($text[$i]))
        // Mengecek apakah text berbentuk alfabet
		{
			
			if (ctype_upper($text[$i]))
			{
                // mengecheck apakah text merupakan uppercase
				$text[$i] = chr(((ord($key[$keyint]) - ord("a") + ord($text[$i]) - ord("A")) % 26) + ord("A"));
                // Melakukan operasi enkripsi vigenere
            }
			
		
			else
            // mengecheck apakah text merupakan lowcase
			{
				$text[$i] = chr(((ord($key[$keyint]) - ord("a") + ord($text[$i]) - ord("a")) % 26) + ord("a"));
			// Melakukan operasi enkripsi vignete pada lowcase
            }
			
		
			$keyint++;
			if ($keyint >= $keylength)
			{
                // melakukan perulangan pada keynya
				$keyint = 0;
			}
		}
	}
	
	
	return  $text;
}

// function to decrypt the text given
function decrypt($key, $text)
{
    //melakukan decript

	$key = ctype_upper($text) ? strtoupper($key) :strtolower($key);
	// melakukan pemilihan key apakah harus besar atau kecil
	$code = "";
    
	$keyint = 0;
	$keylength = strlen($key);
	$length = strlen($text);
    // merupakan inisiasi variabel

	for ($i = 0; $i < $length; $i++)
    // melakukan pengulangan
	{
		
		if (ctype_alpha($text[$i]))
        // mengecheck apakah inputan alphabet
		{
			if (ctype_upper($text[$i]))
            // mengecheck apakah text kapital
			{
				$x = (ord($text[$i]) - ord("A")) - (ord($key[$keyint]) - ord("a"));
				
				if ($x < 0)
				{
					$x += 26;
				}
				
				$x = $x + ord("A");
				
				$text[$i] = chr($x);
                // melakukan decrypt pada vigenere 

			}
			
			// lowercase
			else
			{
                //untuk lowercase pada inputan
				$x = (ord($text[$i]) - ord("a")) - (ord($key[$keyint]) - ord("a"));
				
				if ($x < 0)
				{
					$x += 26;
				}
				
				$x = $x + ord("a");
				
				$text[$i] = chr($x);
                // melakukan operasi decrypt
			}
			
			// update the index of key
			$keyint++;
			if ($keyint >= $keylength)
			{
				$keyint = 0;
			}
            // melakukan perulangan pada key
		}
	}
	
	// return the decrypted text
   
	return  $text;
}

?>