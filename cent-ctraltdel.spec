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
* Tue Dec 09 2008 Grant Williamson <grant_williamson@nl.ibm.com> 5.00-4
- Make suspend work again

* Tue Aug 28 2007 Timothy Bissell <tbissell@us.ibm.com> 5.00-3
- Updated gettext .pot to specify UTF-8 instead of CHARSET

* Tue Apr 17 2007 Timothy Bissell <tbissell@us.ibm.com> 5.00-2
- Added NLS data for fr_CA, ja, ko, zh_CN, zh_TW

* Thu Jan 04 2007 Grant Williamson <grant_williamson@nl.ibm.com> 5.00-1
- Updated for 2.0

* Wed Apr 19 2006 Grant Williamson <grant_williamson@nl.ibm.com> 4.00-8
- Updated schema, so battery suspend does something.

* Tue Jan 10 2006 Grant Williamson <grant_williamson@nl.ibm.com> 4.00-7
- Fixed double click on ctrl-alt-del keys.

* Fri Oct 14 2005 Grant Williamson <grant_williamson@nl.ibm.com> 4.00-6
- Added Openclient back to gui.

* Tue Oct 11 2005 Grant Williamson <grant_williamson@nl.ibm.com> 4.00-5
- Added nls translations.

* Tue Oct 04 2005 Grant Williamson <grant_williamson@nl.ibm.com> 4.00-4
- Added nls translations.

* Thu Mar 31 2005 Grant Williamson <grant_williamson@nl.ibm.com> 4.00-3
- Changed name suspend - hibernate.

* Thu Mar 03 2005 Grant Williamson <grant_williamson@nl.ibm.com> 4.00-2
- Removed suspend addons.

* Wed Feb 02 2005 Grant Williamson <grant_williamson@nl.ibm.com> 4.00-1
- Rebuilt for c4eb-4.00

* Wed Dec 08 2004 Grant Williamson <grant_williamson@nl.ibm.com> 1.0-9
- Added pam links back in.

* Thu Oct 28 2004 Grant Williamson <grant_williamson@nl.ibm.com> 1.0-8
- Changed colour to #162a46

* Fri Oct 22 2004 Grant Williamson <grant_williamson@nl.ibm.com> 1.0-7
- Added support for custom gnome-panel.

* Thu Oct 21 2004 Grant Williamson <grant_williamson@nl.ibm.com> 1.0-6
- Broke out to single installing package.

* Sat Oct 09 2004 Grant Williamson <grant_williamson@nl.ibm.com> 1.0-5
- Added triggers to call our schemas.

* Tue Oct 05 2004 Grant Williamson <grant_williamson@nl.ibm.com> 1.0-4
- No more replacing schemas, we simply add our own.

* Tue Oct 05 2004 Grant Williamson <grant_williamson@nl.ibm.com> 1.0-3
- Rebuild to adhere to new packaging standards 

* Fri Oct 01 2004 Grant Williamson <grant_williamson@nl.ibm.com> 1.0-2
- Corrected lock screen, close application

* Thu Sep 29 2004 Grant Williamson <grant_williamson@nl.ibm.com> 1.0-1
- Added NLS support, better source.

* Fri Aug 27 2004 Grant Williamson <grant_williamson@nl.ibm.com>
- Added pam update.

* Wed Aug 25 2004 Grant Williamson <grant_williamson@nl.ibm.com>
- Better gui.
- Wrong suspend link. 

* Tue Aug 24 2004 Grant Williamson <grant_williamson@nl.ibm.com>
- Added suspend to gui (requested by colm)

* Sun Aug 22 2004 Grant Williamson <grant_williamson@nl.ibm.com>
- Added proper timer to gui.

* Sat Aug 21 2004 Grant Williamson <grant_williamson@nl.ibm.com>
- Added single process start
- Added timer to stop app after 10 seconds

* Thu Aug 19 2004 Grant Williamson <grant_williamson@nl.ibm.com>
- removed nasty redbox

* Wed Aug 18 2004 Grant Williamson <grant_williamson@nl.ibm.com>
- Added keybinding to options.

* Tue Aug 03 2004 Grant Williamson <grant_williamson@nl.ibm.com>
- Bug in wine/metacity changed keybinding to SHIFT-DEL
- Added information window for CTRL-ALT-DEL

* Mon Aug 02 2004 Grant Williamson <grant_williamson@nl.ibm.com>
- First release

