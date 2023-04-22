# ensure connection to server
include stdlib

file_line { 'disable password auth':
    ensure  => present,
    path    => '/etc/ssh/ssh_config/',
    line    => '     PasswordAuthentication no',
    replace => true,
}

file_line { 'declare identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '     IdentityFile ~/.ssh/school',
  replace => true,
}
