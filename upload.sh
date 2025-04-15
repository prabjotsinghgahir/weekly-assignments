#!/usr/bin/env bash
#source ./. env

echo "Running script to zip and upload lambda"
for f in lambdas/*;do
  echo "${f}"
  zipfile = $(echo ${f} | cut -f 1 -d '.').zip
  zip -j "${zipfile}" "${f}"
