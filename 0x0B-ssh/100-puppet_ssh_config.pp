#This script connect to a server without typing a password

include stdlib

file_line { 'Turn off password auth':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => '    IdentityFile ~/.ssh/school',
replace  => true,
}

file_line { 'Declare identity file':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => '    PasswordAuthentication no',
replace  => true,
}
