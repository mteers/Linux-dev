%define rversion 5.00
%define rel      5
%define pkgname  ctraltdel

Summary		: Keybindings for ctrl-alt-del.
Name		: c4eb-%{pkgname}
Version		: %{rversion}
Release		: %{rel}%{?dist}
License		: IBM Internal Use Only
Group		: System Environment/Base
Url		: http://pokgsa.ibm.com/projects/o/openclient

Source0		: ctraltdel-oc2.tar.gz

%if "%rhel" >= "5"
Requires	: bash, coreutils
Requires	: python
%endif

%if "%sled" >= "10"
Requires	: bash, coreutils
Requires	: python
%endif

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch	: noarch
BuildRequires	: perl

Patch1		: c4eb-ctraltdel-hotkey-fix.patch

Patch1000	: c4eb-ctraltdel-en_US.ctrlaltdel.po-i18n.patch
Patch1001	: c4eb-ctraltdel-fr_CA.ctrlaltdel.po-i18n.patch
Patch1002	: c4eb-ctraltdel-ja.ctrlaltdel.po-i18n.patch
Patch1003	: c4eb-ctraltdel-ko.ctrlaltdel.po-i18n.patch
Patch1004	: c4eb-ctraltdel-zh_CN.ctrlaltdel.po-i18n.patch
Patch1005	: c4eb-ctraltdel-zh_TW.ctrlaltdel.po-i18n.patch

%description
Keybindings for ctrl-alt-del.

%prep
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}
%setup -n %{pkgname}
#set the enviroment
find . -type f | xargs perl -pi -e "s|__DISTRIBUTION_SHORT|c4eb|"
find . -type f | xargs perl -pi -e "s|__INSTALL_PATH_PREFIX|%{__install_path_prefix}|"
find . -type f | xargs perl -pi -e "s|__PIXMAP_PATH|%{__pixmap_path}|"
# Copy the pixmap
cp -f pixmaps/ctraltdel.png.c4eb pixmaps/ctraltdel.png

# Bad original data in this .po, remove before we patch
rm po/fr_CA.po
sed -i -e 's/CHARSET/UTF-8/' po/ctrlaltdel.pot

%patch1 -p1

%patch1000 -p1
%patch1001 -p1
%patch1002 -p1
%patch1003 -p1
%patch1004 -p1
%patch1005 -p1

# Tag in source does not match tag in .pot, update everything to match
grep -r 'Log Out' * | awk -F: '{print $1}' | xargs -l1 sed -i -e 's/Log Out/Log _Out/g'

%build
%{__make} all

%install
%{__mkdir_p} %{buildroot}
%{__make} INSTROOT=%{buildroot} install
pushd po
%{__make} INSTROOT=%{buildroot} install
popd
%find_lang ctraltdel

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files -f ctraltdel.lang
%defattr(0755, root, root, 0755)
%{__install_path_prefix}/ctrl-alt-del/ctraltdel.py
%{__install_path_prefix}/ctrl-alt-del/ctraltdel.pyc
%{__install_path_prefix}/ctrl-alt-del/ctraltdel.pyo
%defattr(0644, root, root, 0755)
%{__pixmap_path}/*

%changelog
* Tue Dec 09 2008 Beefcake@bt.qt 5.00-4
- Make suspend work again

