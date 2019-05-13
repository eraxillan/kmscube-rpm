Name: kmscube
Summary: Metal graphics test program
Version: 0.0.1
Release: 0
Group: test
License: MIT
Source0: %{name}-%{version}.tar.gz
Source1001: %{name}.manifest

BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRequires:  pkgconfig

BuildRequires:  pkgconfig(libdrm) >= 2.4.71
BuildRequires:  pkgconfig(gbm1) >= 13.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(egl)

%description
kmscube is a little demonstration program for how to drive bare metal graphics without a compositor
like X11, wayland or similar, using DRM/KMS (kernel mode setting), GBM (graphics buffer manager)
and EGL for rendering content using OpenGL or OpenGL ES.

%prep
%setup -q -n %{name}-%{version}
cp %{SOURCE1001} .

%build
./autogen.sh --prefix=%{_prefix} --libdir=%{_libdir}
make %{?jobs:-j%jobs}

%install
%make_install

%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_bindir}/kmscube
#%{_bindir}/texturator
