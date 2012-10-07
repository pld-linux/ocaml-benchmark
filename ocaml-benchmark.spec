Summary:	Benchmark - measure/compare run-time of OCaml functions
Summary(pl.UTF-8):	Biblioteka benchmark - mierzenie i porównywanie czasu działania funkcji ocamlowych
Name:		ocaml-benchmark
Version:	1.1
Release:	1
License:	LGPL v3 with linking exception
Group:		Development/Languages
Source0:	http://forge.ocamlcore.org/frs/download.php/734/benchmark-%{version}.tar.gz
# Source0-md5:	ae6885082c68f319ded4a1bb25ec5b37
URL:		http://forge.ocamlcore.org/projects/ocaml-benchmark/
BuildRequires:	ocaml >= 3.04-7
BuildRequires:	ocaml-camlp4
%requires_eq	ocaml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Benchmark provides functions to measure and compare the run-time of
OCaml functions. It is inspired by the Perl module of the same name.

%description -l pl.UTF-8
Biblioteka benchmark dostarcza funkcje do mierzenia i porównywania
czasu działania funkcji ocamlowych. Została zainspirowana modułem
Perla o tej samej nazwie.

%prep
%setup -q -n benchmark-%{version}

%build
ocaml setup.ml -configure \
	--prefix %{_prefix}

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/benchmark

%{__make} install \
	OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml

mv -f $RPM_BUILD_ROOT%{_libdir}/ocaml/benchmark/META $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/benchmark
cat >>$RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/benchmark/META <<EOF
directory="+benchmark"
EOF

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/benchmark/benchmark.mli

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt benchmark.mli
%dir %{_libdir}/ocaml/benchmark
%{_libdir}/ocaml/benchmark/benchmark.a
%{_libdir}/ocaml/benchmark/benchmark.cm[aix]*
%{_libdir}/ocaml/site-lib/benchmark
%{_examplesdir}/%{name}-%{version}
