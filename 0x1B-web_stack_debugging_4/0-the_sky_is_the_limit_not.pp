# increases the no. of traffic an nginx server can handle.

exec { 'fix-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin:/bin/'
}

-> exec { 'restart':
  command => 'nginx restart',
  path    => '/etc/init.id/'
}
