#script finds and replaces "phpp" extensions with "php" in "wp-settings.php".
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/bin'],
}
