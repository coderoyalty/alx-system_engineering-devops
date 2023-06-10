# puppet file to fix a 500 error from an apache server
exec { 'phpp-fixed':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/bin',
}
