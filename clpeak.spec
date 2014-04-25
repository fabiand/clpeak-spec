%global commit c0b94f2f232819eeccff7251d363b65b31fa391e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global checkout .20140425git%{shortcommit}

Summary:    Find peak OpenCL capacities like bandwidth & compute
Name:       clpeak
Version:    0.1
Release:    1%{?checkout}%{?dist}
License:    Public Domain
Group:      Applications/System
URL:        https://github.com/krrishnarraj/%{name}

Source0:    %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires: cmake >= 2.6
BuildRequires: opencl-headers
BuildRequires: ocl-icd-devel
BuildRequires: mesa-libGL-devel
BuildRequires: gcc-c++

# Issue with arch specific opencl-headers
# https://bugzilla.redhat.com/show_bug.cgi?id=1027199
ExcludeArch: armv7hl


%description
A tool which profiles OpenCL devices to find their peak capacities like
bandwidth & compute.

%prep
%setup -q -n %{name}-%{commit}


%build
mkdir build
cd build

%cmake ..

make %{?_smp_mflags}


%install
mkdir -p %{buildroot}/%{_bindir}/
%{__install} -m0755 build/clpeak %{buildroot}/%{_bindir}/


%files
%doc README.md LICENSE STATUS
%{_bindir}/clpeak


%changelog
* Fri Apr 25 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.1-1.20140425gitc0b94f2
- Initial package
