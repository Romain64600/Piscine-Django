#!/bin/sh

curl -I $1 | grep Location | cut -d : -f 2,3
