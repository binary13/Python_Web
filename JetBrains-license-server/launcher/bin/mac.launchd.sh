#!/bin/sh
# --------------------------------------------------------------------------------------
# DO NOT CHANGE THIS FILE! ALL YOUR CHANGES WILL BE ELIMINATED AFTER AUTOMATIC UPGRADE.
# --------------------------------------------------------------------------------------
# Loads/unloads Mac OS X daemons
# Usage: ./mac.launchd.sh [load|unload] <daemon label> [<command to run as a daemon> [<command param> ...]]
# E.g.: ./mac.launchd.sh load my-script-label /path/to/my/script.sh param1 param2
#       ./mac.launchd.sh unload my-script-label
# --------------------------------------------------------------------------------------
# WARNING: Use only absolute paths inside your script started as a daemon,
#          since your working directory will be "/" (root directory).
# --------------------------------------------------------------------------------------

LABEL="$2"

case "$1" in
  load)
    shift
    shift
    launchctl remove "$LABEL" 2>/dev/null
    launchctl submit -l "$LABEL" -- "$@"
    exit $?
  ;;

  unload)
    launchctl remove "$LABEL"
    exit $?
  ;;

  *)
    echo "" 1>&2
    echo "Usage: `dirname \"$0\"`/mac.launchd.sh [load|unload] <daemon label> [<command to run as a daemon> [<command param> ...]]" 1>&2
    echo "" 1>&2
    exit 1
  ;;
esac

exit 0
