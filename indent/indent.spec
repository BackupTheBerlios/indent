Name		: indent
Version		: 0.1
Release		: 1
Group		: Programming/Tools

Summary         : Source code indenting program.

Copyright       : BSD with advertisment clause
Packager        : Christoph Hellwig <hch@infradead.org>
URL		: ftp://ftp.openlinux.org/pub/people/hch/indent/

BuildRoot	: /tmp/%{Name}-%{Version}
Source		: %{Name}-%{Version}.tar.gz

%Description
This is _the_ C indenter.  It reformats C sources by inserting or deleting
whitespace.  It originally came from the University of Illinois via some
distribution tape for PDP-11 Unix.  It has subsequently been hacked upon
by James Gosling @ CMU.

%Prep
%setup

%Build
CFLAGS="${RPM_OPTFLAGS}" ./configure --prefix=/usr --mandir=/usr/share/man/
make

%Install
make install DESTDIR=${RPM_BUILD_ROOT}

%Files
/usr/bin/indent
/usr/share/man/man1/indent.1*
%doc AUTHORS COPYING INSTALL NEWS README ChangeLog
