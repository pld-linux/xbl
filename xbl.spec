Summary:	3D geometry game
Summary(pl):	Trójwymiarowa gra na zasadach tetrisa
Name:		xbl
Version:	1.0j
Release:	7
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	ftp://ftp710.univ-lyon1.fr/pub/xbl/%{name}-%{version}.tar.Z
Source1:	%{name}.desktop
Patch0:		%{name}-config.patch
URL:		http://www710.univ-lyon1.fr/ftp/xbl/xbl.html
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
A three dimensional version of a popular arcade game.

%description -l pl
Trójwymiarowa wersja popularnej gry.

%prep
%setup -q
%patch -p1

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

gzip -9nf README xbl-README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(2755,root,games) %{_bindir}/xbl
%config %{_libdir}/X11/app-defaults/*
%{_mandir}/man6/xbl.6*
%{_applnkdir}/Games/xbl.desktop
# score files are owner by first player - so don't allow him to modify...
%attr(770,root,games) %dir /var/games/xbl
