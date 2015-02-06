%define debug_package %{nil}

%define	PYVER	`python -c "import sys; print sys.version[:3]"`
%define	rel	1

Name:		foobnix
Version: 	2.6.03
Release: 	2
URL:		http://foobnix.com
License	:	GPLv3 
Source:		https://launchpad.net/~foobnix-player/+archive/foobnix/+files/%{name}_%{version}m.tar.gz
Summary:		Simple and Powerful music player for Linux
Group:		Sound


BuildRequires: python-chardet, 
BuildRequires: pygtk2.0, 
BuildRequires: pygtk2.0-libglade, 
BuildRequires: mutagen, 
BuildRequires: python-simplejson, 
BuildRequires: python-setuptools 
BuildRequires: gstreamer0.10-plugins-good, 
BuildRequires: gstreamer0.10-plugins-ugly, 
BuildRequires: gstreamer0.10-ffmpeg, 
BuildRequires: gstreamer0.10-plugins-bad
BuildRequires: gstreamer0.10-python, 
BuildRequires: gettext, 
BuildRequires: make, 
BuildRequires: fuseiso
BuildRequires: keybinder


Requires: python-webkitgtk
Requires: python-chardet, 
Requires: python-setuptools, 
Requires: python-simplejson, 
Requires: mutagen
Requires: gstreamer0.10-plugins-good, 
Requires: gstreamer0.10-python
Requires: gstreamer0.10-ffmpeg, 
Requires: gstreamer0.10-plugins-ugly

%description 
Simple and Powerful music player for Linux

All best features in one player. Foobnix small, fast, customizable, powerful
music player with user-friendly interface.

%prep
%setup -q -n %{name}_%{version}

%build

%install
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
#permissions
chmod a+x %{buildroot}%{_libdir}/python2.7/site-packages/foobnix/thirdparty/google/{browser,__init__,search}.py
chmod a+x %{buildroot}%{_libdir}/python2.7/site-packages/foobnix/thirdparty/mutagen/__init__.py
chmod a+x %{buildroot}%{_libdir}/python2.7/site-packages/foobnix/preferences/preferences_window.py

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




