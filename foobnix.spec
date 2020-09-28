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
%{__python} setup.py build

%install
%{__python} setup.py install --root %{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/foobnix/images/foobnix*
%{_datadir}/foobnix/images/theme/*
%{_datadir}/foobnix/images/vk-small.png
%{_datadir}/foobnix/images/vk.png
%{_datadir}/foobnix/radio/*
%{_datadir}/pixmaps/foobnix.png
%{_mandir}/man1/foobnix.1.*
%{python_sitelib}/foobnix*
