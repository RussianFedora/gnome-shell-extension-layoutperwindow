Summary:        Layout per Window extension for GNOME Shell
Name:           gnome-shell-extension-layoutperwindow
Version:        0.0.0

Release:        0.2.7c3099e.git%{?dist}
Group:          User Interface/Desktops
License:        GPLv2+ 
URL:            https://github.com/rat4/layoutperwindow/tree/master/layoutperwindow%40rat4.github.com
Source0:        gnome-shell-extension-layoutperwindow-0.0.0-7c3099e.tar.xz

Requires:       gnome-shell >= 3.6

BuildArch:      noarch


%description
Remember layout for single window in GNOME Shell

%package -n cinnamon-extension-layoutperwindow
Summary:        Layout per Window extension for Cinnamon
Group:          User Interface/Desktops
License:        GPLv2+
Requires:       cinnamon >= 1.6.6

%description -n cinnamon-extension-layoutperwindow
Remember layout for single window in Cinnamon


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
install -dD $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/
install -dD $RPM_BUILD_ROOT%{_datadir}/cinnamon/extensions/
cp -r layoutperwindow@rat4.github.com $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/
cp -r layoutperwindow@rat4.github.com $RPM_BUILD_ROOT%{_datadir}/cinnamon/extensions/

cat > $RPM_BUILD_ROOT%{_datadir}/cinnamon/extensions/layoutperwindow@rat4.github.com/metadata.json <<FOE
{"cinnamon-version": ["1.6"], "uuid": "layoutperwindow@rat4.github.com", "name": "Layout per window", "description": "blah blah blah"}
FOE

%files
%defattr(-,root,root,-)
%{_datadir}/gnome-shell/extensions/*

%files -n cinnamon-extension-layoutperwindow
%{_datadir}/cinnamon/extensions/*


%changelog
* Mon Jan 28 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 0.0.0-0.2.7c3099e.git.R
- adapted for cinnamon

* Tue Jan 15 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 0.0.0-0.1.7c3099e.git.R
- initial build
