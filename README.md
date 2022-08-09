# Fedora Packages

Some packages for Fedora which I miss.


# Installation 

```commandline
dnf install mock rpmdevtools
usermod -a -G mock myusername
echo %_topdir $PWD > ~/.rpmmacros
```

## Using dnf history rollback

```commandline
dnf history last
N:=ID
dnf history rollback N
```


# Packages

## Modify existing from older Fedora

e.g. gocryptfs exists in FC35 but not in FC36

```commandline
dnf download --releasever 35 --source gocryptfs
rpm2cpio golang-github-rfjakob-gocryptfs-1.8.0-6.fc35.src.rpm | cpio -idv
rm 0001-Update-go-fuse-import-path.patch gocryptfs_v1.8.0_src.tar.gz
mv golang-github-rfjakob-gocryptfs.spec SPECS
rpmdev-spectool -gR SPECS/golang-github-rfjakob-gocryptfs.spec
# -either-
rpmbuild -bs SPECS/golang-github-rfjakob-gocryptfs.spec
mock SRPMS/golang-github-rfjakob-gocryptfs-1.8.0-6.fc36.src.rpm
# -or-
rpmbuild -bb SPECS/golang-github-rfjakob-gocryptfs.spec
```


## Generate new

```commandline

```


# References

https://developer.fedoraproject.org/deployment/rpm/about.html

https://fedoraproject.org/wiki/Using_Mock_to_test_package_builds
