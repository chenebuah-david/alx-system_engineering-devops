# The amount of traffic an Nginx server can handle will increase
# The ULIMIT of the default file will increase

exec { 'fix--for-nginx': 
  command => 'sed -i "s/15/4096/" /etc/default/nginx', 
  path    => '/usr/local/bin/:/bin/' 
} -> 
  
# Nginx restarts
exec { 'nginx-restart': 
  command => 'nginx restart', 
  path    => '/etc/init.d/' 
}
