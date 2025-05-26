%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname pyexcel-ods
%global o_srcname pyexcel_ods

Name:           pyexcel-ods
Version:        0.6.0
Release:        3%{?dist}
Summary:        A library to read, manipulate and write data in ods format
License:        New BSD
URL:            https://github.com/pyexcel/pyexcel-ods
Source0:        https://github.com/pyexcel/pyexcel-ods/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pyexcel
BuildRequires:  python%{python3_pkgversion}-odfpy
BuildRequires:  python%{python3_pkgversion}-psutil
BuildRequires:  python%{python3_pkgversion}-wheel
BuildRequires:  python%{python3_pkgversion}-nose

%{?python_enable_dependency_generator}


%define _description %{expand:
pyexcel-ods is a tiny wrapper library to read, manipulate and write data in
ods format using python.
}
%description
%_description

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%_description


%prep
%autosetup -p1 -n %{srcname}-%{version}

sed -i tests/test_multiple_sheets.py \
  -e '/testfile2.*\.xls/s/xls/ods/'

%build
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
%py3_install


%check
%{__python3} -m nose \
  -e 'TestOdsNxls.*' -e 'TestXls.*'


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE 
%doc README.rst 
# For noarch packages: sitelib
%{python3_sitelib}/%{o_srcname}/
%{python3_sitelib}/%{o_srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Wed Mar 19 2025 Edward
- New for Fedora 40 
