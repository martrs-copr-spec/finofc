%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname pyexcel-io
%global o_srcname pyexcel_io
%global o_version 0.6.7

Name:           pyexcel-io
Version:        0.6.7.1
Release:        3%{?dist}
Summary:        A python library to read and write structured data in csv
License:        New BSD
URL:            https://github.com/pyexcel/pyexcel-io
Source0:        https://github.com/pyexcel/pyexcel-io/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-lml
BuildRequires:  python%{python3_pkgversion}-chardet
BuildRequires:  python%{python3_pkgversion}-sqlalchemy
BuildRequires:  python%{python3_pkgversion}-nose

%{?python_enable_dependency_generator}


%define _description %{expand:
pyexcel-io provides one application programming interface(API) to read
and write the data in excel format, import the data into and export the data
from database. It provides support for csv(z) format, django database and
sqlalchemy supported databases.
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


%build
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
%py3_install


%check
# we don't use pyexcel
rm -f tests/test_pyexcel_integration.py
sed -i -e '/import pyexcel /d' tests/test_issues.py
sed -i -e '/get_io_type.*xls.*/,+1d' tests/test_io.py
%{__python3} -m nose \
  -e '.*test_issue_43' -e '.*test_write_xlsx_data'


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE CHANGELOG.rst CONTRIBUTORS.rst
%doc README.rst 
# For noarch packages: sitelib
%{python3_sitelib}/%{o_srcname}/
%{python3_sitelib}/%{o_srcname}-%{o_version}-py%{python3_version}.egg-info/


%changelog
* Tue Mar 18 2025 Martin RS - 0.6.7.1
- Initial
