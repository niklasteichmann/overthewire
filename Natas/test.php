<?php 
	class Executor {
                private $filename="";
                private $signature='adeafbadbabec0dedabada55ba55d00d';
                private $init=False;

                function __construct(){
                    if(filesize($_FILES['uploadedfile']['tmp_name']) > 4096) {
                        echo "File is too big<br>";
                    }
                }
		function __destruct(){
                    if(md5_file($this->filename) == $this->signature){
                        echo "Congratulations! Running firmware update: $this->filename <br>";
                        passthru("php " . $this->filename);
                    }
                    else{
                        echo "Failur! MD5sum mismatch!<br>";
                    }
                }
	}
	echo filesize("phar://" . getcwd() . "/33.phar/text.txt");
?>
