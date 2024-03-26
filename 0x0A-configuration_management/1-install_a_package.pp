#!/usr/bin/pup
# Install flask from pip3 version (2.1.0)
package {'flask':
ensure   => '2.1.0',
provider => 'pip3'
}

# Install Werkzeug version
package {'werkzeug':
ensure   => '2.1.1',
provider => 'pip3'
}