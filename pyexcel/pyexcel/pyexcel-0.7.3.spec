%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname pyexcel

Name:           pyexcel
Version:        0.7.3
Release:        2%{?dist}
Summary:        A library that provides one API for different excel formats
License:        New BSD
URL:            https://github.com/pyexcel/pyexcel
Source0:        https://github.com/pyexcel/pyexcel/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}


%define _description %{expand:
1. One application programming interface(API) to handle multiple data sources:
   * physical file
   * memory file
   * SQLAlchemy table
   * Django Model
   * Python data structures: dictionary, records and array
2. One API to read and write data in various excel file formats.
3. For large data sets, data streaming are supported. A genenerator can be
   returned to you. Checkout iget_records, iget_array, isave_as and
   isave_book_as.
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


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE 
%doc README.rst 
# For noarch packages: sitelib
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Mon May 26 2025 Martin RS - 0.7.3
- Update
* Wed Mar 19 2025 Martin RS - 0.7.1
- Initial
