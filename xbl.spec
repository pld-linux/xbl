Summary:	3D geometry game
Summary(de):	3D-Geometriespiel
Summary(es):	Juego geométrico en 3D
Summary(fr):	Jeu en géometrie 3D
Summary(pl):	Trójwymiarowa gra na zasadach tetrisa
Summary(pt_BR):	Jogo geométrico em 3d
Summary(tr):	Üç boyutlu geometri oyunu
Name:		xbl
Version:	1.1.4
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www710.univ-lyon1.fr/ftp/xbl/%{name}-%{version}.tar.gz
# Source0-md5:	217127882e5999f8b20c499d24e2ee04
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-config.patch
URL:		http://www710.univ-lyon1.fr/ftp/xbl/xbl.html
BuildRequires:	autoconf
BuildRequires:	xorg-lib-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	%{_datadir}/X11/app-defaults

%description
A three dimensional version of a popular arcade game.

%description -l es
Una versión en tres dimensiones de un popular juego del tipo arcade.

%description -l de
Eine 3D-Version eines beliebten Spielhallen-Games.

%description -l fr
Version tri-dimensionnelle d'un célèbre jeu d'arcade.

%description -l pl
Trójwymiarowa wersja popularnej gry.

%description -l pt_BR
Uma versão em três dimensões de um popular jogo do tipo arcade.

%description -l tr
Popüler oyunun üç boyutlu bir sürümü.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

# just copy of app-defaults
rm -f $RPM_BUILD_ROOT/var/games/xbl/Xbl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README xbl-README
%attr(2755,root,games) %{_bindir}/xbl
%{_datadir}/xbl
%{_appdefsdir}/Xbl
%{_mandir}/man6/xbl.6*
%{_desktopdir}/xbl.desktop
%{_pixmapsdir}/*
# score files are owner by first player - so don't allow him to modify...
%attr(770,root,games) %dir /var/games/xbl
