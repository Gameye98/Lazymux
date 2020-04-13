apt update && apt upgrade
apt install curl git
apt install autoconf bison clang coreutils curl findutils git apr apr-util libffi-dev libgmp-dev libpcap-dev \ postgresql-dev readline-dev libsqlite-devopenssl-dev libtool libxml2-dev libxslt-dev ncurses-dev pkg-config \ postgresql-contrib wget make ruby-dev libgrpc-dev termux-tools ncurses ncurses-utils libsodium-dev
curl -L https://github.com/rapid7/metasploit-framework/archive/4.16.2.tar.gz | tar xz cd metasploit-framework-4.16.2 sed 's|git ls-files|find -type f|' -i metasploit-framework.gemspec
sed 's/rb-readline (0.5.5)/rb-readline /g' -i Gemfile.lock sed 's/rb-readline/rb-readline (= 0.5.5)/g' -i Gemfile.lock
gem install bundler
gem unpack rbnacl-libsodium -v'1.0.13' cd rbnacl-libsodium-1.0.13 termux-fix-shebang ./vendor/libsodium/configure ./vendor/libsodium/build-aux/* sed 's|">= 3.0.1"|"~> 3.0", ">= 3.0.1"|g' -i rbnacl-libsodium.gemspec sed's|">= 10"|"~> 10"|g' -i rbnacl-libsodium.gemspec
curl -LO https://Auxilus.github.io/configure.patch patch ./vendor/libsodium/configure < configure.patch
gem build rbnacl-libsodium.gemspec gem install rbnacl-libsodium-1.0.13.gemcd .. rm -rf rbnacl-libsodium-1.0.13
gem install nokogiri -- --use-system-libraries
sed 's|grpc (.*|grpc (1.4.1)|g' -i $HOME/metasploit-framework/Gemfile.lock gem unpack grpc -v 1.4.1 cd grpc-1.4.1 curl -LO https://raw.githubusercontent.com/grpc/grpc/v1.4.1/grpc.gemspec curl -L https://wiki.termux.com/images/b/bf/Grpc_extconf.patch -o extconf.patch patch -p1 < extconf.patch gem build grpc.gemspec gem install grpc-1.4.1.gem cd .. rm -r grpc-1.4.1
bundle install -j5
$PREFIX/bin/find -type f -executable -exec termux-fix-shebang \{ \ } \;ruby msfconsole