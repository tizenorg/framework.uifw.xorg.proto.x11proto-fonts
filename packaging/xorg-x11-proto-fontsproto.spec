Name:       xorg-x11-proto-fontsproto
Summary:    X.Org X11 Protocol fontsproto
Version:    2.1.1
Release:    0 
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/xorg-x11-proto-fontsproto.manifest 
Provides:   fontsproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}

%build
cp %{SOURCE1001} .

%reconfigure --disable-static \
    --libdir=%{_datadir}

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}






%files
%manifest xorg-x11-proto-fontsproto.manifest
%defattr(-,root,root,-)
%{_datadir}/pkgconfig/fontsproto.pc
%{_includedir}/X11/fonts/fsmasks.h
%{_includedir}/X11/fonts/FS.h
%{_includedir}/X11/fonts/fontstruct.h
%{_includedir}/X11/fonts/font.h
%{_includedir}/X11/fonts/fontproto.h
%{_includedir}/X11/fonts/FSproto.h
/usr/share/doc/fontsproto/fsproto.xml


