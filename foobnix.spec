%define	PYVER	`python -c "import sys; print sys.version[:3]"`
%define	rel	5

Name:		foobnix
Version: 	0.2.5
Release: 	%mkrel %rel
URL:		http://foobnix.com
License:	GNU GPL v3 or later
Source: 	%{name}_%{version}-%{rel}m.tar.gz
Summary:	Simple and Powerful music player for Linux
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}_%{version}-build

BuildRequires: python-chardet, pygtk2.0, pygtk2.0-libglade, mutagen, python-simplejson, python-setuptools 
BuildRequires: gstreamer0.10-plugins-good, gstreamer0.10-plugins-ugly, gstreamer0.10-ffmpeg, gstreamer0.10-plugins-bad
BuildRequires: gstreamer0.10-python, gettext, make, fuseiso
BuildRequires: python-keybinder

Requires: python-chardet, python-setuptools, python-simplejson, mutagen
Requires: gstreamer0.10-plugins-good, gstreamer0.10-python
Requires: gstreamer0.10-ffmpeg, gstreamer0.10-plugins-ugly

%description 
Simple and Powerful music player for Linux

All best features in one player. Foobnix small, fast, customizable, powerful
music player with user-friendly interface.

%prep
%setup -q -n %{name}_%{version}-%{rel}


%build

%install
rm -rf %{buildroot}
PREFIX=%{buildroot}/usr make install

%files
%defattr (-,root,root,0755)
%doc README COPYING CHANGELOG
%{_bindir}/%{name}
%{_libdir}/python%{pyver}/site-packages/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}*
%{_datadir}/pixmaps/theme/cat.jpg
%{_datadir}/pixmaps/theme/flower.jpg
%{_mandir}/man1/%{name}*
%{_datadir}/locale/es/LC_MESSAGES/%{name}.*
%{_datadir}/locale/it/LC_MESSAGES/%{name}.*
%{_datadir}/locale/uk/LC_MESSAGES/%{name}.*
%{_datadir}/locale/ru/LC_MESSAGES/%{name}.*
%{_datadir}/locale/pl/LC_MESSAGES/%{name}.*
%{_datadir}/locale/zh_CN/LC_MESSAGES/%{name}.*

%clean
rm -rf %{buildroot}

