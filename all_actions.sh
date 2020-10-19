#!/usr/bin/env bash

for i in stdlib numpy pandas pytorch scipy
do
  ./action.sh $i $1
done

