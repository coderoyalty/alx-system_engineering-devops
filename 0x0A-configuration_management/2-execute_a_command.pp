# kill a process named killmenow
exec { 'kill-process-killmenow':
    command => 'pkill killmenow',
    onlyif  => 'pgrep killmenow',
    path    => '/usr/bin/',
}
