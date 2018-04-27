#! /bin/sh
# This is for executing the webcontrol python code at boot

PATH=/sbin:/bin:/usr/sbin:/usr/bin
DAEMON=/home/pi/Desktop/throwing-shade/our_code/webControl.py
NAME=shady
SNAME=shady
DESC="Shade Web Interface"
PIDFILE="/var/run/$NAME.pid"

export TMPDIR=/tmp

test -f $DAEMON || exit 0

set -e

case "$1" in
	start)
echo -n "Starting $DESC: "
	$DAEMON
	echo "$NAME."
	;;

	stop)
echo -n "Stopping $DESC: "
	pkill -SIGKILL $NAME
	echo "$NAME."
	;;

restart | force-reload)
echo -n "Restarting $DESC: "
	pkill -9 $NAME
	$DAEMON
	echo "$NAME."
	;;

*)
	N=/etc/init.d/$SNAME
	echo "Usage: $N {start|stop}" >&2
	exit 1
	;;
esac

exit 0
