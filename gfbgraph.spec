#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries

Summary:	GObject library for Facebook Graph API
Summary(pl.UTF-8):	Biblioteka GObject do API Facebook Graph
Name:		gfbgraph
Version:	0.2.5
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://download.gnome.org/sources/gfbgraph/0.2/%{name}-%{version}.tar.xz
# Source0-md5:	05af5bd8af691a8e8de265fe061f6705
URL:		https://github.com/alvaropg/gfbgraph
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gnome-online-accounts-devel >= 1.0
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	json-glib-devel
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRequires:	rest-devel >= 0.7
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.198
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GObject library for Facebook Graph API.

%description -l pl.UTF-8
Biblioteka GObject do API Facebook Graph.

%package devel
Summary:	Header files for GFBGraph library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GFBGraph
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0
Requires:	gnome-online-accounts-devel >= 1.0
Requires:	json-glib-devel
Requires:	libsoup-devel >= 2.4
Requires:	rest-devel >= 0.7

%description devel
Header files for GFBGraph library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GFBGraph.

%package static
Summary:	Static GFBGraph library
Summary(pl.UTF-8):	Statyczna biblioteka GFBGraph
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GFBGraph library.

%description static -l pl.UTF-8
Statyczna biblioteka GFBGraph.

%package apidocs
Summary:	API documentation for GFBGraph library
Summary(pl.UTF-8):	Dokumentacja API biblioteki GFBGraph
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for GFBGraph library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki GFBGraph.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgfbgraph-*.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libgfbgraph-0.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgfbgraph-0.2.so.0
%{_libdir}/girepository-1.0/GFBGraph-0.2.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgfbgraph-0.2.so
%{_includedir}/gfbgraph-0.2
%{_datadir}/gir-1.0/GFBGraph-0.2.gir
%{_pkgconfigdir}/libgfbgraph-0.2.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgfbgraph-0.2.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gfbgraph-0.2
