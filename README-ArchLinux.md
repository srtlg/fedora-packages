# Build on Arch Linux

## Via systemd-nspawn

from [https://wiki.archlinux.org/title/systemd-nspawn](here)

with [](httpcache)

```commandline
packman -S dnf

cat>>/etc/dnf/dnf.conf<<EOF
[fedora]                                                                                            
name=Fedora \$releasever - \$basearch
#metalink=https://mirrors.fedoraproject.org/metalink?repo=fedora-\$releasever&arch=\$basearch
baseurl=http://ftp.uni-bayreuth.de/linux/fedora/linux/releases/\$releasever/Everything/\$basearch/os
gpgkey=https://getfedora.org/static/fedora.gpg
EOF

release=37
mkdir /var/lib/machines/fedora-$release
export http_proxy=http://localhost:8000
dnf --releasever=$release --best --setopt=install_weak_deps=False --repo=fedora --installroot=/var/lib/machines/fedora-$release \
install dhcp-client dnf fedora-release glibc glibc-langpack-en iputils less ncurses passwd systemd systemd-networkd systemd-resolved util-linux -y

rm -f /etc/systemd/nspawn/fedora-$release.nspawn

systemd-nspawn -D /var/lib/machines/fedora-$release passwd
systemd-nspawn -D /var/lib/machines/fedora-$release sh -c "useradd -m $USER; passwd $USER"

echo "%_topdir /home/$USER/Github/fedora-packages" > /home/$USER/.rpmmacros

# this is a link, prevents nspawn to function
rm /var/lib/machines/fedora-$release/etc/resolv.conf

cat>/etc/systemd/nspawn/fedora-$release.nspawn<<EOF
[Network]
VirtualEthernet=no
[Files]
Bind=/home/$USER/Github/fedora-packages:/home/$USER/Github/fedora-packages:idmap
EOF

machinectl start fedora-$release
machinectl login fedora-$release

dnf --releasever=$release --best --setopt=install_weak_deps=False --repo=fedora --installroot=/var/lib/machines/fedora-$release \
install rpmdevtools -y


# requirements for individual packages

dnf --releasever=$release --best --setopt=install_weak_deps=False --repo=fedora --installroot=/var/lib/machines/fedora-$release \
install go-rpm-macros -y
```
