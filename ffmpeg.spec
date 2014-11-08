Summary:	Realtime audio/video encoder and streaming server
Name:		ffmpeg
Version:	2.4.3
Release:	1
License:	GPL v3
Group:		Applications/Multimedia
Source0:	http://ffmpeg.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	8da635baff57d7ab704b1daca5a99b47
URL:		http://ffmpeg.org/
BuildRequires:	SDL-devel
BuildRequires:	flac-devel
BuildRequires:	freetype-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	lame-libs-devel
BuildRequires:	libass-devel
BuildRequires:	libbluray-devel
BuildRequires:	libdc1394-devel
BuildRequires:	libraw1394-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtool
BuildRequires:	libva-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libvpx-devel
BuildRequires:	libx264-devel
BuildRequires:	nasm
BuildRequires:	opencore-amr-devel
BuildRequires:	opus-devel
BuildRequires:	perl-tools-pod
BuildRequires:	texinfo
BuildRequires:	v4l-utils-devel
BuildRequires:	vo-aacenc-devel
BuildRequires:	xvidcore-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
ffmpeg is a hyper fast realtime audio/video encoder and streaming
server. It can grab from a standard Video4Linux video source and
convert it into several file formats based on DCT/motion compensation
encoding. Sound is compressed in MPEG audio layer 2 or using an AC3
compatible stream.

%package libs
Summary:	ffmpeg libraries
Group:		Libraries

%description libs
This package contains ffmpeg shared libraries.

%package devel
Summary:	ffmpeg header files
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
ffmpeg header files.

%prep
%setup -q

%build
# not autoconf configure
./configure \
	--arch=%{_target_base_arch}	\
	--libdir=%{_libdir}		\
	--mandir=%{_mandir}		\
	--prefix=%{_prefix}		\
	--shlibdir=%{_libdir}		\
	--cc="%{__cc}"			\
	--extra-cflags="%{rpmcflags}"	\
	--extra-ldflags="%{rpmldflags}"	\
	--disable-debug			\
	--disable-ffplay		\
	--disable-ffserver		\
	--disable-static		\
	--disable-stripping		\
	--enable-avresample		\
	--enable-gnutls			\
	--enable-gpl			\
	--enable-libass			\
	--enable-libbluray		\
	--enable-libdc1394		\
	--enable-libfreetype		\
	--enable-libmp3lame		\
	--enable-libopencore-amrnb	\
	--enable-libopencore-amrwb	\
	--enable-libopus		\
	--enable-libtheora		\
	--enable-libv4l2		\
	--enable-libvo-aacenc		\
	--enable-libvorbis		\
	--enable-libvpx			\
	--enable-libx264		\
	--enable-libxvid		\
	--enable-postproc		\
	--enable-pthreads		\
	--enable-runtime-cpudetect	\
	--enable-shared			\
	--enable-swresample		\
	--enable-vaapi			\
	--enable-version3		\
	--enable-x11grab
%{__make} V=1

%{__make} tools/qt-faststart V=1 CC_O='-c -o $@'

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/ffmpeg/examples

install -p tools/qt-faststart $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
#%doc README doc/RELEASE_NOTES
# BR tetex doc/*.html
%attr(755,root,root) %{_bindir}/ffmpeg
%attr(755,root,root) %{_bindir}/ffprobe
%attr(755,root,root) %{_bindir}/qt-faststart
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.ffpreset
%{_datadir}/%{name}/*.xsd
%{_mandir}/man1/ffmpeg*.1*
%{_mandir}/man1/ffprobe*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libavcodec.so.56
%attr(755,root,root) %ghost %{_libdir}/libavdevice.so.56
%attr(755,root,root) %ghost %{_libdir}/libavfilter.so.5
%attr(755,root,root) %ghost %{_libdir}/libavformat.so.56
%attr(755,root,root) %ghost %{_libdir}/libavresample.so.2
%attr(755,root,root) %ghost %{_libdir}/libavutil.so.54
%attr(755,root,root) %ghost %{_libdir}/libpostproc.so.53
%attr(755,root,root) %ghost %{_libdir}/libswresample.so.1
%attr(755,root,root) %ghost %{_libdir}/libswscale.so.3
%attr(755,root,root) %{_libdir}/libavcodec.so.*.*.*
%attr(755,root,root) %{_libdir}/libavdevice.so.*.*.*
%attr(755,root,root) %{_libdir}/libavfilter.so.*.*.*
%attr(755,root,root) %{_libdir}/libavformat.so.*.*.*
%attr(755,root,root) %{_libdir}/libavresample.so.*.*.*
%attr(755,root,root) %{_libdir}/libavutil.so.*.*.*
%attr(755,root,root) %{_libdir}/libpostproc.so.*.*.*
%attr(755,root,root) %{_libdir}/libswresample.so.*.*.*
%attr(755,root,root) %{_libdir}/libswscale.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/optimization.txt
%attr(755,root,root) %{_libdir}/libavcodec.so
%attr(755,root,root) %{_libdir}/libavdevice.so
%attr(755,root,root) %{_libdir}/libavfilter.so
%attr(755,root,root) %{_libdir}/libavformat.so
%attr(755,root,root) %{_libdir}/libavutil.so
%attr(755,root,root) %{_libdir}/libpostproc.so
%attr(755,root,root) %{_libdir}/libswresample.so
%attr(755,root,root) %{_libdir}/libswscale.so
%attr(755,root,root) %{_libdir}/libavresample.so
%{_includedir}/libavcodec
%{_includedir}/libavdevice
%{_includedir}/libavfilter
%{_includedir}/libavformat
%{_includedir}/libavresample
%{_includedir}/libavutil
%{_includedir}/libpostproc
%{_includedir}/libswresample
%{_includedir}/libswscale
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/libavcodec.3*
%{_mandir}/man3/libavdevice.3*
%{_mandir}/man3/libavfilter.3*
%{_mandir}/man3/libavformat.3*
%{_mandir}/man3/libavutil.3*
%{_mandir}/man3/libswresample.3*
%{_mandir}/man3/libswscale.3*

