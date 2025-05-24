%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname meza

Name:           python-%{srcname}
Version:        0.47.0
Release:        1%{?dist}
Summary:        Python toolkit for processing tabular data
License:        MIT
URL:            https://github.com/reubano/meza
Source0:        https://github.com/reubano/meza/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-responses

%generate_buildrequires
%pyproject_buildrequires -r

%define _description %{expand:
meza is a Python library for reading and processing tabular data. It has
a functional programming style API, excels at reading/writing large files,
and can process 10+ file types.}
%description
%_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python%{python3_pkgversion}-%{srcname}
%_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -i requirements.txt -e 's/,<.*//' -e 's/==/>=/'

# update to python3-dbfread 2.0.7 instead of 2.0.4:
# read_header(.) instead of read_headers(.)
#ed meza/dbf.py <<EOF
#/^class DBF2(/
#/self._read_headers(/
#s/\(self._read_header\)s\(([^,)]*\),.*/\1\2)/
#p
#wq
#EOF


%build
%pyproject_wheel


%install
rm -rf $RPM_BUILD_ROOT
%pyproject_install


%check
pushd build/lib
ln -s ../../data
%pytest


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE 
%doc README.rst 
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/


%changelog
* Tue May 20 2025 Martin RS - 0.47.0
- Update
* Sat May 04 2024 Martin RS
- for Fedora 38/40
* Wed Feb 22 2023 Martin RS
- patch for Fedora 37
* Wed Oct 05 2022 Martin RS -0.46.0
- for Fedora 35
