# update ubuntu packages

exec { 'update system':
    command => '/usr/bin/apt-get -y update',
}

package { 'nginx':
    ensure => 'installed',
    require => Exec['update system']
}

file {'var/www/html/index.nginx-debian.html':
    content => 'Hello World!',
}

exec {'redirect_me':
    command => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
    provider => 'shell'
}

service { 'nginx':
    ensure => running,
    require => package['nginx']
}
