%define	PYVER	`python -c "import sys; print sys.version[:3]"`
%define	rel	9

Name:		foobnix
Version: 	0.2.5
Release: 	%mkrel %rel
URL:		http://foobnix.com
License:	GNU GPL v3 or later
Source:		https://launchpad.net/~foobnix-player/+archive/foobnix/+files/%{name}_%{version}-%{rel}m.tar.gz
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
%setup -q -n %{name}_%{version}-%{rel}


%build

%install
rm -rf %{buildroot}
PREFIX=%{buildroot}/usr make install


# Mandriva Desktop Main file
mkdir -p %{buildroot}{%{_icons48dir},%{_desktopdir}}

cat > %{buildroot}/%{_desktopdir}/%{name}.desktop << EOF
[Desktop Entry]
Name=Foobnix
GenericName=Music Player
GenericName[ru]=Плеер музыки
X-GNOME-FullName=Foobnix Music Player
Comment=Simple and Powerful player for Linux
Comment[ru]=Простой и мощный плеер для Linux
Comment[uk]=Простий і потужний плеєр для Linux
Exec=%{name} %U
Icon=%{name}.png
StartupNotify=true
Terminal=false
Type=Application
X-GNOME-DocPath=foobnix/foobnix.xml
Categories=GNOME;GTK;AudioVideo;Player;X-MandrivaLinux-CrossDesktop;X-MandrivaLinux-Multimedia-Video;
MimeType=application/x-ogg;application/ogg;audio/x-vorbis+ogg;audio/x-scpls;audio/x-mp3;audio/x-mpeg;audio/mpeg;audio/x-mpegurl;audio/x-flac;x-content/audio;
EOF
# end Mandriva Desktop Main

# Mandriva dirty-fix the Python bug for x86_64 patch lib64
%if "%{?_lib}" == "lib64" 
mkdir -p %{buildroot}%{python_sitearch}/
cp -r %{buildroot}%{python_sitelib}/ %{buildroot}%{py_platlibdir}/
rm -r %{buildroot}%{python_sitelib}/
%endif
# end Mandriva dirty-fix

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
%{_mandir}/man1/%{name}*
%{_datadir}/locale/es/LC_MESSAGES/%{name}.*
%{_datadir}/locale/it/LC_MESSAGES/%{name}.*
%{_datadir}/locale/uk/LC_MESSAGES/%{name}.*
%{_datadir}/locale/ru/LC_MESSAGES/%{name}.*
%{_datadir}/locale/pl/LC_MESSAGES/%{name}.*
%{_datadir}/locale/zh_CN/LC_MESSAGES/%{name}.*

%clean
rm -rf %{buildroot}

