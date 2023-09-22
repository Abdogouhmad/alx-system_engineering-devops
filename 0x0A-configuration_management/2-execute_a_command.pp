# execute cmd with puppet
exec { 'pkill':
	commadn => 'pkill -9 -f killmenow',
	path => ['/usr/bin', '/usr/sbin', '/bin']
}
