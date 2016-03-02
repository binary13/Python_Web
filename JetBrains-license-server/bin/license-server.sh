#!/bin/sh
# --------------------------------------------------------------------------------------
# DO NOT CHANGE THIS FILE! ALL YOUR CHANGES WILL BE ELIMINATED AFTER AUTOMATIC UPGRADE.
# --------------------------------------------------------------------------------------

JB_CURRENT_DIR=`pwd`
JB_SCRIPT_DIR=`dirname "$0"`
cd "$JB_SCRIPT_DIR/.."

jb_exit() {
  cd "$JB_CURRENT_DIR"
  exit $1
}

# workaround for Solaris; use this instead of "export a=b"
jb_export() {
  eval $1=\$2
  export $1
}

LAUNCHER_SETENV_SH="launcher/conf/launcher.setenv.sh"
if [ -f "$LAUNCHER_SETENV_SH" ]; then . "$LAUNCHER_SETENV_SH"; fi

. launcher/bin/findJava.sh

if [ -z "$MIN_REQUIRED_JAVA_VERSION" ]; then
  MIN_REQUIRED_JAVA_VERSION="1.6"
else
  version_ge $MIN_REQUIRED_JAVA_VERSION 1.6
  if [ $? -ne 0 ]; then
    echo "Cannot start launcher with Java $MIN_REQUIRED_JAVA_VERSION, will look for at least Java 1.6." 1>&2
    MIN_REQUIRED_JAVA_VERSION="1.6"
  fi
fi

EXPLICIT_JAVA_FILE="conf/$APP_FILE_NAME.java.path"
if [ -f "$EXPLICIT_JAVA_FILE" ]; then
  FJ_JAVA_EXEC=`head -n 1 "$EXPLICIT_JAVA_FILE"`
fi

find_java $MIN_REQUIRED_JAVA_VERSION $ADDITIONAL_FIND_JAVA_DIRS
if [ $? -ne 0 ]; then
  jb_exit 255
fi

jb_export FJ_JAVA_EXEC "$FJ_JAVA_EXEC"

version_ge $FJ_JAVA_VERSION 1.8
if [ $? -eq 0 ]; then
  jb_export JL_LAUNCHER_OPTS "$LAUNCHER_OPTS $LAUNCHER_MAX_METASPACE_SIZE_OPTION"
else
  jb_export JL_LAUNCHER_OPTS "$LAUNCHER_OPTS $LAUNCHER_MAX_PERM_SIZE_OPTION"
fi

jb_export JL_JAVA_PROPERTIES "$LAUNCHER_ENV_OPTS"

JB_COMMAND_SUFFIX="-jar launcher/lib/launcher.jar Main"

LAUNCH_INFO=`eval \"$FJ_JAVA_EXEC\" $JL_LAUNCHER_OPTS $JB_COMMAND_SUFFIX get-launch-info "$@" 2>/dev/null`

APP_DISPLAY_NAME=`echo "$LAUNCH_INFO" | head -1 | cut -c 3-`
IS_SERVICE=`echo "$LAUNCH_INFO" | head -2 | tail -1 | cut -c 3-`
PREP_SCRIPT=`echo "$LAUNCH_INFO" | tail -1 | cut -c 3-`

if [ -n "$IS_SERVICE" ]; then
  jb_export JL_LAUNCHER_OPTS "-Xrs $JL_LAUNCHER_OPTS"
fi

if [ -n "$PREP_SCRIPT" ]; then
  . $PREP_SCRIPT "$@"
  PREP_SCRIPT_EXIT_CODE=$?
  if [ $PREP_SCRIPT_EXIT_CODE -ne 0 ]; then
    echo "$APP_DISPLAY_NAME prep script failed: exit code $PREP_SCRIPT_EXIT_CODE" 1>&2
    echo "Prep script: $PREP_SCRIPT $@" 1>&2
    jb_exit 255
  fi
fi

JB_HOME=`pwd`
eval \"$FJ_JAVA_EXEC\" \"-Djl.service=$APP_DISPLAY_NAME Launcher\" \"-Djl.home=$JB_HOME\" $JL_LAUNCHER_OPTS $JB_COMMAND_SUFFIX "$@"
jb_exit $?
