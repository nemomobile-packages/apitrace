Name:      apitrace-x11
Version:   4.0
Release:   1%{?dist}
Summary:   Tools for tracing OpenGL, Direct3D, and other graphics APIs - X11 version

Group:	   System
License:   Apache 2.0
URL:	     http://apitrace.github.io
Source0:   %{name}-%{version}.tar.bz2
Patch0:    0001-Use-RGBA-format-in-getDrawBufferImage.patch
Patch1:    0002-Add-support-for-system-EGL-headers-and-enabling-EGL-.patch

BuildRequires: libEGL-devel
BuildRequires: libGLESv2-devel
BuildRequires: libGLESv1-devel
BuildRequires: libGL-devel
BuildRequires: cmake
BuildRequires: python

%description
apitrace consists of a set of tools to:
 * trace OpenGL, OpenGL ES, Direct3D, and DirectDraw APIs calls to a file;
 * replay OpenGL and OpenGL ES calls from a file;
 * inspect OpenGL state at any call while retracing;
 * visualize and edit trace files.

See the apitrace homepage (http://apitrace.github.io/) for more details.

%prep
%setup -q -n %{name}-%{version}/apitrace
%patch0 -p1
%patch1 -p1

%build
rm -rf build
cmake -H. -Bbuild -DCMAKE_INSTALL_PREFIX:PATH=/usr -DENABLE_GUI:STRING=FALSE -DSYSTEM_EGL:BOOL=true -DENABLE_EGL_NO_X11:BOOL=false
cd build
make -j4
cd ..

%install
rm -rf $RPM_BUILD_ROOT
cd build
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/apitrace/*
%{_docdir}/apitrace
