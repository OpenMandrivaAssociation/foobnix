%define	PYVER	`python -c "import sys; print sys.version[:3]"`
%define	rel	1

Name:		foobnix
Version: 	2.5.16
Release: 	%mkrel 1
URL:		http://foobnix.com
License:	GNU GPL v3 or later
Source:		https://launchpad.net/~foobnix-player/+archive/foobnix/+files/%{name}_%{version}m.tar.gz
#Source: 	%{name}_%{version}-%{rel}m.tar.gz
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
%setup -q -n %{name}_%{version}

%build

%install
rm -rf %{buildroot}
PREFIX=%{buildroot}/usr make install

%if "%{?_lib}" == "lib64" 
mkdir -p %{buildroot}%{python_sitearch}/
cp -r %{buildroot}%{python_sitelib}/ %{buildroot}%{py_platlibdir}/
rm -r %{buildroot}%{python_sitelib}/
%endif

# icons fix
mkdir -p %{buildroot}%{_icons64dir}/
cp %{buildroot}%{_datadir}/pixmaps/%{name}.png \
%{buildroot}%{_icons64dir}/

%files
%defattr (-,root,root,0755)
%doc README COPYING CHANGELOG
%{_bindir}/%{name}
%{python_sitearch}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_datadir}/icons/hicolor/64x64/apps/%{name}.*
%{_datadir}/pixmaps/%{name}*
%{_datadir}/pixmaps/theme/cat.jpg
%{_datadir}/pixmaps/theme/flower.jpg
%{_datadir}/pixmaps/vk.png
%{_mandir}/man1/%{name}*
%{_datadir}/locale/es/LC_MESSAGES/%{name}.*
%{_datadir}/locale/it/LC_MESSAGES/%{name}.*
%{_datadir}/locale/uk/LC_MESSAGES/%{name}.*
%{_datadir}/locale/ru/LC_MESSAGES/%{name}.*
%{_datadir}/locale/pl/LC_MESSAGES/%{name}.*
%{_datadir}/locale/zh_CN/LC_MESSAGES/%{name}.*
%{_datadir}/locale/en_GB/LC_MESSAGES/%{name}.*
%{_datadir}/locale/pt/LC_MESSAGES/%{name}.*
%{_datadir}/locale/de/LC_MESSAGES/%{name}.*
#%{_datadir}/locale/by/LC_MESSAGES/%{name}.*
%{_datadir}/locale/fr/LC_MESSAGES/%{name}.*
%{_datadir}/locale/tr/LC_MESSAGES/%{name}.*

%clean
rm -rf %{buildroot}

