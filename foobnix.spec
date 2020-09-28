%define debug_package %{nil}

%define	PYVER	`python -c "import sys; print sys.version[:3]"`

Name:		foobnix
Version: 	3.2.1
Release: 	1
URL:		http://foobnix.com
License	:	GPLv3 
Source:		https://github.com/foobnix/foobnix/archive/%{version}/%{name}-%{version}.tar.gz
Summary:		Simple and Powerful music player for Linux
Group:		Sound

%description 
Simple and Powerful music player for Linux

All best features in one player. Foobnix small, fast, customizable, powerful
music player with user-friendly interface.


BuildRequires: pkgconfig(python)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: python3dist(simplejson)
BuildRequires: python3dist(mutagen)
BuildRequires: python3dist(pylast)

Requires: python
Requires: python3dist(simplejson)
Requires: python3dist(mutagen)
Requires: python3dist(pylast)


%prep
%setup -q -n %{name}-%{version}

%build
%make_build

%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%doc README COPYING CHANGELOG
%{_bindir}/%{name}
%{python_sitearch}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
#{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/pixmaps/%{name}*
%{_datadir}/pixmaps/theme/cat.jpg
%{_datadir}/pixmaps/theme/flower.jpg
%{_datadir}/pixmaps/vk.png
%{_datadir}/pixmaps/theme/winter.jpg
%{_mandir}/man1/%{name}*




