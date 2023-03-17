#!/bin/bash

last=$( printf '%s\n' prab* | sed -nE 's/^prab([0-9]+)$/\1/p' | sort -rn | head -n 1)
  for ((i = last+1, j=last+25; i <= j; i++))
  do
     touch "prab$i"
  done

