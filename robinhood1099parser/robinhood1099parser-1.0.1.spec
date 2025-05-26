%{?!python3_pkgversion:%global python3_pkgversion 3}

%global srcname Robinhood-1099-Parser
%global o_srcname rh_1099

Name:           robinhood1099parser
Version:        1.0.1
Release:        1%{?dist}
Summary:        Convert Robinhood Securities 1099 tax document from PDF to CSV
License:        AGPL-3.0
URL:            https://github.com/kevinpark1217/Robinhood-1099-Parser
Source0:        https://github.com/kevinpark1217/Robinhood-1099-Parser/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pdfreader
BuildRequires:  python%{python3_pkgversion}-tqdm

%{?python_enable_dependency_generator}

%description
This project converts Robinhood Securities 1099 tax document from PDF to
CSV file. This tool will be helpful for those who need every transaction
in a spreadsheet format for tax reporting purposes.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py3_build


%install
rm -rf $RPM_BUILD_ROOT
%py3_install


%check
# use what your upstream is using
%{__python3} setup.py test || :


%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{o_srcname}
# For noarch packages: sitelib
%{python3_sitelib}/%{o_srcname}/
%{python3_sitelib}/%{o_srcname}-%{version}-py%{python3_version}.egg-info/


%changelog
* Sat Sep 03 2022 Martin RS - 1.0.1
- Initial
