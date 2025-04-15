#!/usr/bin/env bash
#source ./. env

bucket=$1
echo "$bucket"

echo "Running script to zip and upload lambda"
for f in lambdas/*;do
  echo "${f}"
  zipfile=$(echo ${f} | cut -f 1 -d '.').zip
  zip -j "$(echo ${f} | cut -f 1 -d '.').zip" "${f}"
  #echo "$(cut -f 1 -d '.').zip"
done
