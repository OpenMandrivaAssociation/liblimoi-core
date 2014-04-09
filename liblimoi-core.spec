%define	major	0
%define	oname	limoi-core
%define	devname	%mklibname -d %{oname}

Summary:	LIM OpenMAX Integration Layer core library
Name:		lib%{oname}
Version:	0.1.0
Release:	1
Group:		System/Libraries
License:	LGPLv2.1+
Url:		http://limoa.sourceforge.net/
Source0:	%{name}-%{version}.tar.xz
Patch0:		liblimutil-0.1.2-add-missing-pthread-linkage.patch

%description
LIM OpenMAX Integration Layer core library

%libpackage %{oname} %{major}

%package -n	%{devname}
Summary:	Development headers for OpenMAX LIM utility library
Group:		Development/C

%description -n	%{devname}
Development headers for OpenMAX LIM utility library.

%files -n	%{devname}
%doc COPYING ChangeLog
%{_includedir}/OMX_*.h
%{_libdir}/lib%{oname}.so
%{_libdir}/pkgconfig/lib%{oname}.pc

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%changelog
* Wed Apr 9 2014 Per Øyvind Karlsen <proyvind@moondrake.org> 0.1.0-1
- initial release
