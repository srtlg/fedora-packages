# Fedora Packages

Some packages for Fedora which I miss.

[![Copr build status](https://copr.fedorainfracloud.org/coprs/mscholz1/solvespace/package/solvespace/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/mscholz1/solvespace/package/solvespace/)
solvespace

[![Copr build status](https://copr.fedorainfracloud.org/coprs/mscholz1/GMAT/package/GMAT/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/mscholz1/GMAT/package/GMAT/)
GMAT


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
cd SPECS
+rpmdev-newspec GMAT
```

## Check sources

```cmdline
rpmdev-spectool -gR SPECS/foobar.spec
```

## install dependencies

```cmdline
sudo dnf builddep SPECS/foobar.spec
```

## Iterative generating

extraction is slow

```commandline
rpmbuild -bb --noprep SPECS/foobar.spec
```

build succeeded, develop install

```commandline
rpmbuild --short-circuit -bi SPECS/foobar.spec
```


## New upstream

```commandline
rpmdev-bumpspec -c 'Upgrade to X' SPECS/foobar.spec
```


# References

https://fedoraproject.org/wiki/PackagingDrafts:GPGSignatures

https://developer.fedoraproject.org/deployment/rpm/about.html

https://fedoraproject.org/wiki/Using_Mock_to_test_package_builds

https://docs.fedoraproject.org/en-US/packaging-guidelines/AppData/

https://rpm-packaging-guide.github.io/#working-with-spec-files

http://ftp.rpm.org/max-rpm/s1-rpm-inside-macros.html

https://rpm-software-management.github.io/rpm/manual/autosetup.html
