%define	oname	DragonMemory

Name:		dragonmemory
Version:	1.0
Release:	%mkrel 2
Summary:	A memory game where you have to match identical chips
License:	GPLv3
Group:		Games/Boards
URL:		http://dragontech.net/index.php/games-en
Source0:	http://dragontech.net/index.php/games-en?file=tl_files/dragontech/Software/%{oname}/%{oname}-source.tgz
Source1:	dragonmemory.png
Patch0:		dragonmemory-1.0-linuxpath.patch
Patch1:		dragonmemory-1.0-makefile.patch
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:	mesagl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Dragon Memory is a memory game where you have to match identical chips from
a board. The game has very detailed graphics and a lot of levels to play.

%prep
%setup -q -n %{oname}
%patch0 -p1 -b .path
%patch1 -p1 -b .makefile

%build
export CPPFLAGS="%{optflags}"
%make

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_gamesbindir}
%__cp %{name} %{buildroot}%{_gamesbindir}/

%__mkdir_p %{buildroot}%{_gamesdatadir}/%{name}

%__cp -r fonts %{buildroot}%{_gamesdatadir}/%{name}/
%__cp -r gfx %{buildroot}%{_gamesdatadir}/%{name}/
%__cp -r music %{buildroot}%{_gamesdatadir}/%{name}/
%__cp -r sounds %{buildroot}%{_gamesdatadir}/%{name}/
%__cp -r themes %{buildroot}%{_gamesdatadir}/%{name}/

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Dragon Memory
Comment=%{summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;BoardGame;
EOF

%__mkdir_p %{buildroot}%{_iconsdir}/hicolor/128x128/apps/
%__cp %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/128x128/apps/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Authors.txt License.txt
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*.png
