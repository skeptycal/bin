#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import platform

# import autosys

# make usage dict for all utilities
# ... better yet, make a class to contain all utilities


print(platform.system())


def getURL():
    pass


"""
getURL() {
    # copy URL from active tab of Google Chrome to macOS clipboard
    if [$OS = 'darwin']
    then
    url =$(osascript - e 'tell application "Google Chrome" to return URL of active tab of front window')
    # printf "%s" "$url" | pbcopy # skip clipboard on -v

    # -v is verbose : print url to stdout in addition to clipboard
    if ["$1"= '-v']
    then
    printf "%s\n" "$url"
    else
    printf "%s" "$url" | pbcopy
    fi
    return $url
    fi
}

ping_avg() {
    # extract the average ping time (ms) from 'ping' output
    # $1 = number of pings to average
    # $2 = url to test
    count =$1
    url =$(echo "$2" | cut - d '/' - f 3)  # remove schema and folders
    ping - c "$count" "$url" | tail - n 1 | cut - d '/' - f 6
}

log_urls() {
    # ref: https://www.cyberciti.biz/faq/linux-unix-sleep-bash-scripting/
    url_log = ~ / .url_log.log
    # shellcheck disable=SC2078
    while [:]
    do
    url = getURL - v
    # >>$url_log
    printf "%s\n" "$(date), $url, $(ping_avg 2 $url), $(ping_avg 2 'www.example.com')"
    printf "%s\n" "$(date), $url, $(ping_avg 2 $url), $(ping_avg 2 'www.example.com')" >>$url_log
    sleep 10
    done
}

log_urls

"""
