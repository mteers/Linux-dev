%define rversion 5.00
%define rel      5
%define pkgname  ctraltdel

Summary		: Keybindings for ctrl-alt-del.
Name		: oscent-%{pkgname}
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

Patch1		: oscent-ctraltdel-hotkey-fix.patch

Patch1000	: oscent-ctraltdel-en_US.ctrlaltdel.po-i18n.patch
Patch1001	: oscent-ctraltdel-fr_CA.ctrlaltdel.po-i18n.patch
Patch1002	: oscent-ctraltdel-ja.ctrlaltdel.po-i18n.patch
Patch1003	: oscent-ctraltdel-ko.ctrlaltdel.po-i18n.patch
Patch1004	: oscent-ctraltdel-zh_CN.ctrlaltdel.po-i18n.patch
Patch1005	: oscent-ctraltdel-zh_TW.ctrlaltdel.po-i18n.patch

%description
Keybindings for ctrl-alt-del.

%prep
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}
%setup -n %{pkgname}
#set the enviroment
find . -type f | xargs perl -pi -e "s|__DISTRIBUTION_SHORT|oscent|"
find . -type f | xargs perl -pi -e "s|__INSTALL_PATH_PREFIX|%{__install_path_prefix}|"
find . -type f | xargs perl -pi -e "s|__PIXMAP_PATH|%{__pixmap_path}|"
# Copy the pixmap
cp -f pixmaps/ctraltdel.png.oscent pixmaps/ctraltdel.png

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
* Tue Dec 09 2008 beefcake@beef.qt 5.00-4
- Make suspend work again

* Tue Oct 11 2005 beefcake@beef.qt 4.00-5
- Added nls translations.

* Wed Dec 08 2004 beefcake@beef.qt 1.0-9
- Added pam links back in.

* Thu Oct 28 2004 beefcake@beef.qt 1.0-8
- Changed colour to #162a46

* Fri Oct 22 2004 beefcake@beef.qt 1.0-7
- Added support for custom gnome-panel.

* Mon Aug 02 2004 beefcake@beef.qt
- First release

