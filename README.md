
# Installation 

```commandline
dnf install mock
usermod -a -G mock myusername
echo %_topdir $PWD > ~/.rpmmacros
```


# Packages

## Modify existing

e.g. gocryptfs exists in FC35 but not in FC36

```commandline
dnf download --releasever 35 --source gocryptfs
rpm2cpio golang-github-rfjakob-gocryptfs-1.8.0-6.fc35.src.rpm | cpio -idv
mv 0001-Update-go-fuse-import-path.patch gocryptfs_v1.8.0_src.tar.gz SOURCES
mv golang-github-rfjakob-gocryptfs.spec SPECS
rpmbuild -bs SPECS/golang-github-rfjakob-gocryptfs.spec
mock SRPMS/golang-github-rfjakob-gocryptfs-1.8.0-6.fc36.src.rpm
```


## Generate new


# References

https://fedoraproject.org/wiki/Using_Mock_to_test_package_builds
