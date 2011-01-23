%define	PYVER	`python -c "import sys; print sys.version[:3]"`
%define	rel	0

Name:		foobnix
Version: 	0.2.3
Release: 	%mkrel 1
URL:		http://foobnix.com
License:	GNU GPL v3 or later
Source: 	%{name}_%{version}-0l.tar.gz
Summary:	Simple and Powerful music player for Linux
Summary(ru): 	Простой и мощный плеер музыки для ОС Linux
Group:		Multimedia/Sound/Players
Packager:	Sergey Zhemoitel <djam5@ya.ru>
BuildRoot:	%{_tmppath}/%{name}_%{version}-build

BuildRequires: python-chardet, pygtk2.0, pygtk2.0-libglade, mutagen, python-simplejson, python-setuptools 
BuildRequires: gstreamer0.10-plugins-good, gstreamer0.10-plugins-ugly, gstreamer0.10-ffmpeg, gstreamer0.10-plugins-bad
BuildRequires: gstreamer0.10-python, gettext, make, fuseiso
BuildRequires: python-keybinder

## python-glade2 ??=?? pygtk2.0-libglade
## python-gtk2 ??=?? pygtk2.0 
## python-mutagen ??=?? mutagen


%description 
Simple and Powerful music player for Linux

All best features in one player. Foobnix small, fast, customizable, powerful
music player with user-friendly interface.

%description -l ru
Простой и мощный плеер музыки для ОС Linux

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
%{_libdir}/python%{pyver}/site-packages/%{name}*
#{_libdir}/python%{pyver}/site-packages/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}*
%{_datadir}/pixmaps/theme/cat.jpg
%{_datadir}/pixmaps/theme/flower.jpg
%{_mandir}/man1/%{name}*

%clean
rm -rf %{buildroot}

