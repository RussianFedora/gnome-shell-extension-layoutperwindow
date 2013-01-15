Summary:        Layout per Window extension for GNOME Shell
Name:           gnome-shell-extension-layoutperwindow
Version:        0.0.0

Release:        0.1.7c3099e.git%{?dist}
Group:          User Interface/Desktops
License:        GPLv2+ 
URL:            https://github.com/rat4/layoutperwindow/tree/master/layoutperwindow%40rat4.github.com
Source0:        gnome-shell-extension-layoutperwindow-0.0.0-7c3099e.tar.xz

Requires:       gnome-shell >= 3.6

BuildArch:      noarch


%description
Remember layout for single window in GNOME Shell


%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
install -dD $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/
cp -r layoutperwindow@rat4.github.com $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/

%files
%defattr(-,root,root,-)
%{_datadir}/gnome-shell/extensions/*


%changelog
* Tue Jan 15 2013 Arkady L. Shane <ashejn@russianfedora.ru> - 0.0.0-0.1.7c3099e.git.R
- initial build
